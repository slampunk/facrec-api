from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from recognition.models import RecognitionRequest
from recognition.serializers import RecognitionRequestSerializer
from recognition.image import RunRecognition

@csrf_exempt
@api_view(['POST'])
def recognition_attempt(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = JSONParser().parse(request)
    serializer = RecognitionRequestSerializer(data=data)
    if serializer.is_valid():
        result = RunRecognition(data)
        return JsonResponse(result, status=200)

    return JsonResponse(serializer.errors, status=400)
