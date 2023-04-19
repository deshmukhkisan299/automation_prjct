from django.shortcuts import render,HttpResponseRedirect
from .form import UserForm
# Create your views here.
def sign_up(r):
    if r.method == "POST":
        form = UserForm(r.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/')
    return render(r, 'home/signup.html', {'form': UserForm})