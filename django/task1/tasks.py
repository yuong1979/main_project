

##########################################################################################################################
######### For sending automated emails every 5 seconds - make changes on settings.py CELERY_BEAT_SCHEDULE ################
##########################################################################################################################

# from __future__ import absolute_import, unicode_literals

# from celery import shared_task

# from django.conf import settings
# from django.template.loader import render_to_string
# from django.core.mail import EmailMessage
# from celery.utils.log import get_task_logger


# logger = get_task_logger(__name__)

# @shared_task
# def send_test_email():

#     email = 'yuong1979@gmail.com'
#     context = {
#         'test_field': "testing",
#     }

#     email_subject = 'Testing Email'
#     email_body = render_to_string('email_message.txt', context)

#     email = EmailMessage(
#         email_subject, email_body,
#         settings.DEFAULT_FROM_EMAIL, [email, ],
#     )
#     return email.send(fail_silently=False)










from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def add(x, y):
    return x + y