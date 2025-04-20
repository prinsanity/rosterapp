from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    name = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()  # Store table data dynamically as JSON
    status = models.CharField(
        max_length=20,
        choices=[
            ('planning', 'Planning'),
            ('editing', 'Editing'),
            ('viewing', 'Viewing'),
        ],
        default='planning',
    )

    def __str__(self):
        return self.name