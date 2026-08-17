from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import StudentRegistrationForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('courses:course_list')

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # تحديث بيانات البروفايل الإضافية
            student = user.student_profile
            student.phone_number = form.cleaned_data.get('phone_number')
            student.bio = form.cleaned_data.get('bio')
            student.save()

            login(request, user)
            messages.success(request, f"Welcome to the platform, {user.username}!")
            return redirect('courses:course_list')
    else:
        form = StudentRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('courses:course_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, f"You are now logged in as {user.username}.")
            next_url = request.GET.get('next', 'courses:course_list')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('courses:course_list')


@login_required
def profile_view(request):
    student = request.user.student_profile
    enrollments = student.enrollments.select_related('course', 'course__instructor').all()
    return render(request, 'accounts/profile.html', {
        'student': student,
        'enrollments': enrollments
    })