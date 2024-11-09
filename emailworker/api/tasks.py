from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@shared_task
def send_email(recipient_email,username,template,subject):
        subject = subject
        from_email = settings.EMAIL_HOST_USER  # Replace with your from email
        to = recipient_email

        html_content = render_to_string(f'api/{template}.html', {
                'username': username,
        })
        text_content = strip_tags(html_content)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()




