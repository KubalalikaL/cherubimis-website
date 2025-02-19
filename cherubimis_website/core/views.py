# django_app/core/views.py

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import InquiryForm
import logging

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

def ContactView(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry_obj = form.save()
            # Email admin
            subject = "New Inquiry Received"
            message = (
                f"New inquiry from {inquiry_obj.first_name} {inquiry_obj.last_name}\n"
                f"Email: {inquiry_obj.business_email}\n"
                f"Company: {inquiry_obj.company_name}\n\n"
                f"Message:\n{inquiry_obj.inquiry}"
            )
            # send_mail(
            #     subject,
            #     message,
            #     settings.DEFAULT_FROM_EMAIL,
            #     [settings.ADMIN_EMAIL],
            #     fail_silently=False,
            # )
            logging.info(f"Email: {subject}\n{message}")
            print(f"Subject: {subject}\n{message}")
            return redirect('contact_success')
    else:
        form = InquiryForm()
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')
