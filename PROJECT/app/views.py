from django.shortcuts import render
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from app.forms import LogMessageForm
from app.models import LogMessage
from classes.models import UClass
from django.views.generic import ListView

def check(request, name):
    return render(
        request,
        'app/check.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def home(request):
    queryset=LogMessage.objects.order_by("-log_date")[:5]  # :5 limits the results to the five most recent
    querysetUC=UClass.objects.order_by("-log_date")[:5]
    return render(request, "home/index.html", {
        'message_list': queryset.values,
        'classes_list': querysetUC.values,
        'date': datetime.now()
    })

def about(request):
    queryset=LogMessage.objects.order_by("-log_date")[:5]  # :5 limits the results to the five most recent
    return render(request, "about/index.html", {
        'message_list': queryset.values,
        'date': datetime.now()
    })

def contact(request):
    queryset=LogMessage.objects.order_by("-log_date")[:5]  # :5 limits the results to the five most recent
    return render(request, "contact/index.html", {
        'message_list': queryset.values,
        'date': datetime.now()
    })

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("log")
    else:
        queryset=LogMessage.objects.order_by("-log_date")[:5]  # :5 limits the results to the five most recent
        return render(request, "log_message/index.html", {
            "form": form, 
            'message_list': queryset.values,
            'date': datetime.now()
        })