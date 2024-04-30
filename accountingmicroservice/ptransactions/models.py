from django.db import models
from accountingmicroservice.users.models import *


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'Transaction for {self.user.username} on {self.transaction_date}'
