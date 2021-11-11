from django.db import models
from settings.models import Building, Staff, Room, Group, TeacherRole


class TeacherRole(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'Teacher Role'
        verbose_name_plural = 'Teacher Role'


class GroupPattern(models.Model):
    group_pattern = models.CharField(max_length=255)

    def __str__(self):
        return self.group_pattern

    class Meta:
        verbose_name = 'Group Pattern'
        verbose_name_plural = 'Group Pattern'


class NewGroup(models.Model):
    group_number = models.CharField(max_length=30)
    main_teacher = models.ForeignKey(
        Staff, related_name='main_teacher', on_delete=models.CASCADE)
    teacher_role = models.ForeignKey(
        TeacherRole, related_name='teacher_role', on_delete=models.CASCADE)
    examiner = models.ForeignKey(
        Staff, related_name='examiner', on_delete=models.CASCADE)
    first_lesson = models.DateField(auto_now_add=False, blank=True, null=True)
    building = models.ForeignKey(
        Building, related_name='building', on_delete=models.CASCADE)
    group_room = models.ForeignKey(
        Room, related_name='group_room', on_delete=models.CASCADE)
    group_type = models.ForeignKey(
        Group, related_name='new_group_type', on_delete=models.CASCADE)
    lesson_time = models.TimeField(max_length=255)
    lesson_days = models.CharField(max_length=255)
    group_pattern = models.ForeignKey(
        GroupPattern, related_name='new_group_pattern', on_delete=models.CASCADE)
    total_lessons = models.CharField(max_length=30)
    payment = models.CharField(max_length=30)
    exam_date = models.DateField(auto_now_add=False, blank=True, null=True)
