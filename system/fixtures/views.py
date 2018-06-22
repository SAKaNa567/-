from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
from .models import Goods
from django.contrib.auth.models import User
from django.utils import timezone


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
def list(request):
    try:
        fixtures_list = Goods.objects.all()
    except Goods.DoesNotExist:
        raise Http404("Fixtures does not exist")
    else:
        return render(request,
                      'choose.html',
                      {'fixtures_list':fixtures_list}
                      )

@login_required
def home(request):
    return render(request,home.html)

@login_required
def borrow(request,fixtures_id):
    try:
        fixtures = Goods.objects.get(pk=fixtures_id)
    except Goods.DoesNotExist:
        raise Http404("Goods does not exist")
    else:
        fixtures.user = User.objects.get(username=request.user)
        fixtures.status = True
        fixtures.pub_date = timezone.now()
        fixtures.save()
        return render(request,
                      'borrow.html',
                      {'fixtures_name':fixtures}
                      )

@login_required
def back(request,fixtures_id):
    try:
        fixtures = Goods.objects.get(pk=fixtures_id)
    except Goods.DoesNotExist:
        raise Http404("Goods does not exist")
    else:
        fixtures.user = None
        fixtures.status = False
        fixtures.pub_date = None
        fixtures.save()
        return render(request,
                      'back.html',
                      {'fixtures_name':fixtures.goods})
