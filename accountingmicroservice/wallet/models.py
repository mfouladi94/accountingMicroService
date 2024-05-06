from django.db import models



class Wallet(models.Model):
    userId = models.PositiveIntegerField(default=1)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Wallet for {self.userId} - {self.balance}'
