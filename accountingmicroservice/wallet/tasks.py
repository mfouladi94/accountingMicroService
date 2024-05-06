from celery import shared_task

from time import sleep


@shared_task
def my_task():
    for i in range(10):
        print(i)
        sleep(1)
    return "Task Complete"


@shared_task
def check_wallet_balance_task():
    for i in range(10):
        print(i)
        sleep(1)
    return "Task Complete"

