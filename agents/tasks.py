from django.core.mail import send_mail

from basiccrm.celery import app


@app.task()
def send_created_email(username, password, email):
    send_mail(
        subject='Account Created',
        message=f'An account was created for you in BasicCRM. '
                f'Your username is {username} and your password is {password}',
        from_email='jrahmonov2@gmail.com',
        recipient_list=[email]
    )
