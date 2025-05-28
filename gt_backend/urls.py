from django.urls import path
from .views import (
    Index, About, Academics, Admissions, Falco, Campus, ContactView,
    NewsList, NewsDetail, Privacy, InfrastructureList,
    PartnerPage, StudentLife, TermsServices
)

# URL patterns mapping each path to its corresponding view function
urlpatterns = [
    path('', Index, name='index'),  # Home page

    # Static informational pages
    path('about/', About, name='about'),
    path('academics/', Academics, name='academics'),
    path('admissions/', Admissions, name='admissions'),
    path('community/falco/', Falco, name='falco'),  # Community or Falco section
    path('campus/', Campus, name='campus'),
    path('contact/', ContactView, name='contact'),

    # News section
    path('news/', NewsList, name='news'),  # Shows list of news items
    path('news_detail/<slug:slug>/', NewsDetail, name='news_detail'),  # Shows a specific news item by slug

    # Legal and policy pages
    path('privacy/', Privacy, name='privacy'),
    path('terms_services/', TermsServices, name='terms_services'),

    # Miscellaneous content
    path('starter_page/', InfrastructureList, name='starter_page'),  # Infrastructure or project starter
    path('partnerUniversities/', PartnerPage, name='partner_page'),  # List of partner universities
    path('student_life/', StudentLife, name='student_life'),  # Student life section
]
