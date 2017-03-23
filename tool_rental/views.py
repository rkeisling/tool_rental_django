from django.shortcuts import render
from .models import Tool
from django.utils import timezone


def tool_list(request):
    equip = Tool.objects.all()
    return render(request, 'tool_rental/tool_list.html', {'equip': equip})

def home(request):
    equip = Tool.objects.all()
    return render(request, 'tool_rental/index.html', {'equip': equip})

def pricing(request):
    return render(request, 'tool_rental/pricing.html', {})

def rules(request):
    return render(request, 'tool_rental/rules.html', {})

def rent_tool(request):
    if request.is_ajax:
        tool = Tool.objects.get(tool_name=request[name])
        tool.rent()
        tool.save()
    else:
        return HttpRequest(status=400)
