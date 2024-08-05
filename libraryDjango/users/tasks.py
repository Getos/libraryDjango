import time

from celery import shared_task


@shared_task
def send_mass_emails(recipient):
    print(f"sending welcome email: welcome user {recipient}")
    time.sleep(5)
    print("sent")
    return


# @shared_task
# def send_scheduled_emails():
#      print("started to sleep")
#      return
