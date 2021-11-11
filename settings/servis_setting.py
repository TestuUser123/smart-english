from settings.views import *
from settings.models import *


def add_edit_time(form):
    result = {}
    if 'id' in form:
        try:
            print(type(form))
            subject = Subjects.objects.get(id=form['subject'])
            lesson_pattern = Patterns.objects.get(id=form['subject-type'])
            lesson_type = LessonType.objects.get(id=form['lesson-type'])
            group = Group.objects.get(id=form['group'])
            time = Timetable.objects.get(id=form['id'])
            time.subject_name = subject
            time.lesson_pattern = lesson_pattern
            time.lesson_type = lesson_type
            time.group_type = group
            time.start_time = form['start-time']
            time.finish_time = form['end-time']
            time.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        try:
            subject = Subjects.objects.get(id=form['subject'])
            lesson_pattern = Patterns.objects.get(id=form['subject-type'])
            lesson_type = LessonType.objects.get(id=form['lesson-type'])
            group = Group.objects.get(id=form['group'])
            time = Timetable.objects.create(
                subject_name=subject,
                lesson_pattern=lesson_pattern,
                lesson_type=lesson_type,
                group_type=group,
                start_time=form['start-time'],
                finish_time=form['end-time']
            )
            time.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    return result


def get_times(id):
    return Timetable.objects.get(id=id)


def delete_time(form):
    result = {}
    if Timetable.objects.filter(id=form['id']).exists():
        try:
            Timetable.objects.filter(id=form['id']).delete()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        result['success'] = False
        result['error'] = 'Object not found!'
    return result 


def add_edit_teacher(form):
    result = {}
    if 'id' in form:
        try:
            print(type(form))
            teacher = TeacherTypes.objects.get(id=form['id'])
            teacher.teacher_rank = form['position']
            teacher.role = form['vakolat']
            teacher.employees = form['staff-number']
            teacher.added_time = form['date']
            teacher.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        try:
            teacher = TeacherTypes.objects.create(
            teacher_rank = form['position'],
            role = form['vakolat'],
            employees = form['staff-number'],
            added_time = form['date'],
            )
            teacher.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    return result


def get_teacher(id):
    return TeacherTypes.objects.get(id=id)


def add_edit_salary(form):
    result = {}
    if 'id' in form:
        try:
            print(type(form))
            subject = Subjects.objects.get(id=form['subject-name'])
            lesson_pattern = Patterns.objects.get(id=form['lesson-pattern'])
            lesson_type = LessonType.objects.get(id=form['lesson-type'])
            group = Group.objects.get(id=form['group-type'])
            salary = Salary.objects.get(id=form['id'])
            salary.subject_name = subject
            salary.lesson_pattern = lesson_pattern
            salary.lesson_type = lesson_type
            salary.group_type = group
            salary.month_amount = form['month-amount']
            salary.monthly_fee = form['monthly-fee']
            salary.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        try:
            subject = Subjects.objects.get(id=form['subject-name'])
            lesson_pattern = Patterns.objects.get(id=form['lesson-pattern'])
            lesson_type = LessonType.objects.get(id=form['lesson-type'])
            group = Group.objects.get(id=form['group-type'])
            salary = Salary.objects.create(
                subject_name=subject,
                lesson_pattern=lesson_pattern,
                lesson_type=lesson_type,
                group_type=group,              
                month_amount=form['month-amount'],              
                monthly_fee=form['monthly-fee'],
            )
            salary.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    return result

def get_salary(id):
    return Salary.objects.get(id=id)


def delete_salary(form):
    result = {}
    if Salary.objects.filter(id=form['id']).exists():
        try:
            Salary.objects.filter(id=form['id']).delete()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        result['success'] = False
        result['error'] = 'Object not found!'
    return result

def add_edit_other(form):
    result = {}
    if 'id' in form:
        try:
            print(type(form))
            subject = Subjects.objects.get(id=form['subject-name'])
            lesson_pattern = Patterns.objects.get(id=form['lesson-pattern'])
            other = Other.objects.get(id=form['id'])
            other.subject_name = subject
            other.lesson_pattern = lesson_pattern
            other.weekly_plan = form['weekly-plan']
            other.monthly_plan = form['monthly-plan']
            other.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        try:
            subject = Subjects.objects.get(id=form['subject-name'])
            lesson_pattern = Patterns.objects.get(id=form['lesson-pattern'])
            other = Other.objects.create(
                subject_name=subject,
                lesson_pattern=lesson_pattern,
                weekly_plan=form['weekly-plan'],
                monthly_plan=form['monthly-plan'],
                total_lessons=form['total-lessons'], 
                course_duration=form['course-duration'], 
            )
            other.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    return result

def get_other(id):
    return Other.objects.get(id=id)


def delete_other(form):
    result = {}
    if Other.objects.filter(id=form['id']).exists():
        try:
            Other.objects.filter(id=form['id']).delete()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        result['success'] = False
        result['error'] = 'Object not found!'
    return result

def add_edit_room(form):
    result = {}
    if 'id' in form:
        try:
            print(type(form))
            building_name = Building.objects.get(id=form['building-name'])
            room_type = RoomType.objects.get(id=form['room-type'])
            room = Room.objects.get(id=form['id'])
            room.building_name = building_name
            room.room_type = room_type
            room.room_number = form['room-number']
            room.owner = form['room-teacher']
            room.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        try:
            building_name = Building.objects.get(id=form['building-name'])
            room_type = RoomType.objects.get(id=form['room-type'])
            room = Room.objects.create(
                building_name=building_name,
                room_type=room_type,
                room_number=form['room-number'],
                owner=form['room-teacher'],
            )
            room.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    return result

def get_room(id):
    return Room.objects.get(id=id)


def delete_room(form):
    result = {}
    if Room.objects.filter(id=form['id']).exists():
        try:
            Room.objects.filter(id=form['id']).delete()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        result['success'] = False
        result['error'] = 'Object not found!'
    return result

def add_edit_student(form):
    result = {}
    if 'id' in form:
        try:
            print(type(form))
            building_name = Building.objects.get(id=form['building'])
            student = Student.objects.get(id=form['id'])
            student.first_name = form['name']
            student.middle_name = form['middle-name']
            student.last_name = form['surname']
            student.id_code = form['id-code']
            student.register_date = form['register-date']
            student.born_date = form['born-date']
            student.student_age = form['id-code']
            student.document_type = form['document-type']
            student.id_number = form['id-number'] #passport
            student.id_card_number = form['id-card-number']
            student.level = form['level']
            student.free_time = form['lesson-time']
            student.address = form['address']
            student.building_name = building_name
            student.tel_number = form['tel']
            student.student_login = form['login']
            student.student_password = form['password']
            student.status = True
            student.gender = form['gender']
            student.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        try:
            building_name = Building.objects.get(id=form['building'])
            student = Student.objects.create(
                building_name=building_name,
                first_name=form['name'],
                middle_name=form['middle-name'],
                last_name=form['surname'],
                id_code=form['id-code'],
                register_date=form['register-date'],
                born_date=form['born-date'],
                student_age=form['id-code'],
                document_type=form['document-type'],
                id_number=form['id-number'],
                id_card_number=form['id-card-number'],
                level=form['level'],
                free_time=form['lesson-time'],
                address=form['address'],
                tel_number=form['tel'],
                student_login=form['login'],
                student_password=form['password'],
                status=True,
                gender=form['gender'],
            )
            student.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    return result

def get_student(id):
    return Student.objects.get(id=id)


def delete_student(form):
    result = {}
    if Student.objects.filter(id=form['id']).exists():
        try:
            Student.objects.filter(id=form['id']).delete()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        result['success'] = False
        result['error'] = 'Object not found!'
    return result

def add_edit_building(form):
    result = {}
    if 'id' in form:
        try:
            print(type(form))
            building = Building.objects.get(id=form['id'])
            building.name = form['building-name']
            building.location = form['address']
            building.room_amount = form['room-amount']
            building.nickname = form['nickname']
            building.added_time = form['added-time']
            building.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        try:
            building = Building.objects.create(
                name=form['building-name'],
                location=form['address'],
                room_amount=form['room-amount'],
                nickname=form['nickname'],
                added_time=form['added-time'],
            )
            building.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    return result

def get_building(id):
    return Building.objects.get(id=id)

def delete_building(form):
    result = {}
    if Building.objects.filter(id=form['id']).exists():
        try:
            Building.objects.filter(id=form['id']).delete()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        result['success'] = False
        result['error'] = 'Object not found!'
    return result
