from django.urls import path
from .views import HomeView, AboutView, ServicesView, SolutionsView, SupportView, CareersView, ContactView, contact_success_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='cyber_protection_services'),
    path('solutions/', SolutionsView.as_view(), name='solutions'),
    path('support/', SupportView.as_view(), name='support'),
    path('careers/', CareersView.as_view(), name='careers'),
    path('contact/', ContactView, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
]