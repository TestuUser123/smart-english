from django.core import paginator
from django.shortcuts import render, redirect,  get_object_or_404
from settings import servis_setting
from django.http import JsonResponse, request
from .models import *
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'home.html')

def login_request(request):
    return render(request, 'log-in.html')

def config(request):
    return render(request, 'config.html')

def teachers(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_teacher(request.POST)
            return redirect('/teachers')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_teacher(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            
            return render(request, 'add_teacher.html')
        elif 'id' in request.GET:
           
            context = {
                
                'teachers': servis_setting.get_teacher(request.GET['id']),
            }
            return render(request, 'edit_teacher.html', context=context)
        else:
            ctx = {}
            url_parameter = request.GET.get("q")
            amount = TeacherTypes.objects.all().count()

            if url_parameter:
                teacher = TeacherTypes.objects.filter(teacher_rank__icontains=url_parameter)
            else:
                teacher = TeacherTypes.objects.all()
            paginator = Paginator(teacher, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number) 
            ctx = {
                'teacher':teacher, 'page_obj':page_obj,
                'amount':amount,
            }
            if request.is_ajax():

                html = render_to_string(
                    template_name="settings/search/teacher-results.html", context={'teacher':teacher, 'page_obj':page_obj, 'amount':amount,}
                )
                data_dict = {"html_from_view": html}
                return JsonResponse(data=data_dict, safe=False)
            return render(request, 'teacher.html', context=ctx)


def delete_teacher(request, id):
    teacher = TeacherTypes.objects.get(id=id)
    teacher.delete()
    return redirect('/teacher')


def salary(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_salary(request.POST)
            return redirect('/salary')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_salary(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            lesson_type = LessonType.objects.all()
            group = Group.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'lesson_type': lesson_type,
                'group': group
            }
            return render(request, 'add_salary.html', context)
        elif 'id' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            lesson_type = LessonType.objects.all()
            group = Group.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'lesson_type': lesson_type,
                'group': group,
                'salaries': servis_setting.get_salary(request.GET['id']),
            }
            return render(request, 'edit_salary.html', context=context)
        else:
            ctx = {}
            url_parameter = request.GET.get("q")

            if url_parameter:
                salary = Salary.objects.filter(subject_name__name__icontains=url_parameter)
            else:
                salary = Salary.objects.all()
            paginator = Paginator(salary, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number) 
            ctx = {
                'salary':salary, 'page_obj':page_obj,
            }
            if request.is_ajax():

                html = render_to_string(
                    template_name="settings/search/salary-results.html", context={'salary':salary, 'page_obj':page_obj,}
                )
                data_dict = {"html_from_view": html}
                return JsonResponse(data=data_dict, safe=False)
            return render(request, 'salary.html', context=ctx)

def delete_salary(request, id):
    salary = Salary.objects.get(id=id)
    salary.delete()
    return redirect('/salary')


def times(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_time(request.POST)
            return redirect('/time')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_time(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            lesson_type = LessonType.objects.all()
            group = Group.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'lesson_type': lesson_type,
                'group': group
            }
            return render(request, 'add_time.html', context)
        elif 'id' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            lesson_type = LessonType.objects.all()
            group = Group.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'lesson_type': lesson_type,
                'group': group,
                'times': servis_setting.get_times(request.GET['id'])
            }
            return render(request, 'edit_time.html', context=context)
        else:
            ctx = {}
            url_parameter = request.GET.get("q")

            if url_parameter:
                time = Timetable.objects.filter(subject_name__name__icontains=url_parameter)
            else:
                time = Timetable.objects.all()
            paginator = Paginator(time, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            
            ctx = {
                'time':time, 'page_obj':page_obj,
            }
            if request.is_ajax():

                html = render_to_string(
                    template_name="settings/search/time-results.html", context={'time':time, 'page_obj':page_obj,}
                )
                data_dict = {"html_from_view": html}
                return JsonResponse(data=data_dict, safe=False)

            return render(request, 'time.html', context=ctx)

def delete_time(request, id):
    time = Timetable.objects.get(id=id)
    time.delete()
    return redirect('/time')

def other(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_other(request.POST)
            return redirect('/other')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_other(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
            }
            return render(request, 'add_other.html', context)
        elif 'id' in request.GET:
            subject = Subjects.objects.all()
            lesson_pattern = Patterns.objects.all()
            context = {
                'subject': subject,
                'lesson_pattern': lesson_pattern,
                'others': servis_setting.get_other(request.GET['id'])
            }
            return render(request, 'edit_other.html', context=context)
        else:
            ctx = {}
            url_parameter = request.GET.get("q")

            if url_parameter:
                other = Other.objects.filter(subject_name__name__icontains=url_parameter)
            else:
                other = Other.objects.all()
            paginator = Paginator(other, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            
            ctx = {
                'other':other, 'page_obj':page_obj,
            }
            if request.is_ajax():

                html = render_to_string(
                    template_name="settings/search/other-results.html", context={'other':other, 'page_obj':page_obj,}
                )
                data_dict = {"html_from_view": html}
                return JsonResponse(data=data_dict, safe=False)
            return render(request, 'other.html', context=ctx)

def delete_other(request, id):
    other = Other.objects.get(id=id)
    other.delete()
    return redirect('/other')

def room(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_room(request.POST)
            return redirect('/room')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_room(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            building_name = Building.objects.all()
            room_type = RoomType.objects.all()           
            context = {
                'building_name': building_name,
                'room_type': room_type,
            }
            return render(request, 'add_room.html', context)
        elif 'id' in request.GET:
            building_name = Building.objects.all()
            room_type = RoomType.objects.all()
            context = {
                'building_name': building_name,
                'room_type': room_type,
                'rooms': servis_setting.get_room(request.GET['id']),
            }
            return render(request, 'edit_room.html', context=context)
        else:
            ctx = {}
            url_parameter = request.GET.get("q")

            if url_parameter:
                room = Room.objects.filter(building_name__name__icontains=url_parameter)
            else:
                room = Room.objects.all()
            paginator = Paginator(room, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            ctx = {
                'room':room, 'page_obj':page_obj,
            }
            if request.is_ajax():

                html = render_to_string(
                    template_name="settings/search/room-results.html", context={'room':room, 'page_obj':page_obj,}
                )
                data_dict = {"html_from_view": html}
                return JsonResponse(data=data_dict, safe=False)
            return render(request, 'room.html', context=ctx)

def delete_room(request, id):
    room = Room.objects.get(id=id)
    room.delete()
    return redirect('/room')

def students(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_student(request.POST)
            return redirect('/students')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_student(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            building = Building.objects.all()
            context = {
                'building': building,
            }
            return render(request, 'add_student.html', context)
        elif 'id' in request.GET:
            building = Building.objects.all()
            context = {
                'building': building,
                'students': servis_setting.get_student(request.GET['id']),
            }
            return render(request, 'edit_student.html', context=context)
        else:
            ctx = {}
            url_parameter = request.GET.get("q")

            if url_parameter:
                students = Student.objects.filter(first_name__icontains=url_parameter)
            else:
                students = Student.objects.all()
            paginator = Paginator(students, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            ctx = {
                'students':students, 'page_obj':page_obj,
            }
            if request.is_ajax():

                html = render_to_string(
                    template_name="settings/search/students-results.html", context={'students':students, 'page_obj':page_obj,}
                )
                data_dict = {"html_from_view": html}
                return JsonResponse(data=data_dict, safe=False)
            return render(request, 'student.html', context=ctx)

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/students')

def building(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            servis_setting.add_edit_building(request.POST)
            return redirect('/building')
        elif request.POST['action'] == 'delete':
            response = servis_setting.delete_building(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            return render(request, 'add_building.html')
        elif 'id' in request.GET:
            context = {
                'buildings': servis_setting.get_building(request.GET['id'])
            }
            return render(request, 'edit_building.html', context=context)
        else:
            ctx = {}
            url_parameter = request.GET.get("q")

            if url_parameter:
                buildings = Building.objects.filter(name__icontains=url_parameter)
            else:
                buildings = Building.objects.all()
            paginator = Paginator(buildings, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            ctx = {
                'buildings':buildings, 'page_obj':page_obj,
            }
            if request.is_ajax():

                html = render_to_string(
                    template_name="settings/search/building-results.html", context={'buildings':buildings, 'page_obj':page_obj,}
                )
                data_dict = {"html_from_view": html}
                return JsonResponse(data=data_dict, safe=False)

            return render(request, 'building.html', context=ctx)

def delete_building(request, id):
    building = Building.objects.get(id=id)
    building.delete()
    return redirect('/building')

