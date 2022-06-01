from django.urls import path
from .views import DoctorsFormView, FeedbackCreateView, SubscriptionCreateView

urlpatterns = [
    path('', DoctorsFormView.as_view(), name='home'),
    path('create/', FeedbackCreateView.as_view(), name='create_feedback'),
    path('create-subscription/', SubscriptionCreateView.as_view(), name='create_subscription')

]