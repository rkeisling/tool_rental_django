""" Django tool rental project. """

from django.db import models
from django.utils import timezone


class Tool(models.Model):
    """
    Models a tool.
    """
    tool_name = models.CharField(max_length=50)
    num_available = models.IntegerField(default=0)
    num_rented = models.IntegerField(default=0)
    date_last_rented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tool_name

    def rent(self):
        """
        Removes item from inventory, changes date rented to whenever it was rented.
        """
        self.num_available -= 1
        self.num_rented += 1
        self.date_last_rented = timezone.now()
        self.save()
