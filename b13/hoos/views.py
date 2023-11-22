import googlemaps
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import EventSubmissionForm
from .models import EventSubmission
from django.http import HttpResponseRedirect
from django.urls import reverse

def check_authenticated(request):
    pass

def is_admin(user):
    return user.is_authenticated and user.is_superuser

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    return render(request, "home.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def welcome(request):
    if not request.user.is_authenticated:
        return redirect('home')
    user_type = 'an Admin' if is_admin(request.user) else 'a User'
    return render(request, 'welcome.html', context={'user_type': user_type})

def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
            return redirect('home_admin')
    return redirect('home_user')

def submit_event(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = EventSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            gmaps = googlemaps.Client(key='AIzaSyBFnP0Yo4IN8h8Q1U4SjPKdJH9X1QeiKMc')
            geocode_result = gmaps.geocode(submission.location)
            if geocode_result:
                submission.latitude = geocode_result[0]['geometry']['location']['lat']
                submission.longitude = geocode_result[0]['geometry']['location']['lng']
            submission.user = request.user
            form.save()
            context = {'submission': submission, 'valid_location': bool(geocode_result)}
            return render(request, 'submit_confirmation.html', context=context)
    else:
        form = EventSubmissionForm()
    return render(request, 'submit.html', {'form': form})

def review_events(request):
    if not request.user.is_authenticated:
        return redirect('home')
    events = EventSubmission.objects.filter(approved=False)
    return render(request, 'review.html', {'events': events})

def approve_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('home')
    event = EventSubmission.objects.get(id=event_id)
    event.approved = True
    event.save()
    return redirect('review_events')

def reject_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('home')
    event = EventSubmission.objects.get(id=event_id)
    event.delete()
    return redirect('review_events')

def listings(request):
    if not request.user.is_authenticated:
        return redirect('home')
    events = EventSubmission.objects.filter(approved=True)
    return render(request, 'listings.html', context={'events': events})

def map_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    events = EventSubmission.objects.filter(approved=True)
    return render(request, "map.html", context={'events': events})
