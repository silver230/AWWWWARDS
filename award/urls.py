from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
url(r'^$',views.index,name='index'),
url(r'^sign/$',views.signup, name='signup'),
url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
url(r'auth/',include('registration.backends.simple.urls')),
url(r'^post/(\d+)', views.post, name='post'),
url(r'^new/post$', views.new_post, name='new-post'),
url(r'^search/$', views.search_results, name = 'search_results'),
url(r'^rating/(?P<project_id>\d+)$', views.rating, name = 'rating'),
# url(r'^profile/',views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
