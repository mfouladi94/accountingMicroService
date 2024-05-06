from django.db import models
from accountingmicroservice.wallet.models import *


class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE , blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')] , default="deposit")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'Transaction for {self.wallet.id} on {self.created_at}'

