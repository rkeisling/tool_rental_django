from django import forms
from .models import Tool


class RentTool(forms.Form):
    """
    This form contains two fields: tool_name, which is a dropdown that lets the
    user select the name of the tool they would like to rent, and days_renting,
    an input field that the user can input an integer on how long they want to rent the tool.
    """
    tool_name = forms.ChoiceField(
        label="Tool Name:",
        choices=lambda: [(tool.id, tool) for tool in Tool.objects.all()],
        required=True)
    days_renting = forms.IntegerField(label="Days Renting:", required=True, initial=1)
