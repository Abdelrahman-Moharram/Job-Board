from rest_framework import routers, serializers, viewsets
from .models import Job



class jobSerial(serializers.ModelSerializer):
        class Meta:
                model = Job
                fields = '__all__'