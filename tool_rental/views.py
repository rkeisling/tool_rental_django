from django.shortcuts import render, redirect
from .models import Tool
from .forms import RentTool

def pricing(request):
    """
    Goes to the pricing page.
    """
    return render(request, 'tool_rental/pricing.html', {})

def rules(request):
    """
    Goes to the terms and conditions page.
    """
    return render(request, 'tool_rental/rules.html', {})

def error(request):
    """
    Goes to the 'error' page; usually happens when a user tries to rent an
    item that is out of stock.
    """
    return render(request, 'tool_rental/error.html', {})

def calc_price(days, tool):
    """
    Calculates the price of a tool for however many days it's being rented.
    """
    prices = {'prices_day': {'auger': 80,
                             'nailgun': 40,
                             'tilesaw': 60,
                             'air compressor': 120,
                             'generator': 200},
              'prices_week': {'auger': 40,
                              'nailgun': 30,
                              'tilesaw': 45,
                              'air compressor': 90,
                              'generator': 150},
              'prices_month': {'auger': 20,
                               'nailgun': 15,
                               'tilesaw': 30,
                               'air compressor': 60,
                               'generator': 100}}
    if days == 1:
        return (days*prices['prices_day'][str(tool).lower()])*1.07
    elif days > 1 and days < 8:
        return (days*prices['prices_week'][str(tool).lower()])*1.07
    else:
        return (days*prices['prices_month'][str(tool).lower()])*1.07

def rent_tool(request):
    """
    Goes to the home page, error page, or receipt page; has different outcomes
    depending on user input and request type.
    """
    if request.method == "POST":
        form = RentTool(request.POST)
        if form.is_valid():
            try:
                tool_id = form.cleaned_data['tool_name']
                days = form.cleaned_data['days_renting']
                curr_tool = Tool.objects.get(id=tool_id)
                if curr_tool.num_available > 0:
                    curr_tool.rent()
                    curr_tool.save()
                    return render(request,
                                  'tool_rental/trans_complete.html',
                                  {'tool': curr_tool.tool_name,
                                   'days': days,
                                   'owed': "{0:.2f}".format(calc_price(days, curr_tool))})
                else:
                    return render(request, 'tool_rental/error.html', {})
            except TypeError:
                return redirect('error')
    else:
        in_stock = Tool.objects.filter(num_available__gte=1)
        form = RentTool()
        return render(request, 'tool_rental/index.html', {'form': form, 'in_stock': in_stock})
