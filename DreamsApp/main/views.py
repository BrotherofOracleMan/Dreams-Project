from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main.models import Dream
from main.serializers import DreamSerializer

# Create your views here.
@csrf_exempt
def dream_list(request):
    """
        List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        dreams = Dream.objects.all()
        serializer = DreamSerializer(dreams, many = True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = DreamSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors ,status=400)

@csrf_exempt
def dream_detail(request, id):
    """
    Retrieve, update or delete
    """
    try:
        dream =  Dream.objects.get(id = id)
    except Dream.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = DreamSerializer(dream)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser.parse(request)
        serializer = DreamSerializer(dream, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONParser(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        dream.delete()
        return HttpResponse(status= 204)
    


    
    