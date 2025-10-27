# Create your views here.
from django.shortcuts import render, redirect
from .models import Researcher
from .forms import ResearcherForm

def researcher_view(request):
    # Handle form submission
    if request.method == 'POST':
        form = ResearcherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('researcher_view')
    else:
        form = ResearcherForm(request.GET)

    # if request.method == 'GET' <- note this is not needed as we implied it (but only for a normal usage)

    # Retrieve all saved people, let's interrogate the database true ORM:
    researchers = Researcher.objects.all()

    return render(request, 'researchers.html', {'form': form, 'researchers': researchers})
