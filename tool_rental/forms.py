from django import forms
from .models import Tool


class RentTool(forms.Form):
    tool_name = forms.ChoiceField(
        label="Tool Name:",
        choices=lambda: [
            (tool.id, tool) for tool in Tool.objects.all()
        ],
        required=True)
    days_renting = forms.IntegerField(
        label="Days Renting:",
        required=True,
        initial=1
    )
