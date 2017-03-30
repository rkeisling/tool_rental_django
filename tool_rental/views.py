from django.shortcuts import render, redirect
from .models import Tool
from .forms import RentTool
from django.contrib import messages

def home(request):
    equip = Tool.objects.all()
    return render(request, 'tool_rental/index.html', {'equip': equip})

def pricing(request):
    return render(request, 'tool_rental/pricing.html', {})

def rules(request):
    return render(request, 'tool_rental/rules.html', {})

def error(request):
    return render(request, 'tool_rental/error.html', {})

def rent_tool(request):
    if request.method == "POST":
        form = RentTool(request.POST)
        if form.is_valid():
            try:
                tool_id = form.cleaned_data['tool_name']
                days = form.cleaned_data['days_renting']
                curr_tool = Tool.objects.get(id=tool_id)
                curr_tool.rent()
                curr_tool.save()
                return render(request,
                              'tool_rental/trans_complete.html',
                              {'tool': curr_tool.tool_name,
                               'days': days,
                               'owed': 0})
            except TypeError:
                return redirect('error')
    else:
        form = RentTool()
        return render(request, 'tool_rental/index.html', {'form': form})
