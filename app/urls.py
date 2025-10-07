# app/urls.py
"""from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('advance/search/', views.advance_search, name='advance_search'),
    path('about/', views.about, name='about'),
    path('representatives/', views.representatives, name='representatives'),
    path('contact/', views.contact, name='contact'),
    path('terms_condition/', views.terms_condition, name='terms_condition'),
    path("register_newsletter/", views.register_newsletter, name="register_newsletter"),

]

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('advance/search/', views.advance_search, name='advance_search'),
    path('about/', views.about, name='about'),
    path('representatives/', views.representatives, name='representatives'),
    path('contact/', views.contact, name='contact'),
    path('terms_condition/', views.terms_condition, name='terms_condition'),
    path("register_newsletter/", views.register_newsletter, name="register_newsletter"),
    
    # NEW URLs - Add these lines
    path('bulletin/', views.bulletin_page, name='bulletin'),
    path('academic-calendar/', views.academic_calendar_page, name='academic_calendar'),
]

# app/urls.py
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('advance/search/', views.advance_search, name='advance_search'),
    path('about/', views.about, name='about'),
    # ... your existing URLs ...
    
    # ADD THESE TWO LINES:
    path('bulletin/', views.bulletin_page, name='bulletin'),
    path('academic-calendar/', views.academic_calendar_page, name='academic_calendar'),
] """

# app/urls.py
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('advance/search/', views.advance_search, name='advance_search'),
    path('about/', views.about, name='about'),
    path('representatives/', views.representatives, name='representatives'),
    path('contact/', views.contact, name='contact'),
    path('terms_condition/', views.terms_condition, name='terms_condition'),
    path('register_newsletter/', views.register_newsletter, name='register_newsletter'),
    path('bulletin/', views.bulletin_page, name='bulletin'),
    path('academic-calendar/', views.academic_calendar_page, name='academic_calendar'),
    path('ongoing/', views.ongoing_view, name='ongoing'),
    path('announcements/', views.announcements_page, name='announcements'),
    
]
