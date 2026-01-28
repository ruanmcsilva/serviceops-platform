from django.db import models
from django.utils.timezone import now

class Order(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('CLOSED', 'Closed'),
    ]

    customer = models.ForeignKey(
        'customers.Customer',
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == 'CLOSED' and self.closed_at is None:
            self.closed_at = now()
        super().save(*args, **kwargs)

class OrderService(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.service.price
        super().save(*args, **kwargs)
    