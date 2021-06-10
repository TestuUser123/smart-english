from django.shortcuts import render, redirect, resolve_url
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import views 
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Timetable, Salary, Building, Staff, Other, Room, Student
from. models import Subjects, Group, LessonType, Patterns

@login_required
def dashboard(request):
	return render(request,'dashboard.html',{'section': 'dashboard'})

def config(request):
	return render(request, 'config.html')

def time(request):
	courses = Timetable.objects.all
	return render(request, 'time.html', {'courses':courses})

def building(request):
	buildings = Building.objects.all()
	return render(request, 'building.html', {'buildings':buildings})

def room(request):
	rooms = Room.objects.all()
	return render(request, 'room.html', {'rooms':rooms})

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(
				user_form.cleaned_data['password']
			)
			new_user.save()
			UserProfile.objects.create(user=new_user)
			return render(request, 'register_done.html',
			{'new_user':new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'register.html',
	{'user_form':user_form})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user,
		data=request.POST)
		profile_form = ProfileEditForm(
			instance=request.user.profile,
			data=request.POST,
			files=request.FILES
		)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
	return render(request, 'edit.html', {'user_form':user_form, 'profile_form':profile_form})


def profile(request):
	user = request.user
	return render(request, 'profile.html', {'user':user})

def teacher(request):
	teachers = Staff.objects.all()
	return render(request, 'teacher.html', {'teachers':teachers})

def salary(request):
	salary = Salary.objects.all()
	return render(request, 'salary.html', {'salary':salary})

def other(request):
	extra_details = Other.objects.all()
	return render(request, 'other.html', {'extra_details':extra_details})

def student(request):
	students = Student.objects.all()
	return render(request, 'student.html', {'students':students})

def modal_time(request):
	subjects = Subjects.objects.all()
	groups = Group.objects.all()
	lesson_types = LessonType.objects.all()
	lesson_patterns = Patterns.objects.all()
	if request.method == 'POST':
		subject = Subjects.objects.get(name=request.POST['subject'])
		subject_type = Patterns.objects.get(patterns=request.POST['subject-type'])
		lesson_type = LessonType.objects.get(lesson_types=request.POST['lesson-type'])
		group = Group.objects.get(group_type=request.POST['group'])
		timetable = Timetable.objects.create(
			subject_name=subject,
			group_type=group,
			lesson_pattern=subject_type,
			start_time=request.POST['start-time'],
			lesson_type=lesson_type,
			finish_time=request.POST['end-time']
		)
		timetable.save()
		return redirect('/time')
	return render(request, 'modal_time.html', 
	{'subjects':subjects, 'groups':groups, 'lesson_types':lesson_types,
	'lesson_patterns':lesson_patterns})


def modal_teacher(request):
	return render(request, 'modal_teacher.html')

def modal_salary(request):
	subjects = Subjects.objects.all()
	salary = Salary.objects.all()
	patterns = Patterns.objects.all()
	l_types = LessonType.objects.all()
	if request.method == 'POST':
		subject = Subjects.objects.get(name=request.POST['subject'])
		subject_type = Patterns.objects.get(patterns=request.POST['subject-type'])
		lesson_type = LessonType.objects.get(lesson_types=request.POST['lesson-type'])
		group = Group.objects.get(group_type=request.POST['group'])
		salary = Salary.objects.create(
			subject_name = subject,
			lesson_pattern = subject_type,
			lesson_type = lesson_type,
			group_type = group,
			month_amount = request.POST['start-time'],
			monthly_fee = request.POST['end-time']
		)
		salary.save()	
		return redirect('/salary')
	return render(request, 'modal_salary.html', {'salary':salary, 'patterns':patterns, 
	'l_types':l_types, 'subjects':subjects})

def modal_building(request):
	if request.method == 'POST':
		building = Building.objects.create(
		location = request.POST['address'],
		name = request.POST['name'],
		nickname = request.POST['nickname'],
		room_amount = request.POST['staff-number'],
		added_time = request.POST['date'],
		)
		building.save()
		return redirect('/building')
	return render(request, 'modal_building.html')

def modal_other(request):
	subjects = Subjects.objects.all()
	patterns = Patterns.objects.all()
	if request.method == 'POST':
		subject = Subjects.objects.get(name=request.POST['subject'])
		subject_type = Patterns.objects.get(patterns=request.POST['pattern'])
		other = Other.objects.create(
			subject_name = subject,
			lesson_pattern = subject_type,
			weekly_plan = request.POST['weekly-plan'],
			monthly_plan = request.POST['monthly-plan'],
			total_lessons = request.POST['total-lessons'],
			course_duration = request.POST['course-duration'],
		)
		other.save()
		return redirect('/other')
	return render(request, 'modal_other.html', {'subjects':subjects,
	"patterns":patterns})

def modal_room(request):
	buildings = Building.objects.all()
	rooms = Room.objects.all()
	if request.method == 'POST':
		building = Building.objects.get(name=request.POST['building'])
		room = Room.objects.create(
			building_name = building,
			room_number = request.POST['room-number'],
			room_type = request.POST['room-type'],
			owner = request.POST['room-teacher'],
		)
		room.save()
		return redirect('/room')
	return render(request, 'modal_room.html', {'buildings':buildings,
	'rooms':rooms})

def modal_student(request):
	buildings = Building.objects.all()
	if request.method == 'POST':
		building = Building.objects.get(name=request.POST['building'])
		student = Student.objects.create(
			first_name = request.POST['fname'],
			born_date = request.POST['birthday'],
			document_type = request.POST['doc'],
			last_name = request.POST['surname'],
			register_date = request.POST['app-date'],
			id_number = request.POST['id-number'],
			middle_name = request.POST['middle-name'],
			id_code = request.POST['id-code'],
			id_card_number = request.POST['id-card'],
			gender = request.POST['gender'],
			address = request.POST['address'],
			free_time = request.POST['week-day'],
			student_login = request.POST['login'],
			level = request.POST['level'],
			tel_number = request.POST['tel'],
			student_password = request.POST['password'],
			building_name = building,
			student_age = 10
		)
		student.save()
		return redirect('/student')
	return render(request, 'modal_student.html', {'buildings':buildings,})