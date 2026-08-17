from django.contrib import admin
from .models import Instructor, Course, Category, Enrollment

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'category', 'enrolled_students_count', 'created_at')
    list_filter = ('instructor', 'category', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'enrolled_at')
    list_filter = ('status', 'enrolled_at')
    search_fields = ('student__user__username', 'course__title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)