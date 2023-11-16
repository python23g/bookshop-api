from django.db import models
from apps.orders.models import Order


class Payment(models.Model):
    status_choices = [
        ("Pending", "Pending"),
        ("Success", "Success"),
        ("Failed", "Failed"),
    ]
    payment_method_choices = [
        ("Credit Card", "Credit Card"),
        ("cash", "Cash"),
        ("other", "Other"),
    ]
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, default='cash', choices=payment_method_choices)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending', choices=status_choices)

    def __str__(self):
        return f"Payment for Order #{self.order.id}"

    class Meta:
        ordering = ['-timestamp']
