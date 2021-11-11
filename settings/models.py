from django.db import models
from django.conf import settings
from django.db.models.fields import DateField


class TeacherRole(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'Teacher Role'
        verbose_name_plural = 'Teacher Role'


class Subjects(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Group(models.Model):
    group_type = models.CharField(max_length=60)

    def __str__(self):
        return self.group_type
    
    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class LessonType(models.Model):
    lesson_types = models.CharField(max_length=255)

    def __str__(self):
        return self.lesson_types
    
    class Meta:
        verbose_name = 'Lesson type'
        verbose_name_plural = 'Lesson Types'


class Patterns(models.Model):
    patterns = models.CharField(max_length=255)

    def __str__(self):
        return self.patterns
    
    class Meta:
        verbose_name = 'Lesson Pattern'
        verbose_name_plural = 'Lesson Patterns'

class Timetable(models.Model):
    subject_name = models.ForeignKey(Subjects, related_name='subject_name', on_delete=models.CASCADE)
    lesson_pattern = models.ForeignKey(Patterns, related_name='lesson_patterns', on_delete=models.CASCADE)
    lesson_type = models.ForeignKey(LessonType, related_name='lessons', on_delete=models.CASCADE)
    group_type = models.ForeignKey(Group, related_name='group_types', on_delete=models.CASCADE)
    start_time = models.TimeField()
    finish_time = models.TimeField()

    class Meta:
        verbose_name = 'timetable'
        verbose_name_plural = 'timetable'


class Salary(models.Model):
    subject_name = models.ForeignKey(Subjects, related_name='salary_subject_name', on_delete=models.CASCADE)
    lesson_pattern = models.ForeignKey(Patterns, related_name='salary_lesson_patterns', on_delete=models.CASCADE)
    lesson_type = models.ForeignKey(LessonType, related_name='salary_lessons', on_delete=models.CASCADE)
    group_type = models.ForeignKey(Group, related_name='salary_group_types', on_delete=models.CASCADE)
    month_amount = models.IntegerField()
    monthly_fee = models.IntegerField()
    
    class Meta:
        verbose_name = 'salary'
        verbose_name_plural = 'salary'


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Profile for user {{ self.user.username}}'    


class Building(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    room_amount = models.IntegerField(default=0)
    nickname = models.CharField(max_length=255)
    added_time = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'building'
        verbose_name_plural = 'buildings'


class Staff(models.Model):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    id_code = models.CharField(max_length=250)
    gender = models.CharField(max_length=25)
    register_date = models.DateField()
    born_date = models.DateField()
    document_type = models.CharField(max_length=250)
    passport_id = models.CharField(max_length=250)
    id_card_number = models.CharField(max_length=25)
    role = models.ForeignKey(TeacherRole, related_name='teacher_role', on_delete=models.CASCADE)
    workplace = models.ForeignKey(Building, related_name='workplace', on_delete=models.CASCADE)
    login = models.CharField(max_length=250)
    password = models.CharField(max_length=250) 

    def __str__(self):
        return self.first_name + self.middle_name + self.last_name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Other(models.Model):
    subject_name = models.ForeignKey(Subjects, related_name='other_subject_name', on_delete=models.CASCADE)
    lesson_pattern = models.ForeignKey(Patterns, related_name='other_lesson_patterns', on_delete=models.CASCADE)
    weekly_plan = models.IntegerField()
    monthly_plan = models.IntegerField()
    total_lessons = models.IntegerField()
    course_duration = models.IntegerField()


class RoomType(models.Model):
    type = models.CharField(max_length=30)
    
    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Room type'
        verbose_name_plural = 'Room types'


class Room(models.Model):
    building_name = models.ForeignKey(Building, related_name='building_name', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=30)
    room_type = models.ForeignKey(RoomType, related_name='room_type', on_delete=models.CASCADE)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.room_number
    

class Student(models.Model):
    first_name = models.CharField(max_length = 150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    id_code = models.CharField(max_length=20)
    register_date = models.DateField(auto_now=False, auto_now_add=True)
    born_date = models.DateField(auto_now=False)
    student_age = models.IntegerField()
    document_type = models.CharField(max_length=150)
    id_number = models.CharField(max_length=20)
    id_card_number = models.CharField(max_length=25)
    level = models.CharField(max_length=20)
    free_time = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    building_name = models.ForeignKey(Building, related_name='student_building', on_delete=models.CASCADE)
    tel_number = models.CharField(max_length=20)
    student_login = models.CharField(max_length=150)
    student_password = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    gender = models.CharField(max_length=20)
    

class TeacherTypes(models.Model):
    teacher_rank = models.CharField(max_length = 150)
    role = models.CharField(max_length=150)
    employees = models.CharField(max_length=150)
    added_time = models.DateField()

    class Meta:
        verbose_name = 'Teacher type'
        verbose_name_plural = 'Teacher types'