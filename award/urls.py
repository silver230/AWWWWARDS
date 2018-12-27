from django.conf.urls import url,include
from . import views

urlpatterns=[
url(r'^$',views.index,name='Index'),
url(r'^signup/$', views.signup, name='signup'),
url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]
