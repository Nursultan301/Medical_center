from modeltranslation.translator import register, TranslationOptions

from medical.models import Doctor


@register(Doctor)
class DoctorTranslation(TranslationOptions):
    fields = ('name', 'description', 'position')
