from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
from .models import Goods
# you need this function.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})



@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def choose(request,fixtures_id):
    try:
        fixtures_list = Goods.objects.all()
    except Goods.DoesNotExist:
        raise Http404("Fixtures does not exist")
    else:
        return render(request,
                      'choose.html',
                      {'fixtures_list':fixtures_list}
                      )