from django.shortcuts import render
from .models import Block
from .serializers import BlockData
from django.http import JsonResponse

# Create your views here.
def detail_view(request,pk):
  blu=Block.objects.get(id=pk)
  serializer=BlockData(blu)
  return JsonResponse(serializer.data)

def list_view(request):
  blu=Block.objects.all()
  serializer=BlockData(blu,many=True)
  return JsonResponse(serializer.data,safe=False)  