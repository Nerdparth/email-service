from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import send_email
# Create your views here.

@csrf_exempt
def process_data(request):
    if request.method == "POST":
        data = eval(request.body.decode('utf-8'))
        try:
            send_email.delay(data['email'],data['username'],data['template'],data['subject'])
        except Exception as e:
            return JsonResponse({"status":500,"message":"email not sent "})
    return JsonResponse({"status":200,"message":"email sent successfully"})




