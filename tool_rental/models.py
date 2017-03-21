""" Django tool rental project. """

from django.db import models
from django.utils import timezone


class Tool(models.Model):
    """
    Models a tool.
    """
    tool_name = models.CharField(max_length=50)
    tool_descrip = models.TextField()
    price = models.FloatField()
    date_added = models.DateTimeField(default=timezone.now())
    date_rented = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.tool_name

    def is_expensive(self):
        """
        Returns a bool on whether or not the item is expensive (over 150 dollars).
        """
        return self.price > 150

    def rent(self):
        """
        Removes item from inventory, changes date rented to whenever it was rented.
        """
        self.date_rented = timezone.now()
        self.save()
