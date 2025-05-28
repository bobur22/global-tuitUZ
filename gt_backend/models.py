from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .validators import validateFullNname
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# News model to store articles or announcements
class News(models.Model):
    n_header = models.CharField(max_length=120, verbose_name=_("news header"), default="header",
                                help_text=_("Please enter the header of the news !"))
    n_paragraph = RichTextField(verbose_name=_("news paragraph"), help_text=_("Please enter the paragraph of the news !"), default="paragraph")
    n_date = models.DateField(default=timezone.now, verbose_name=_("news date"),
                              help_text=_("Please enter the date of the news !."))
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    n_view_counter = models.PositiveIntegerField(default=0, verbose_name=_("news view counter"), help_text=_("This is newses view counter don't change it!"))
    n_news_img = models.ImageField(upload_to='news/', verbose_name=_("news image"),
                                   help_text=_("Please upload your image !"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.n_header)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.n_header

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")


# Contact model to store messages from users
class Contact(models.Model):
    f_name = models.CharField(max_length=50, verbose_name=_("full name"),
                              help_text=_("Please, fill your full name."), validators=[validateFullNname])
    email = models.EmailField(verbose_name=_("email"),
                              help_text=_("Please, fill your email."))
    subject = models.CharField(null=True, blank=True, max_length=50, verbose_name=_("subject"),
                               help_text=_("Please, fill the subject."))
    message = models.TextField(null=True, blank=True, verbose_name=_("message"),
                               help_text=_("Please, fill the message."))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.f_name

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


# Infrastructure model to store content about infrastructure
class Infrastructure(models.Model):
    inf_img = models.ImageField(upload_to='infrostructure/', verbose_name=_("infrostructure image"),
                                help_text=_("Please upload your image !"))
    inf_header = models.CharField(max_length=100, verbose_name=_("infrostructure header"),
                                  help_text=_("Please, enter the header."), default="header")
    inf_paragraph = RichTextField(verbose_name=_("infrostructure paragraph"),
                                   help_text=_("Please, enter the paragraph."), default="paragraph")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.inf_header

    class Meta:
        verbose_name = _("Infrastructure")
        verbose_name_plural = _("Infrastructures")


# Model for foreign partner universities
class partnerUniversity(models.Model):
    nation = models.CharField(max_length=50, verbose_name=_("nation"),
                              help_text=_("Please enter the nation of the university."))
    universityName = models.CharField(max_length=255, verbose_name=_("university name"), help_text=_("Please enter the name of the university."))
    universityLink = models.CharField(max_length=255, verbose_name=_("university link"), help_text=_("Please enter the link of the university."), default="")
    universityDate = models.DateField(verbose_name=_("university date"), help_text=_("Please enter the date of the university."))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.nation

    class Meta:
        verbose_name = _("Partner University")
        verbose_name_plural = _("Partner Universities")


# Telegram bot config model
class TelegramData(models.Model):
    chat_id = models.IntegerField(verbose_name=_("Telegram ID"), help_text=_("Please enter the Telegram ID."))
    bot_token = models.CharField(max_length=46, verbose_name=_("Telegram Bot"), help_text=_("Please enter the Telegram Bot token."))

    def __str__(self):
        return f"{self.chat_id}"

    class Meta:
        verbose_name = _("TelegramData")
        verbose_name_plural = _("TelegramData")


# Admission deadline model for semesters
class admissionDeadline(models.Model):
    semesterName = models.CharField(max_length=50, verbose_name=_("semester name"),
                                    help_text=_("Please enter the semester name."), default="semester dealine")
    semesterDate = models.DateField(verbose_name=_("semester date"),
                                    help_text=_("Please enter the semester date."))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.semesterName

    class Meta:
        verbose_name = _("Admission Deadline")
        verbose_name_plural = _("Admission Deadlines")


# Model for academic programs (Bachelor, Master, PhD, etc.)
class AcademicProgram(models.Model):

    class StudyType(models.TextChoices):
        DOCTORAL = 'doctoral', _('Doctoral')
        UNDERGRADUATE = 'undergraduate', _('Undergraduate')
        GRADUATE = 'graduate', _('Graduate')
        PROGRAM = 'program', _('Program')
        CERTIFICATION = 'certification', _('Certification')

    class ColorType(models.TextChoices):
        DOCTORAL = 'doctoral', _('doctoral')
        UNDERGRADUATE = 'undergraduate', _('undergraduate')
        GRADUATE = 'graduate', _('graduate')
        PROGRAM = 'program', _('program')
        CERTIFICATION = 'certification', _('certification')

    typeStudy = models.CharField(max_length=15, choices=StudyType.choices, default=StudyType.GRADUATE, verbose_name=_("Type of Study"), help_text=_("Please choose the type of study."))
    nameEducation = models.CharField(max_length=40, verbose_name=_("Education Name"), help_text=_("Please enter the name of the education."), default="nameEducation")
    detailEducation = models.CharField(max_length=80, verbose_name=_("Education Detail"), help_text=_("Please enter the detail of the education."), default="detailEducation")
    duration = models.CharField(max_length=20, verbose_name=_("Duration"), help_text=_("Please enter the duration of the education."), default="duration")
    certification = models.CharField(max_length=30, verbose_name=_("Certification"), help_text=_("Please enter the certification of the education."), default="certification")
    startPeriod = models.CharField(max_length=30, verbose_name=_("Start of Period"), help_text=_("Please enter the start period of the education."), default="startPeriod")
    link = models.FileField(upload_to='academicProgram/', verbose_name=_("Academic Program's file"), default="/", help_text=_("Please enter the link of the academic program."))

    iconType = models.CharField(max_length=40, verbose_name=_("icon bi"), default="bi-bounding-box-circles", help_text=_("Please choose the type of icon bi bi"))
    colorType = models.CharField(max_length=15, choices=ColorType.choices, default=ColorType.PROGRAM, verbose_name=_("Color Type"), help_text=_("Please choose the type of color."), blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.nameEducation

    class Meta:
        verbose_name = _("Academic Program")
        verbose_name_plural = _("Academic Programs")
