from django.shortcuts import render
from registration.forms import CustomUserCreationForm


def registration_view(request):
    form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'registration.html', context)
