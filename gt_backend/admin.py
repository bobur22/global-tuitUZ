from django.contrib import admin
from .models import (
    News, Contact, Infrastructure, partnerUniversity,
    TelegramData, admissionDeadline, AcademicProgram
)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("n_header", "n_date", "n_view_counter", "created_at")
    search_fields = ("n_header",)
    prepopulated_fields = {"slug": ("n_header",)}
    list_filter = ("n_date", "created_at")
    ordering = ("-n_date",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("f_name", "email", "subject", "created_at")
    search_fields = ("f_name", "email", "subject")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)


@admin.register(Infrastructure)
class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ("inf_header", "created_at")
    search_fields = ("inf_header",)
    ordering = ("-created_at",)


@admin.register(partnerUniversity)
class PartnerUniversityAdmin(admin.ModelAdmin):
    list_display = ("universityName", "nation", "universityDate")
    search_fields = ("universityName", "nation")
    list_filter = ("nation",)
    ordering = ("-universityDate",)


@admin.register(TelegramData)
class TelegramDataAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "bot_token")
    search_fields = ("chat_id",)


@admin.register(admissionDeadline)
class AdmissionDeadlineAdmin(admin.ModelAdmin):
    list_display = ("semesterName", "semesterDate", "created_at")
    search_fields = ("semesterName",)
    ordering = ("-semesterDate",)


@admin.register(AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = ("nameEducation", "typeStudy", "duration", "startPeriod")
    search_fields = ("nameEducation", "typeStudy")
    list_filter = ("typeStudy", "colorType")
    ordering = ("nameEducation",)
