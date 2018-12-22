from django.conf.urls import url,include
from . import views

urlpatterns=[
url(r'^$',views.index,name='Index'),
url(r'^profile/$', views.profile, name='profile'),

]