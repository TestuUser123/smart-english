from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


app_name = 'settings'

urlpatterns = [
	path('config/', views.config, name='config'),
	path('time/', views.time, name='time'),
	path('building/', views.building, name='building'),
	path('room/', views.room, name='room'),
	path('', views.dashboard, name='dashboard'),
	path('teacher/', views.teacher, name='teacher'),
	path('salary/', views.salary, name='salary'),
	path('other/', views.other, name='other'),
	path('student/', views.student, name='student'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	path('password_reset/', auth_views.PasswordResetView.as_view(),	name='password_reset'),	
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),	name='password_reset_done'), 
	path('reset/<uidb64>/<token>/',	auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),	
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	path('register/', views.register, name='register'),
	path('edit/', views.edit, name='edit'),
	path('profile/', views.profile, name='profile'),
	path('modal_time/', views.modal_time, name='modal_time'),
	path('modal_teacher/', views.modal_teacher, name='modal_teacher'),
	path('modal_salary/', views.modal_salary, name='modal_salary'),
	path('modal_building/', views.modal_building, name='modal_building'),
	path('modal_other/', views.modal_other, name='modal_other'),
	path('modal_room/', views.modal_room, name='modal_room'),
	path('modal_student/', views.modal_student, name='modal_student'),
	]