from django.contrib import admin
from django.urls import path

from fixtures import views as fixtures_views
app_name = 'fixtures'
urlpatterns = [
    path('list/',fixtures_views.list,name='list'),
    path('<int:fixtures_id>/borrow/',fixtures_views.borrow,name='borrow'),
    path('<int:fixtures_id>/back',fixtures_views.back,name='back'),
    path('<int:fixtures_id>/comment',fixtures_views.comment,name='comment'),
]