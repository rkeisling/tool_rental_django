""" Django tool rental project. """

from django.db import models
from django.utils import timezone


class Tool(models.Model):
    """
    Models a tool.
    """
    tool_name = models.CharField(max_length=50)
    tool_descrip = models.TextField()
    day_price = models.FloatField(default=0)
    week_price = models.FloatField(default=0)
    month_price = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now())
    date_rented = models.DateTimeField(blank=True, null=True)
    num_available = models.IntegerField(default=0)

    def __str__(self):
        return self.tool_name

    def rent(self):
        """
        Removes item from inventory, changes date rented to whenever it was rented.
        """
        if self.num_available > 0:
            self.num_available -= 1
        else:
            return "Sorry, that item is not available!"
        self.date_rented = timezone.now()
        self.save()
