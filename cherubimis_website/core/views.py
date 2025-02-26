# django_app/core/views.py

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import InquiryForm
from django.core.mail import EmailMessage

class HomeView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ServicesView(TemplateView):
    template_name = "services.html"

class SolutionsView(TemplateView):
    template_name = "solutions.html"

class SupportView(TemplateView):
    template_name = "support.html"

class CareersView(TemplateView):
    template_name = "careers.html"

# def ContactView(request):
#     if request.method == 'POST':
#         form = InquiryForm(request.POST)
#         if form.is_valid():
#             inquiry_obj = form.save()

#             # Build the email subject and body
#             subject = "New Inquiry Received"
#             message = (
#                 f"New inquiry from {inquiry_obj.first_name} {inquiry_obj.last_name}\n"
#                 f"Email: {inquiry_obj.business_email}\n"
#                 f"Company: {inquiry_obj.company_name}\n\n"
#                 f"Message:\n{inquiry_obj.inquiry}"
#             )

#             # Create the EmailMessage
#             email = EmailMessage(
#                 subject=subject,
#                 body=message,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=[settings.ADMIN_EMAIL],
#                 reply_to=[inquiry_obj.business_email],
#             )

#             try:
#                 email.send(fail_silently=False)
#             except Exception as e:
#                 print(f"Failed to send email. Error: {e}")
#                 raise

#             # For debugging/logging
#             print(f"Subject: {subject}\n{message}")

#             return redirect('contact_success')
#         else:
#             return render(request, 'contact.html', {'form': form})
#     else:
#         form = InquiryForm()
#     return render(request, 'contact.html', {'form': form})

def ContactView(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
        else:
            return render(request, 'contact.html', {'form': form})
    else:
        form = InquiryForm()
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')
