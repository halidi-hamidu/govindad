from django.shortcuts import render

# Create your views here.
def dashboardPage(request):
    template_name = 'dashboardPage/dashboardPage.html'
    context = {

    }

    return render (request, template_name , context)