from django.shortcuts import render, get_object_or_404
from .models import Course
 
def course_list(request):
    course = Course.objects.all()
    return render(request, 'course_list.html', {'courses': course})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_detail.html', {'course': course})

