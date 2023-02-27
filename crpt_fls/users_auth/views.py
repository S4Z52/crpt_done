from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import FileUp
from .forms import FileForm

def home(request):
    return render(request,"home.html")

class PageHome(CreateView):
    model = FileUp
    form_class = FileForm
    template_name = 'homes.html'
    success_url = reverse_lazy('list_file')

class ViewFile(ListView):
    model = FileUp
    template_name = 'viewer.html'