from django.shortcuts import render
from .models import Tool
from django.utils import timezone


def tool_list(request):
    tools = Tool.objects.order_by('price')
    return render(request, 'tool_rental/tool_list.html', {'tools': tools})
