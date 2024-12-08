from celery import shared_task
from claremont_church.celery import app
from cms.models import User


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def send_email(user_pk):
    # user = User.objects.get(pk=user_pk)
    return f"{user_pk}: has its email sent successfully."