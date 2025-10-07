# app/views.py
from django.shortcuts import render, redirect
from material.models import Material, Department, Course, PastQuestion, TimeTable, DepartmentRepresentative
from user_account.models import User
from .models import Newsletter, Partner
from django.contrib import messages
from .utils import search_in_model
from django.utils import timezone
from django.core.paginator import Paginator
from datetime import datetime

# Import the new models from material app
from material.models import Bulletin, AcademicEvent
# Add this import line with your other imports
from material.models import Announcement

def index(request):
    context = {}
    context['partners'] = Partner.objects.all()
    
    # Add ongoing preview data to homepage
    context['current_semester'] = get_current_semester()
    context['current_week'] = get_current_week()
    
    # Get ongoing events for preview (2 events max)
    current_date = timezone.now().date()
    ongoing_events = AcademicEvent.objects.filter(
        start_date__lte=current_date,
        end_date__gte=current_date
    ).order_by('start_date')[:2]
    
    context['ongoing_events_preview'] = ongoing_events
      # Get recent bulletins for homepage preview
    context['bulletins'] = Bulletin.objects.filter(is_active=True).order_by('-created_at')[:3]
    
    # ADD: Get recent announcements for homepage preview (3 most recent)
    context['announcements'] = Announcement.objects.filter(is_active=True).order_by('-created_at')[:3]
    
    return render(request, 'app/index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
    
def terms_condition(request):
    return render(request, 'terms_condition.html')

def representatives(request):
    reps = DepartmentRepresentative.objects.all()
    return render(request, 'reps.html', {'reps': reps})

def register_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if Newsletter.objects.filter(email=email).exists():
            messages.info(request, "This Email is already registered to our newsletter.")
            return redirect("/")
        n = Newsletter(email=email)
        n.save()
    return render(request, "app/email.html")

def advance_search(request):
    if request.method != 'POST':
        return redirect('/')
    q = request.POST.get('q')
    pq = request.POST.get('pq', None)
    m = request.POST.get('m', None)
    c = request.POST.get('c', None)
    tb = request.POST.get('tb', None)
    bg = request.POST.get('bg', None)
    past_questions = search_in_model(PastQuestion, q) if pq else None
    materials = search_in_model(Material, q) if m else None
    courses = search_in_model(Course, q) if c else None
    time_tables = search_in_model(TimeTable, q) if tb else None
    
    models = (past_questions, materials, courses, time_tables)
    context = {'models_name': [], 'empty_models': [], 'models': [], 'q': q, 'number_of_results': 0}
    
    for model in models:
        if model != None:
            context['models_name'] += [model.model._meta.object_name]
            if not model:
                context['empty_models'] += [model.model._meta.object_name]
            else:
                context['models'] += [{'object_name':model.model._meta.object_name, 'objects': model}]
                context['number_of_results'] += model.count()
    return render(request, 'advance_search.html', context)

def bulletin_page(request):
    # Get all active bulletins, newest first
    bulletins_list = Bulletin.objects.filter(is_active=True).order_by('-created_at')
    
    # Add pagination (10 per page)
    paginator = Paginator(bulletins_list, 10)
    page_number = request.GET.get('page')
    bulletins = paginator.get_page(page_number)
    
    context = {
        'bulletins': bulletins,
        'page_title': 'Campus Bulletin'
    }
    return render(request, 'app/bulletin.html', context)

def academic_calendar_page(request):
    # Get all upcoming events, ordered by date
    upcoming_events = AcademicEvent.objects.filter(
        start_date__gte=timezone.now().date()
    ).order_by('start_date')
    
    # Get past events (last 30 days) for reference
    past_events = AcademicEvent.objects.filter(
        start_date__lt=timezone.now().date(),
        start_date__gte=timezone.now().date() - timezone.timedelta(days=30)
    ).order_by('-start_date')
    
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'page_title': 'Academic Calendar'
    }
    return render(request, 'app/academic_calendar.html', context)

def ongoing_view(request):
    # Get current academic events
    current_date = timezone.now().date()
    
    # Get ongoing events (events that are currently happening)
    ongoing_events = AcademicEvent.objects.filter(
        start_date__lte=current_date,
        end_date__gte=current_date
    ).order_by('start_date')
    
    context = {
        'ongoing_events': ongoing_events,
        'current_semester': get_current_semester(),
        'current_week': get_current_week(),
        'page_title': 'Currently Ongoing'
    }
    return render(request, 'app/ongoing.html', context)

def get_current_semester():
    # Implement your semester logic
    today = datetime.now()
    # Example logic - adjust based on your academic calendar
    if 1 <= today.month <= 5:
        return "Spring Semester"
    elif 6 <= today.month <= 8:
        return "Summer Semester"
    else:
        return "Fall Semester"

def get_current_week():
    # Implement week calculation logic
    return "Week 5"  # Example - you can make this dynamic

def announcements_page(request):
    # Get all active announcements, newest first
    announcements_list = Announcement.objects.filter(is_active=True).order_by('-created_at')
    
    # Add pagination (10 per page)
    paginator = Paginator(announcements_list, 10)
    page_number = request.GET.get('page')
    announcements = paginator.get_page(page_number)
    
    context = {
        'announcements': announcements,
        'page_title': 'Announcements'
    }
    return render(request, 'app/announcements.html', context)