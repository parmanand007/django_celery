from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django_celery import settings

@shared_task(bind=True)
def send_mail_func(self):
    users=get_user_model().objects.all()
    for user in users:
        #send email here
        mail_sub="Hi ! Celery testing"
        message="testing celery"
        to_email=user.email
        send_mail(
            subject=mail_sub,message=message,from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True
        )

    return "Done"