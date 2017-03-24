from django import forms
from .models import Tool

class RentTool(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ('tool_name',)
