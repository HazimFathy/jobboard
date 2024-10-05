from .models import job
from .serializers import jobserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    all_jobs=job.objects.all()
    data=jobserializer(all_jobs,many=True).data
    return Response({'data':data})
    
@api_view(['GET'])   
def job_detail_api(request,id):
    job_detail=job.objects.get(id=id)
    data=jobserializer(job_detail).data
    return Response({'data':data})
    
class joblist(generics.ListCreateAPIView):
    queryset=job.objects.all()
    serializer_class=jobserializer
    
    
class jobdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=job.objects.all()
    serializer_class=jobserializer
    lookup_field='id'