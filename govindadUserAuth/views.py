from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
# Create your views here.
def loginPage(request):
    if request.method == "POST":
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')
        user = authenticate (username = get_username, password = get_password)
        if user is not None:
            login(request, user)
            messages.success(request,  "Successfull Login" )
            return redirect('govindadDash:dashboardPage')
        else:
            messages.error(request,  "Incorect Username or Password" )
            return redirect('govindadUserAuth:loginPage')


    else:
        template_name = 'govindadUserAuth/loginPage.html'
        context = {

        }

        return render (request, template_name, context)


def logoutPage(request):
    logout(request)
    messages.success(request,  "Successfull Logout" )
    return redirect('govindadUserAuth:loginPage')