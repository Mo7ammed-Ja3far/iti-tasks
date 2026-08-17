from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Student
from courses.models import Category, Instructor, Course, Enrollment


class Command(BaseCommand):
    help = "Seeds initial demo data for testing the Course Management System."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("⏳ Seeding data..."))

        # 1. Categories
        categories_data = [
            {"name": "Web Development", "description": "Frontend, backend, and full-stack web technologies."},
            {"name": "Data Science & AI", "description": "Data analysis, machine learning, and generative AI."},
            {"name": "Mobile Development", "description": "Native and cross-platform mobile apps."},
            {"name": "DevOps & Cloud", "description": "Docker, Kubernetes, CI/CD, and Cloud architectures."},
        ]

        categories = {}
        for item in categories_data:
            cat, created = Category.objects.get_or_create(
                name=item["name"],
                defaults={"description": item["description"]}
            )
            categories[item["name"]] = cat

        self.stdout.write(self.style.SUCCESS(" Categories seeded."))

        # 2. Instructors
        instructors_data = [
            {
                "name": "Dr. Angela Yu",
                "email": "angela@example.com",
                "bio": "Lead instructor with over 10 years of experience teaching web development and python."
            },
            {
                "name": "Andrew Ng",
                "email": "andrew@example.com",
                "bio": "Pioneer in AI and Machine Learning education, founder of DeepLearning.AI."
            },
            {
                "name": "Brad Traversy",
                "email": "brad@example.com",
                "bio": "Practical full-stack web developer and creator of Traversy Media."
            },
            {
                "name": "Maximilian Schwarzmüller",
                "email": "max@example.com",
                "bio": "Professional web developer specializing in React, Next.js, and modern JavaScript."
            },
        ]

        instructors = {}
        for item in instructors_data:
            inst, created = Instructor.objects.get_or_create(
                name=item["name"],
                defaults={"email": item["email"], "bio": item["bio"]}
            )
            instructors[item["name"]] = inst

        self.stdout.write(self.style.SUCCESS(" Instructors seeded."))

        # 3. Courses
        courses_data = [
            {
                "title": "Django 6 Complete Mastery",
                "description": "Master Django from scratch: models, views, templates, auth, REST APIs, and deployment.",
                "instructor": instructors["Brad Traversy"],
                "category": categories["Web Development"],
            },
            {
                "title": "React & Next.js Advanced Architecture",
                "description": "Learn state management, Server Components, SSR, API routes, and Tailwind CSS.",
                "instructor": instructors["Maximilian Schwarzmüller"],
                "category": categories["Web Development"],
            },
            {
                "title": "Machine Learning Specialization",
                "description": "A comprehensive deep dive into supervised learning, neural networks, and decision trees.",
                "instructor": instructors["Andrew Ng"],
                "category": categories["Data Science & AI"],
            },
            {
                "title": "Python for Data Analysis & Automation",
                "description": "Learn pandas, numpy, web scraping, and task automation using modern Python.",
                "instructor": instructors["Dr. Angela Yu"],
                "category": categories["Data Science & AI"],
            },
            {
                "title": "Docker & Kubernetes for Production",
                "description": "Containerize microservices, orchestrate clusters, and set up CI/CD pipelines.",
                "instructor": instructors["Brad Traversy"],
                "category": categories["DevOps & Cloud"],
            },
        ]

        courses = []
        for item in courses_data:
            course, created = Course.objects.get_or_create(
                title=item["title"],
                defaults={
                    "description": item["description"],
                    "instructor": item["instructor"],
                    "category": item["category"],
                }
            )
            courses.append(course)

        self.stdout.write(self.style.SUCCESS(" Courses seeded."))

        # 4. Demo Students (Users)
        students_data = [
            {"username": "omar_hassan", "email": "omar@example.com", "first_name": "Omar", "last_name": "Hassan"},
            {"username": "nour_ali", "email": "nour@example.com", "first_name": "Nour", "last_name": "Ali"},
            {"username": "youssef_khalid", "email": "youssef@example.com", "first_name": "Youssef", "last_name": "Khalid"},
        ]

        students = []
        for item in students_data:
            user, created = User.objects.get_or_create(
                username=item["username"],
                defaults={
                    "email": item["email"],
                    "first_name": item["first_name"],
                    "last_name": item["last_name"],
                }
            )
            if created:
                user.set_password("pass12345")  # Default password
                user.save()
            
            student, _ = Student.objects.get_or_create(user=user)
            students.append(student)

        self.stdout.write(self.style.SUCCESS(" Students & Accounts seeded (Default password: pass12345)."))

        # 5. Enrollments
        enrollments_data = [
            (students[0], courses[0], "active"),
            (students[0], courses[1], "completed"),
            (students[1], courses[0], "active"),
            (students[1], courses[2], "active"),
            (students[2], courses[3], "active"),
        ]

        for student, course, status in enrollments_data:
            Enrollment.objects.get_or_create(
                student=student,
                course=course,
                defaults={"status": status}
            )

        self.stdout.write(self.style.SUCCESS(" Enrollments seeded."))
        self.stdout.write(self.style.SUCCESS("\n🎉 Database seeded successfully! Ready for demo."))