from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
# Create your views here.
def index(request):
  date = dt.date.today()

  return render(request,'index.html',{"date":date})

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    user = User.objects.get(username=request.user)
    return render(request, 'profile/profile.html', {'user': current_user, "profile": profile})
