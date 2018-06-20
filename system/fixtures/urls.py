from django.contrib import admin
from django.urls import path

from fixtures import views as fixtures_views
app_name = 'fixtures'
urlpatterns = [
    path('home/',fixtures_views.home,name='home'),
    path('<int:fixtures_id>/choose/',fixtures_views.choose,name='choose')

]
