from django.shortcuts import get_object_or_404
from django.shortcuts import render;
from django.views import generic;
from django.views.generic import DetailView

from ..tasks import add, send_email
from cms.models import Post
from cms.models import User

def index(request, pk):
   
    # Render the HTML template index.html with the data in the context variable
    add.delay(14,7)
    send_email.delay_on_commit(15641)
    return render(request, 'cms/post.html', {"pk": pk})

class PostDetailView(DetailView):
    context_object_name = "post"
    template_name = "cms/post.html"
    # queryset = Post.objects.all()
    
    def get_queryset(self):
         return Post.objects.filter(pk=self.kwargs["pk"])
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["users"] = User.objects.all()
        return context