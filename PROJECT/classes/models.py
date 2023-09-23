import uuid
from django.db import models
from django.utils import timezone


class UClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.CharField(max_length=128)
    time = models.CharField(max_length=128)
    capacity = models.CharField(max_length=128)
    teacher = models.CharField(max_length=256, null=True)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
    
class UStudents(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class_id = models.CharField(max_length=64)
    g_name = models.CharField(max_length=128)
    g_email = models.CharField(max_length=128)
    c_name = models.CharField(max_length=128)
    c_age = models.CharField(max_length=128)
    message = models.TextField(null=True)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"