from modeltranslation.translator import register, TranslationOptions
from .models import News, Infrastructure, admissionDeadline, AcademicProgram


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('n_header', 'n_paragraph',)


@register(Infrastructure)
class InfrastructureTranslation(TranslationOptions):
    fields = ('inf_header', 'inf_paragraph',)


@register(admissionDeadline)
class admissionDeadlineTranslation(TranslationOptions):
    fields = ('semesterName',)


@register(AcademicProgram)
class AcademicProgramTranslation(TranslationOptions):
    fields = ( 'nameEducation', 'detailEducation', 'duration', 'certification', 'startPeriod')