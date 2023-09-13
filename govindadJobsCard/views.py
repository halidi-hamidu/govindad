from django.shortcuts import render

# Create your views here.
def newJobCardPage(request):
    template_name = 'govindadJobsCard/newJobCardPage.html'
    context ={

    }

    return render (request, template_name, context)