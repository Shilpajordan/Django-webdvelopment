from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
import json
from .models import Appointment


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == 'POST':

        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send email
        send_mail(
            message_name , #subject
            message, #message
            message_email, # from email
            ['drschaefer@gmail.com'],# to email
            fail_silently=False,  # to throw up an error message if it fails
        )

        return render(request, 'contact.html', {'message_name': message_name})
    
    else:
        #
        return render(request, 'contact.html', {})
    


def webhook_handler(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Extract relevant information from the webhook data
        name = data['event']['invitee']['name']
        appointment_datetime = data['event']['start_time']
        # Save data to the database
        appointment = Appointment.objects.create(name=name, appointment_datetime=appointment_datetime)
        return JsonResponse({'message': 'Appointment saved successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
