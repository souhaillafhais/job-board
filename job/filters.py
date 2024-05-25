import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains')
    description = django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['owner','salary','Availability','image','published_at','slug']