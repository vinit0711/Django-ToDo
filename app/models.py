from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODO(models.Model):

    status_choices = [
    ('C', 'Completed'),
    ('P', 'Pending'),
    ]
    priority_choices = [
    ('1', '1️⃣'),
    ('2', '2️⃣'),
    ('3', '3️⃣'),
    ('4', '4️⃣'),
    ('5', '5️⃣'),]
    task = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    priority=models.CharField(max_length=2, choices=priority_choices)


