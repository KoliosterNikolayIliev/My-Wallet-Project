from django.http import HttpResponse
from django.shortcuts import render

from monitor_app.utils import get_number_of_users, get_assets


def index_view(request):
    users = get_number_of_users()
    assets = get_assets()
    if request.method == 'GET':
        context = {
            'users': users,
            'total_assets': assets
        }
        return render(request, 'index.html', context)
    return HttpResponse('FORBIDDEN!', status=405)



