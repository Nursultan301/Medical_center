from django.contrib import admin

from medical.models import Doctor, Enroll, Feedback, Subscription


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'img')


@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'weeks', 'time', 'doctors')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
