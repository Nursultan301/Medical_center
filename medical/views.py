from django.views.generic import FormView, CreateView

from medical.forms import EnrollForm, FeedbackForm, SubscriptionForm
from medical.models import Doctor, Feedback, Subscription


class DoctorsFormView(FormView):
    form_class = EnrollForm
    success_url = '/'
    template_name = 'index.html'

    def form_valid(self, form):
        form.save()
        return super(DoctorsFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(DoctorsFormView, self).get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()
        context['feedback'] = FeedbackForm()
        context['subscription'] = SubscriptionForm()
        return context


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_url = '/'


class SubscriptionCreateView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    success_url = '/'
