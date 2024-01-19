import django_filters
from .models import Job

class jobFilter(django_filters.FilterSet):
        title = django_filters.CharFilter(lookup_expr='icontains')
        class Meta:
                model = Job
                fields = ['job_type','title','job_type','salary','cat']
