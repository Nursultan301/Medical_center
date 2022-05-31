from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from medical.models import Doctor, Enroll, Feedback, Subscription


@admin.register(Doctor)
class DoctorAdmin(TranslationAdmin):
    list_display = ('name', 'description', 'get_photo')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.img.url}" width="75">')


@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'weeks', 'time', 'doctors')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
