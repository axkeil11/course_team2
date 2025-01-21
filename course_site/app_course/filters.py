from django_filters import FilterSet
from .models import Course


class CourseFilter(FilterSet):
    class Meta:
        model=Course
        fields = {
            'price':['gt', 'lt'],
            'category':['exact'],
            'course_name':['exact']
        }