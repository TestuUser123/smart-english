from groups.views import *
from groups.models import *
from settings.models import *


def add_edit_group(form):
    result = {}
    if 'id' in form:
        try:
            print(type(form))
            main_teacher = Staff.objects.get(id=form['main-teacher'])
            teacher_role = TeacherRole.objects.get(id=form['teacher-role'])
            examiner = Staff.objects.get(id=form['examiner'])
            building = Building.objects.get(id=form['building'])
            group_room = Room.objects.get(id=form['group-room'])
            group_type = Group.objects.get(id=form['group-type'])
            group_pattern = GroupPattern.objects.get(id=form['group-pattern'])
            group = NewGroup.objects.get(id=form['id'])
            group.group_number = form['group-number']
            group.main_teacher = main_teacher
            group.teacher_role = teacher_role
            group.examiner = examiner
            group.first_lesson = form['first-lesson']
            group.building = building
            group.group_room = group_room
            group.group_type = group_type
            group.lesson_time = form['lesson-time']
            group.lesson_days = form['lesson-days']
            group.group_pattern = group_pattern
            group.total_lessons = form['total-lessons']
            group.payment = form['payment']
            group.exam_date = form['exam-date']
            group.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        try:
            main_teacher = Staff.objects.get(id=form['main-teacher'])
            teacher_role = TeacherRole.objects.get(id=form['teacher-role'])
            examiner = Staff.objects.get(id=form['examiner'])
            building = Building.objects.get(id=form['building'])
            group_room = Room.objects.get(id=form['group-room'])
            group_type = Group.objects.get(id=form['group-type'])
            group_pattern = GroupPattern.objects.get(id=form['group-pattern'])
            group = NewGroup.objects.create(
                group_number=form['group-number'],
                main_teacher=main_teacher,
                teacher_role=teacher_role,
                examiner=examiner,
                first_lesson=form['first-lesson'],
                building=building,
                group_room=group_room,
                group_type=group_type,
                lesson_time=form['lesson-time'],
                lesson_days=form['lesson-days'],
                group_pattern=group_pattern,
                total_lessons=form['total-lessons'],
                payment=form['payment'],
                exam_date=form['exam-date'],
            )
            group.save()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    return result


def get_groups(id):
    return NewGroup.objects.get(id=id)


def delete_group(form):
    result = {}
    if NewGroup.objects.filter(id=form['id']).exists():
        try:
            NewGroup.objects.filter(id=form['id']).delete()
            result['success'] = True
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
    else:
        result['success'] = False
        result['error'] = 'Object not found!'
    return result
