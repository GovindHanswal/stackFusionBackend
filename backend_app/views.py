from django.http import JsonResponse
import json
from .models import UserForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import re
# Create your views here.

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        dob = data.get('dob')
        email = data.get('email')
        phone = data.get('phone')

        # Perform form validation and other logic here
        phone_regex = re.compile(r'^\d{10}$')
        if not phone_regex.match(phone):
            return JsonResponse({'message': 'Invalid phone number'}, status=400)

        form = UserForm(name=name, dob=dob, email=email, phone=phone)
        form.save()
        # send_email
        subject="Here is the confirmation mail"
        message="Thank you for joining us"
        from_email=settings.EMAIL_HOST_USER
        to_email=[email]
        send_mail(subject,message,from_email,to_email)

        return JsonResponse({'message': 'Form submitted successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})


def get_submitted_forms(request):
    forms = UserForm.objects.all()
    print(forms)
    data = [{'name': form.name, 'dob': form.dob, 'email': form.email, 'phone': form.phone} for form in forms]
    return JsonResponse(data, safe=False)
