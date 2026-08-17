from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Course, Instructor, Category, Enrollment
from .forms import EnrollmentForm
def course_list(request):
    query = request.GET.get('q', '').strip()
    instructor_id = request.GET.get('instructor', '').strip()
    category_id = request.GET.get('category', '').strip()

    courses = Course.objects.select_related('instructor', 'category').all()

    if query:
        courses = courses.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    if instructor_id and instructor_id.isdigit():
        courses = courses.filter(instructor_id=int(instructor_id))
    if category_id and category_id.isdigit():
        courses = courses.filter(category_id=int(category_id))

    instructors = Instructor.objects.all()
    categories = Category.objects.all()

    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'instructors': instructors,
        'categories': categories,
        'query': query,
        'selected_instructor': int(instructor_id) if instructor_id.isdigit() else None,
        'selected_category': int(category_id) if category_id.isdigit() else None,
    })
def course_detail(request, pk):
    course = get_object_or_404(Course.objects.select_related('instructor', 'category'), pk=pk)
    enrollments = course.enrollments.select_related('student__user').all()

    is_enrolled = False
    student_enrollment = None
    if request.user.is_authenticated and hasattr(request.user, 'student_profile'):
        student_enrollment = enrollments.filter(student=request.user.student_profile).first()
        is_enrolled = student_enrollment is not None

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'enrollments': enrollments,
        'is_enrolled': is_enrolled,
        'student_enrollment': student_enrollment,
    })


def instructor_detail(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    courses = instructor.courses.all()
    return render(request, 'courses/instructor_detail.html', {
        'instructor': instructor,
        'courses': courses,
    })


@login_required
def enroll_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    student = request.user.student_profile

    # تحقق من التسجيل المسبق لمنع التكرار
    enrollment, created = Enrollment.objects.get_or_create(
        student=student,
        course=course,
        defaults={'status': 'active'}
    )

    if created:
        messages.success(request, f"Successfully enrolled in {course.title}!")
    else:
        messages.warning(request, f"You are already enrolled in this course.")

    return redirect('courses:course_detail', pk=course.pk)


@login_required
def edit_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk, student=request.user.student_profile)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment status updated successfully.")
            return redirect('accounts:profile')
    else:
        form = EnrollmentForm(instance=enrollment)

    return render(request, 'courses/edit_enrollment.html', {
        'form': form,
        'enrollment': enrollment,
    })


@login_required
def cancel_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk, student=request.user.student_profile)

    if request.method == 'POST':
        course_title = enrollment.course.title
        enrollment.delete()
        messages.success(request, f"Enrollment for {course_title} has been cancelled.")
        return redirect('accounts:profile')

    return render(request, 'courses/confirm_cancel.html', {'enrollment': enrollment})