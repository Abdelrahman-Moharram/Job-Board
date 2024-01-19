from .models import Job
from .serializers import jobSerial
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def job_list_api(request):
        jobs = Job.objects.all()
        jobs = jobSerial(jobs, many=True).data
        
        return Response({'jobs':jobs})