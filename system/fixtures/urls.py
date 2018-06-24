from django.contrib import admin
from django.urls import path

from fixtures import views as fixtures_views
app_name = 'fixtures'
urlpatterns = [
    path('',fixtures_views.home,name='home'),
    path('list/',fixtures_views.list,name='list'),
    path('category_list/',fixtures_views.category_list,name='category_list'),
    path('<int:fixtures_id>/borrow/',fixtures_views.borrow,name='borrow'),
    path('<int:fixtures_id>/back',fixtures_views.back,name='back'),
    path('<int:fixtures_id>/comment',fixtures_views.comment,name='comment'),
]