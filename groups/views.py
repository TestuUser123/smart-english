from django.shortcuts import render, redirect
from groups import service_setting
from settings.models import *
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string

def groups(request):
    return render(request, 'groups/group.html')

def new_group(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            service_setting.add_edit_group(request.POST)
            return redirect('/new-group')
        elif request.POST['action'] == 'delete':
            response = service_setting.delete_group(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            main_teacher = Staff.objects.all()
            teacher_role = TeacherRole.objects.all()
            examiner = Staff.objects.all()
            building = Building.objects.all()
            group_room = Room.objects.all()
            group_type = Group.objects.all()
            group_pattern = GroupPattern.objects.all()
            context = {
                'main_teacher': main_teacher,
                'teacher_role': teacher_role,
                'examiner': examiner,
                'building': building,
                'group_room': group_room,
                'group_type': group_type,
                'group_pattern': group_pattern,
            }
            return render(request, 'groups/add_group.html', context)
        elif 'id' in request.GET:
            main_teacher = Staff.objects.all()
            teacher_role = TeacherRole.objects.all()
            examiner = Staff.objects.all()
            building = Building.objects.all()
            group_room = Room.objects.all()
            group_type = Group.objects.all()
            group_pattern = GroupPattern.objects.all()
            context = {
                'main_teacher': main_teacher,
                'teacher_role': teacher_role,
                'examiner': examiner,
                'building': building,
                'group_room': group_room,
                'group_type': group_type,
                'group_pattern': group_pattern,
                'groups': service_setting.get_groups(request.GET['id'])
            }
            return render(request, 'groups/edit-group.html', context=context)
        else:
            ctx = {}
            url_parameter = request.GET.get("q")

            if url_parameter:
                new_group = NewGroup.objects.filter(group_number__icontains=url_parameter)
            else:
                new_group = NewGroup.objects.all()
            paginator = Paginator(new_group, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
 
            ctx = {
                'new_group':new_group, 'page_obj':page_obj,
            }
            if request.is_ajax():

                html = render_to_string(
                    template_name="groups/search/new-group-results.html", context={'new_group':new_group, 'page_obj':page_obj,}
                )
                data_dict = {"html_from_view": html}
                return JsonResponse(data=data_dict, safe=False)
            return render(request, 'groups/new-group.html', context=ctx)

def delete_group(request, id):
    group = NewGroup.objects.get(id=id)
    group.delete()
    return redirect('/new-group')

def attendance(request):
    return render(request, 'groups/attendance.html')

def view_attendance(request):
    return render(request, 'groups/view-attendance.html')

def active_group(request):
    english_groups = NewGroup.objects.all().count()
    return render(request, 'groups/group-now.html', context={'english_groups':english_groups})

def ended_group(request):
    return render(request, 'groups/ended-group.html')