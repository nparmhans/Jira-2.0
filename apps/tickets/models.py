from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Ticket(models.Model):
    HIGH = '1'
    MEDIUM = '2'
    LOW = '3'
    PRIORITY_LEVEL = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    )
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    priority_level = models.CharField(max_length=2,
                                      choices=PRIORITY_LEVEL,
                                      default=LOW)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} {}".format(self.title, self.description, self.priority_level)
