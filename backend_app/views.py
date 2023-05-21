from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserForm


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

        form = UserForm(name=name, dob=dob, email=email, phone=phone)
        form.save()

        return JsonResponse({'message': 'Form submitted successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})


def get_submitted_forms(request):
    forms = UserForm.objects.all()
    print(forms)
    data = [{'name': form.name, 'dob': form.dob, 'email': form.email, 'phone': form.phone} for form in forms]
    return JsonResponse(data, safe=False)