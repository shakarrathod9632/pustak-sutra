from django.urls import path
from . import views

app_name = 'website'  # This creates a namespace

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('english/', views.english, name='english'),
    path('mathematics/', views.mathematics, name='mathematics'),
    path('logical_thinking/', views.logical_thinking, name='logical_thinking'),
    # path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('enroll/', views.enroll, name='enroll'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('blog/', views.blog, name='blog'),
    path('faq/', views.faq, name='faq'),

]