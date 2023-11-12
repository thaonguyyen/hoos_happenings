from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import EventSubmissionForm
from .models import EventSubmission
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def user_map(request):
    return render(request, "user_map.html")

def admin_map(request):
    return render(request, "admin_map.html")

def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
            return redirect('home_admin')
    return redirect('home_user')

def is_admin(user):
    return user.is_superuser

def admin_view(request):
    return render(request, 'home_admin.html')

def user_view(request):
    return render(request, 'home_user.html')

def submit_event(request):
    if request.method == 'POST':
        form = EventSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            form.save()
            return redirect('submit_event')  # Redirect to a success page or wherever appropriate
    else:
        form = EventSubmissionForm()
    return render(request, 'submit.html', {'form': form})

def review_events(request):
    events = EventSubmission.objects.filter(approved=False)
    return render(request, 'review.html', {'events': events})

def approve_event(request, event_id):
    event = EventSubmission.objects.get(id=event_id)
    event.approved = True
    event.save()
    return redirect('review_event')

def user_event_listings(request):
    events = EventSubmission.objects.filter(approved=True)
    return render(request, 'user_listings.html', {'events': events})

def admin_event_listings(request):
    events = EventSubmission.objects.filter(approved=True)
    return render(request, 'admin_listings.html', {'events': events})