from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ClearSteps.models import Personality
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return HttpResponse("API Index View")

@csrf_exempt
def PersonalityEntry(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            email_id = data.get("email")
            persona = data.get("personality")
            if not email_id or not persona:
                return JsonResponse({"error": "Both email and personality are required."}, status=400)
            personality,created = Personality.objects.get_or_create(
                email=email_id,
                defaults={"personality":persona})
            if not created and personality.personality != persona:
                personality.personality = persona
                personality.save()
            response = {
                'email':personality.email,
                'personality':personality.personality
            }    
            return JsonResponse(response,status=200) 
        else:
            return JsonResponse({"error": "Invalid HTTP method. Only POST is allowed."}, status=405)   
    except Exception as e:
        return JsonResponse({'error':str(e)},status=400)

def getPersonality(request):
    try:
        if request.method=="GET":
            email_id = request.GET.get("email")
            if not email_id:
                return JsonResponse({"error":"Please provide email id"},status=400)
            try:
                personality = Personality.objects.get(email=email_id)
            except Personality.DoesNotExist:
                return JsonResponse({"error":"No data found for the email"},status=404)  
            response = {
                "email":personality.email,
                "personality":personality.personality
            }
            return JsonResponse(response,status=200)
        else:
            return JsonResponse({"error":"The API call must be GET only"},status=400)
    except Exception as e:
        return JsonResponse({"error":str(e)},status=400)
                        

    