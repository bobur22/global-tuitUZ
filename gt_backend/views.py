from django.shortcuts import render, redirect, get_object_or_404
from .models import News, TelegramData, Contact, partnerUniversity, Infrastructure, admissionDeadline, AcademicProgram
from .forms import ContactForm
import requests
from django.core.paginator import Paginator


# Home page view
def Index(request):
    # Get the 3 most recent news items
    newses = News.objects.all().order_by('-n_date')[:3]
    print(newses)  # Debug print; remove in production
    return render(request, 'index.html', {'newses': newses})


# Static about page
def About(request):
    return render(request, 'about/about.html')


# Academics page showing list of academic programs
def Academics(request):
    academicPrograms = AcademicProgram.objects.all()
    return render(request, 'studentLife/academics.html', {'academicPrograms': academicPrograms})


# Admissions page showing deadlines
def Admissions(request):
    admissions = admissionDeadline.objects.all()
    return render(request, 'about/admissions.html', {"admissions": admissions})


# Alumni or community page
def Falco(request):
    return render(request, 'alumni.html')


# Campus facilities page
def Campus(request):
    return render(request, 'studentLife/campus-facilities.html')


# Contact page view handling form submission and Telegram bot integration
def ContactView(request):
    # Get the last configured Telegram bot data
    telegram_data = TelegramData.objects.last()

    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save contact form data to the database
        contact = Contact.objects.create(
            f_name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Format the message for Telegram
        telegram_text = (
            "📩 <b>New Contact Form Submission</b>\n"
            f"👤 <b>Name:</b> {name}\n"
            f"📧 <b>Email:</b> {email}\n"
            f"📝 <b>Subject:</b> {subject}\n"
            f"💬 <b>Message:</b>\n\t\t\t\t\t\t{message}"
        )

        # Send message to Telegram
        token = telegram_data.bot_token
        chat_id = telegram_data.chat_id
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': telegram_text,
            'parse_mode': 'HTML'
        }
        requests.get(url, params=payload)

        # Optionally delete the contact from DB after sending
        contact.delete()

        return redirect("contact")

    return render(request, 'contact.html')


# News listing page with pagination
def NewsList(request):
    all_news = News.objects.all().order_by('-n_date')
    important_news = all_news[:5]      # Top 5 news (highlighted)
    general_news = all_news[5:]        # The rest for pagination
    paginator = Paginator(general_news, 6)  # Show 6 news per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {"page_obj": page_obj, 'important_news': important_news})


# News detail page by slug (and updates view counter)
def NewsDetail(request, slug):
    news = get_object_or_404(News, slug=slug)
    news.n_view_counter += 1
    news.save(update_fields=['n_view_counter'])
    return render(request, 'news-details.html', {"news": news})


# Privacy policy page
def Privacy(request):
    return render(request, 'privacy.html')


# Infrastructure page showing the last added infrastructure content
def InfrastructureList(request):
    inf = Infrastructure.objects.last()
    print(inf)  # Debug print; remove in production
    return render(request, 'about/international_office.html', {'inf': inf})


# Partner universities page
def PartnerPage(request):
    paginator = partnerUniversity.objects.all().order_by('nation')
    return render(request, 'about/partnersCountry.html', {"page_obj": paginator})


# Student life page
def StudentLife(request):
    return render(request, 'studentLife/students-life.html')


# Terms of service page
def TermsServices(request):
    return render(request, 'terms-of-service.html')


from django.shortcuts import render

# Custom 404 handler
def NF404(request, exception):
    return render(request, '404/404.html', status=404)

