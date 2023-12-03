import googlemaps
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .forms import EventSubmissionForm
from .models import EventSubmission
from .models import Tag
from django.http import HttpResponseRedirect
from django.urls import reverse

def check_authenticated(request):
    pass

def is_admin(user):
    return user.is_authenticated and user.is_superuser

def assign_approval_status(request, event_id, approval_status):
    event = get_object_or_404(EventSubmission, id=event_id)
    redirect_url = request.META.get('HTTP_REFERER', reverse('home'))
    event.approval_status = approval_status
    event.save()
    return redirect(redirect_url)

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
    if not is_admin(request.user):
        return redirect('home')
    events = EventSubmission.objects.filter(approval_status='pending')
    return render(request, 'review.html', {'events': events})

def approve_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('home')
    if not is_admin(request.user):
        return redirect('home')
    return assign_approval_status(request, event_id, 'approved')

def reject_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('home')
    if not is_admin(request.user):
        return redirect('home')
    return assign_approval_status(request, event_id, 'rejected')

def delete_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('home')
    
    event = get_object_or_404(EventSubmission, id=event_id)
    redirect_url = request.META.get('HTTP_REFERER', reverse('home'))
    event.delete()
    return redirect(redirect_url)

def listings(request):
    if not request.user.is_authenticated:
        return redirect('home')
    events = EventSubmission.objects.filter(approval_status='approved').order_by('date_time')
    show_btn = False
    name = ""
    form = EventSubmissionForm()
    tag_filter = request.GET.getlist('tags')
    if tag_filter:
        for tag in tag_filter:
            events = events.filter(tags=tag).order_by('date_time')
        form = EventSubmissionForm(initial={'tags': tag_filter})
        show_btn = True
    name_filter = request.GET.get('name')
    if name_filter:
        events = events.filter(name__icontains=name_filter).order_by('date_time')
        show_btn = True
        name = name_filter
    date_filter = [request.GET.get("after"), request.GET.get("before")]
    if date_filter[0]:
        events = events.filter(date_time__gt=date_filter[0]).order_by('date_time')
        show_btn = True
    if date_filter[1]:
        events = events.filter(date_time__lt=date_filter[1]).order_by('date_time')
        show_btn = True
    return render(request, 'listings.html', context={'events': events, 'form': form, 'show': show_btn, 'name': name, 'tags': tag_filter, 'date': date_filter})

def map_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    events = EventSubmission.objects.filter(approval_status='approved')
    show_btn = False
    name = ""
    form = EventSubmissionForm()
    tag_filter = request.GET.getlist('tags')
    if tag_filter:
        for tag in tag_filter:
            events = events.filter(tags=tag)
        form = EventSubmissionForm(initial={'tags': tag_filter})
        show_btn = True
    name_filter = request.GET.get('name')
    if name_filter:
        events = events.filter(name__icontains=name_filter)
        show_btn = True
        name = name_filter
    date_filter = [request.GET.get("after"), request.GET.get("before")]
    if date_filter[0]:
        events = events.filter(date_time__gt=date_filter[0])
        show_btn = True
    if date_filter[1]:
        events = events.filter(date_time__lt=date_filter[1])
        show_btn = True
    return render(request, "map.html", context={'events': events, 'form': form, 'show': show_btn, 'name': name, 'tags': tag_filter, 'date': date_filter})

def my_events(request):
    if not request.user.is_authenticated:
        return redirect('home')
    events = EventSubmission.objects.filter(user=request.user)
    return render(request, 'my_events.html', context={'events': events})

def event_details(request, event_id):
    if not request.user.is_authenticated:
        return redirect('home')
    event = get_object_or_404(EventSubmission, id=event_id)
    context = {'event': event, 'long_description': True}
    return render(request, 'event_details.html', context=context)
