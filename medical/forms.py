from django import forms

from medical.models import Enroll, Feedback, Subscription


class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = "__all__"

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
        'weeks': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Недели'}),
        'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Время'}),
        'doctors': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Врачи'}),
        'messages': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Сообщения', 'rows': 5}),
    }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            'requirements': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Требования'}),
            'messages': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Сообщения', 'rows': 5}),
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"

        widget = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
        }
