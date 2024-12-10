from django.shortcuts import get_object_or_404
from django.shortcuts import render;
from django.views import generic;
from django.views.generic import DetailView

from ..tasks import add, send_email
from cms.models import Post

def index(request, pk):
   
    # Render the HTML template index.html with the data in the context variable
    add.delay(14,7)
    send_email.delay_on_commit(15641)
    return render(request, 'cms/post.html', {"pk": pk})

class PostDetailView(DetailView):
    context_object_name = "post"
    template_name = "cms/post.html"
    queryset = Post.objects.all()
    
    # def get_queryset(self):
    #      return get_object_or_404(Post, id=self.kwargs["pk"])