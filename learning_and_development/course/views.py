from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import CourseForm
from django.db.models import Q
from django.contrib import messages
from learning_and_development.config import COURSE_API_URL,DJANGO_ENV, RUN_LOCAL
import requests
 
def course_list(request):
    print(f"DJANGO_ENV: {DJANGO_ENV} and RUN_LOCAL: {RUN_LOCAL}")
    if DJANGO_ENV == 'production' and not RUN_LOCAL:
        base_url = f"{COURSE_API_URL}/courses/"
        try:
            response = requests.get(base_url)
            courses = response.json()
            if response.status_code == 200:
                # print(f"Response: {courses}")
                return render(request, 'course_list.html', {'courses': courses})
            else:
                messages.error(request, f"Error fetching courses: {response.status_code}")
                return render(request, 'course_list.html', {'courses': []})
        except requests.exceptions.RequestException as e:
            # print(e)
            messages.error(request, f"Error fetching courses: {e}")
            return render(request, 'course_list.html', {'courses': []})
    else:
        courses = Course.objects.all()  
        query = request.GET.get('q', '')
        if query:
            courses = Course.objects.filter(Q(title__icontains=query))
        else:
            courses = Course.objects.all()
        return render(request, 'course_list.html', {'courses': courses, 'query': query})

def course_detail_by_title(request, title):
    base_url = f"{COURSE_API_URL}/course/details/{title}"
    try:
        response = requests.get(base_url)
        course = response.json()
        if response.status_code == 200:
            # print(f"Response: {course}")
            return render(request, 'course_detail.html', {'course': course})
        else:
            # print(f"Error fetching courses: {response.status_code}")
            messages.error(request, f"Error fetching courses: {response.status_code}")
            return render(request, 'course_list.html', {'courses': []})
    except requests.exceptions.RequestException as e:
            messages.error(request, f"Error fetching courses: {e}")   
            return render(request, 'course_list.html', {'courses': []})
    
def course_detail_by_id(request,id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_detail.html', {'course': course})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            messages.success(request, 'Course added successfully!')
            return render(request, 'course_detail.html', {'course': course})
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"Error in {field.label}: {error}")
    else:
        print("GET request")
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def course_update(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            messages.success(request, 'Course updated successfully!')
            return render(request, 'course_detail.html', {'course': course})
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"Error in {field.label}: {error}")
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form, 'course': course})


