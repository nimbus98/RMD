from django.shortcuts import render, redirect
from .models import Victim
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def victim_list(request):
    if request.method=="POST":
        nm = request.POST.get('name')
        victims = Victim.objects.filter(name=nm).order_by('name')
        return render(request, 'managing/victim_list.html', {'victims':victims})
    else:
        victims = Victim.objects.all().order_by('name')
        return render(request, 'managing/victim_list.html', {'victims':victims})

def app_victimlist(request):
    strng = ','.join([str(i) for i in Victim.objects.all().order_by('name').defer('thumb','date')])
    return HttpResponse('[' + strng + ']')

@login_required(login_url="/accounts/login/")
def victim_new(request):
    if request.method == 'POST':
        form = forms.VictimForm(request.POST, request.FILES)
        if form.is_valid():
            s_instance = form.save(commit=False)
            s_instance.admitter = request.user
            s_instance.save()
            return redirect('managing:list')
    else:
        form = forms.VictimForm
    return render(request, 'managing/victim_enter.html', {'form':form})