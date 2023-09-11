from django.shortcuts import render

# Create your views here.
def loginPage(request):
    template_name = 'userAuth/loginPage.html'
    context = {

    }

    return render (request, template_name, context)