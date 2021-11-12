from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, TemplateView

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


class Register(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'

    def get_success_url(self):
        user = self.request.body.decode().split('&')[1].split('=')[1]
        return reverse('barcode', kwargs={'username': user})


class TOTPCreateView(View):
    """
    Use this endpoint to set up a new TOTP device
    """
    # permission_classes = [permissions.IsAuthenticated]
    template_name = "barcode.html"

    def get(self, request, *args, **kwargs):
        context = {}
        username = kwargs['username']
        user = User.objects.get(username=username)
        device = get_user_totp_device(self, user)
        if not device:
            device = user.totpdevice_set.create(confirmed=True)
        url = device.config_url
        context['device'] = url
        print(context)
        return render(request, 'barcode.html', context)

# class TOTPVerifyView(views.APIView):
#
# """
# Use this endpoint to verify/enable a TOTP device
# """
# permission_classes = [permissions.IsAuthenticated]
#
# def post(self, request, token, format=None):
#     user = request.user
#     device = get_user_totp_device(self, user)
#     if not device == None and device.verify_token(token):
#         if not device.confirmed:
#             device.confirmed = True
#             device.save()
#         return Response(True, status=status.HTTP_200_OK)
#     return Response(status=status.HTTP_400_BAD_REQUEST)
