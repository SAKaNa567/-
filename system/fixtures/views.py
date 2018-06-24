from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
# Create your views here.
from .models import Goods
from django.contrib.auth.models import User
from fixtures.models import Category
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
            return redirect('/fixtures/list')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})


@login_required
def list(request):
    try:
        fixtures_list = Goods.objects.all()
        paginator = Paginator(fixtures_list,10)
        # show 10 fixtures per page
        page = request.GET.get('page')
        fixtures = paginator.get_page(page)
    except Goods.DoesNotExist:
        raise Http404("Fixtures does not exist")
    else:
        return render(request,
                      'choose.html',
                      {'fixtures_list':fixtures_list,
                       'fixtures':fixtures}
                      )

@login_required
def home(request):
    return render(request,'home.html')

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
        return HttpResponseRedirect(reverse('fixtures:list'))

@login_required
def back(request,fixtures_id):#other people can not return!!!
    try:
        fixtures = Goods.objects.get(pk=fixtures_id)
    except Goods.DoesNotExist:
        raise Http404("Goods does not exist")
    else:
        fixtures.user = None
        fixtures.status = False
        fixtures.pub_date = None
        fixtures.save()
        return HttpResponseRedirect(reverse('fixtures:list'))

@login_required
def comment(request,fixtures_id):
    try:
        fixtures = Goods.objects.get(pk=fixtures_id)
    except Goods.DoesNotExist:
        raise Http404("Goods does not exist")
    else:
        fixtures.comment = request.POST['comment']
        fixtures.save()
        return render(request,
                      'comment.html',
                      {'fixtures_comment':fixtures.comment}
                      )

@login_required
def category_list(request):
    if "category" in request.GET: # get Category by QueryParameter
        category = request.GET.get("category")
    else:                       # No queryParameter
        try:
            category_list=Category.objects.all()
        except Category.DoesNotExist:
            raise Http404("Category does not exist")
        else:
            return render(request,
                          'category.html',
                          {"category_list":category_list}
                          )
    try:
        specifiedlists = Category.objects.get(name=category).goods_set.all()
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    else:
        return render(request,
                      'category.html',
                      {"specifiedlists":specifiedlists}
                      )

