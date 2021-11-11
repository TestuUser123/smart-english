from register.views import *
from settings.models import *


def add_edit_add_staff(form):
    result = {}
    if 'id' in form:
        try:
            print(type(form))
            role = TeacherRole.objects.get(id=form['occupation'])
            workplace = Building.objects.get(id=form['workplace'])
            staff = Staff.objects.get(id=form['id'])
            staff.first_name = form['fname']
            staff.born_date = form['birthday']
            staff.document_type = form['pass']
            staff.last_name = form['surname']
            staff.register_date = form['app-date']
            staff.passport_id = form['passport']
            staff.middle_name = form['father-name']
            staff.id_code = form['id-code']
            staff.id_card_number = form['id-card']
            staff.gender = form['gender']
            staff.role = role
            staff.workplace = workplace
            staff.login = form['login']
            staff.password = form['password']
            staff.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        try:
            role = TeacherRole.objects.get(id=form['occupation'])
            workplace = Building.objects.get(id=form['workplace'])
            staff = Staff.objects.create(
                first_name=form['fname'],
                born_date=form['birthday'],
                document_type=form['pass'],
                last_name=form['surname'],
                register_date=form['app-date'],
                passport_id=form['passport'],
                middle_name=form['father-name'],
                id_code=form['id-code'],
                id_card_number=form['id-card'],
                gender=form['gender'],
                role=role,
                workplace=workplace,
                login=form['login'],
                password=form['password'],
            )
            staff.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    return result


def get_add_staff(id):
    return Staff.objects.get(id=id)


def delete_add_staff(form):
    result = {}
    if Staff.objects.filter(id=form['id']).exists():
        try:
            Staff.objects.filter(id=form['id']).delete()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        result['success'] = False
        result['error'] = 'Object not found!'
    return result 
