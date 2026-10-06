from django.urls import path
from bookings_v2.views import SignUpView,AppointmentListCreateView

urlpatterns=[
    path('signup/',SignUpView.as_view()),
    path('appointments/',AppointmentListCreateView.as_view()),
]