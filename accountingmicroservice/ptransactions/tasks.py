from celery import shared_task

from .models import Transaction, Wallet


@shared_task
def update_wallet_balance(transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    wallet = transaction.wallet
    if transaction.type == 'deposit':
        wallet.balance += transaction.amount
    else:
        wallet.balance -= transaction.amount
    wallet.save()
