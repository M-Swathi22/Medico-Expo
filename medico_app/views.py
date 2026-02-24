from django.shortcuts import render, redirect
from django.contrib import messages   # ADD THIS
from .forms import RegistrationForm

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