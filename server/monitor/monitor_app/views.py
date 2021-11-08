from django.shortcuts import render
from django.views.generic import ListView

from monitor_app.models import Monitor


class IndexView(ListView):
    model = Monitor
    context_object_name = 'monitor'
    template_name = "index.html"
