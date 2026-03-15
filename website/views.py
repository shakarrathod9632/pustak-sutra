from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """Home page view"""
    context = {
        'page_title': 'Pustak Sutra - Quality Education for Young Minds',
        'meta_description': 'Pustak Sutram provides quality education for students from LKG to Class 8. Expert tutors, interactive learning, and activity-based teaching.',
        'active_page': 'home'
    }
    return render(request, 'pages/home.html', context)  # ✅ Added 'pages/' folder

def about(request):
    """About us page"""
    context = {
        'page_title': 'About Us - Pustak Sutra',
        'meta_description': 'Learn about Pustak Sutram mission, vision, and our approach to quality education for young minds.',
        'active_page': 'about'
    }
    return render(request, 'pages/about.html', context)  # ✅ Added 'pages/' folder

def courses(request):
    return render(request, 'pages/courses.html')  # ✅ Added 'pages/' folder


def english(request):
    return render(request, 'pages/english.html')  # ✅ Added 'pages/' folder

def mathematics(request):
    return render(request, 'pages/mathematics.html')  # ✅ Added 'pages/' folder

def logical_thinking(request):
    return render(request, 'pages/logical_thinking.html')  # ✅ Added 'pages/' folder


def contact(request):
    """Contact page"""
    if request.method == 'POST':
        # Here you would handle form submission (send email, save to database, etc.)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Add your form processing logic here
        success_message = "Thank you for contacting us! We'll get back to you soon."
        context = {
            'page_title': 'Contact Us - Pustak Sutra',
            'meta_description': 'Get in touch with Pustak Sutram. Visit us, call, or email for any queries about our courses.',
            'active_page': 'contact',
            'success_message': success_message
        }
        return render(request, 'pages/contact.html', context)  # ✅ Added 'pages/' folder
    
    context = {
        'page_title': 'Contact Us - Pustak Sutra',
        'meta_description': 'Get in touch with Pustak Sutram. Visit us, call, or email for any queries about our courses.',
        'active_page': 'contact'
    }
    return render(request, 'pages/contact.html', context)  # ✅ Added 'pages/' folder

def enroll(request):
    """Enrollment page"""
    courses_data = [
        {'id': 1, 'name': 'Mathematics', 'price': 4999},
        {'id': 2, 'name': 'Science', 'price': 5599},
        {'id': 3, 'name': 'English', 'price': 4499},
    ]
    
    if request.method == 'POST':
        # Handle enrollment form submission
        success_message = "Enrollment request submitted successfully! We'll contact you soon."
        context = {
            'page_title': 'Enroll Now - Pustak Sutra',
            'meta_description': 'Enroll your child in our quality education programs. Choose from Mathematics, Science, and English courses.',
            'active_page': 'enroll',
            'courses': courses_data,
            'success_message': success_message
        }
        return render(request, 'pages/enroll.html', context)  # ✅ Added 'pages/' folder
    
    context = {
        'page_title': 'Enroll Now - Pustak Sutra',
        'meta_description': 'Enroll your child in our quality education programs. Choose from Mathematics, Science, and English courses.',
        'active_page': 'enroll',
        'courses': courses_data
    }
    return render(request, 'pages/enroll.html', context)  # ✅ Added 'pages/' folder


def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')  # ✅ Added 'pages/' folder

def terms_and_conditions(request):
    return render(request, 'pages/terms_and_conditions.html')  # ✅ Added 'pages/' folder

def blog(request):
    return render(request, 'pages/blog.html')  # ✅ Added 'pages/' folder

def faq(request):
    return render(request, 'pages/faq.html')  # ✅ Added 'pages/' folder