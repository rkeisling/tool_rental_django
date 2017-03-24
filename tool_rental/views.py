from django.shortcuts import render
from .models import Tool
from django.utils import timezone
from .forms import RentTool


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
    if request.method == "POST":
        form = RentTool(request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.num_available -= 1
            tool.save()
    else:
        form = RentTool()
    return render(request, 'tool_rental/index.html', {'form': form})
