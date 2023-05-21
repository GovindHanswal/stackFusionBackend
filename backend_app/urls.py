from django.urls import path
from .views import submit_form, get_submitted_forms

urlpatterns = [
    path('submit-form/', submit_form, name='submit_form'),
    path('submitted-forms/', get_submitted_forms, name='submitted-forms'),
]
