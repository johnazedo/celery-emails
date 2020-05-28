from celery.decorators import task
from django.core.mail import send_mail

@task(name="sendEmail")
def send_emails():
    send_mail(
        'CeleryEmails',
        'That worked very well',
        'jplimao12@gmail.com',
        ['selok19729@gilfun.com']
    )

    return None
