from django.shortcuts import HttpResponse

# Create your views here.
def orm_tutorial_view(request):
    return HttpResponse("ORM TUTORIAL: Use the shell for this tutorial!")
