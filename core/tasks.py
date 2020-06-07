from celery.decorators import task
from django.core.mail import send_mail
import time

@task(name="sendEmail")
def send_emails():
    send_mail(
        'CeleryEmails',
        'That worked very well',
        'jplimao12@gmail.com',
        ['selok19729@gilfun.com']
    )

    return None


@task(name="example")
def example():
    for i in range(10):
        time.sleep(1)
        print(i)

    return None