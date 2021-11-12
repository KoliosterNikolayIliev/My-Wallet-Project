from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from monitor_app.forms import RegisterForm
from monitor_app.utils import get_number_of_users, get_assets, get_user_totp_device


@login_required
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


def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        context = {}
        device = get_user_totp_device(user=user)
        if not device:
            device = user.totpdevice_set.create(confirmed=True)
        url = device.config_url
        context['device'] = url
        return render(request, 'registration/login.html', context)
    context = {'form': form}
    return render(request, 'register.html', context)
