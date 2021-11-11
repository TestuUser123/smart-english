from django.shortcuts import render
from settings.views import *
from settings.models import *
from register import service_setting


def list_config(request):
    return render(request, 'register/list-config.html')


def add_staff(request):
    if request.is_ajax and request.method == 'POST':
        print(request.POST)
        if request.POST['action'] == 'add':
            service_setting.add_edit_add_staff(request.POST)
            return redirect('/add-staff')
        elif request.POST['action'] == 'delete':
            response = service_setting.delete_add_staff(request.POST)
            return JsonResponse(response, status=200, safe=False)
    if request.method == 'GET':
        if 'add' in request.GET:
            
            return render(request, 'register/add-add-staff.html')
        elif 'id' in request.GET:
           
            context = {
                
                'staff': service_setting.get_add_staff(request.GET['id']),
            }
            return render(request, 'register/edit-add-staff.html', context=context)
        else:
            ctx = {}
            url_parameter = request.GET.get("q")

            if url_parameter:
                staff = Staff.objects.filter(first_name__icontains=url_parameter)
            else:
                staff = Staff.objects.all()
            paginator = Paginator(staff, 1)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number) 
            ctx = {
                'staff':staff, 'page_obj':page_obj,
            }
            if request.is_ajax():

                html = render_to_string(
                    template_name="register/search/add-staff-results.html", context={'staff':staff, 'page_obj':page_obj,}
                )
                data_dict = {"html_from_view": html}
                return JsonResponse(data=data_dict, safe=False)
            
            return render(request, 'register/add-staff.html', context=ctx)


def delete_add_staff(request, id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    return redirect('/add-staff')
