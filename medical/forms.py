from django import forms
from django.utils.translation import ugettext_lazy as _


from medical.models import Enroll, Feedback, Subscription


class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Имя'), 'class': 'form-control border-0'}),
            'email': forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control border-0'}),
            'weeks': forms.Select(attrs={'class': 'form-control', 'placeholder': _('Недели')}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': _('Время'), 'type': 'time'}),
            'messages': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Сообщения')}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'name': 'phone', 'placeholder': 'Телефон'}),
            'requirements': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Требования'}),
            'messages': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Сообщения', 'rows': 5}),
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
        }
