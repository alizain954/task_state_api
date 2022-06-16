
from django.db import models

# Create your models here.


class Task(models.Model):
    state = models.CharField(
        choices=[
            ('draft', 'draft'),
            ('active', 'active'),
            ('done', 'done'),
            ('archived', 'archived'),
        ],
        max_length=8,
    )
    title = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title