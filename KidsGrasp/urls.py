from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^English/$',views.english,name='english'),
    url(r'^Hindi/$',views.hindi,name='hindi'),
    url(r'^Maths/$',views.maths,name='maths'),
    url(r'^Calculator/$',views.calculator,name='calculator'),
]