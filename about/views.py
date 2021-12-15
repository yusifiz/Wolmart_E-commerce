from django.shortcuts import render
from .models import Leaders
# Create your views here.

def about(request):
    leaders = Leaders.objects.all()
    context = { 'leaders' : leaders}
    return render(request, "about-us.html", context)