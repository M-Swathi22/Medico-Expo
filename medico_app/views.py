from django.shortcuts import render, redirect
from django.contrib import messages   # ADD THIS
from .forms import RegistrationForm
from .models import Registration 

def home(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration submitted successfully!")  # ADD THIS
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'index.html', {'form': form})

def view_registrations(request):
    registrations = Registration.objects.all().order_by('-created_at')
    return render(request, 'view_registrations.html', {
        'registrations': registrations
    })

