from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users
from AppTwo import forms
# Create your views here.

def index(request):
    return render(request, 'AppTwo/index.html')

def help(request):
    help_dict = {'help_temp':"Help Page"}
    return render(request, 'AppTwo/help.html', context=help_dict)

def users(request):
    # this was for displaying all users
    #
    # users_list = Users.objects.all()
    # users_dict = {'users_list':users_list}
    # return render(request, 'AppTwo/users.html', context=users_dict)
    form = forms.user_sign_up()
    if request.method == 'POST':
        form = forms.user_sign_up(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error! Form Invalid")

    return render(request, 'AppTwo/users.html', context={'form':form})
