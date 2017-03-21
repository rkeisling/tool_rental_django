from django.shortcuts import render


def tool_list(request):
    return render(request, 'tool_rental/tool_list.html', {})
