# Course Management System (Django)

A full-featured Course Management System built with Django, featuring course discovery, enrollment management, student accounts, instructor listings, and category filtering.

## Features Implemented

- **Authentication & Profiles:** Student registration, login/logout, and custom student profiles.
- **Courses & Categories:** Course listing, keyword search, instructor filter, and category filter.
- **Enrollment Management:** Course enrollment, status updates, duplicate prevention, and cancellation.
- **Admin Dashboard:** Full management for Instructors, Courses, Categories, and Enrollments.
- **Demo Data Seeder:** Automated command to populate initial data.

## Tech Stack

- Python / Django 6.1
- Bootstrap 5 & Bootstrap Icons
- SQLite

## Setup Instructions

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/Mo7ammed-Ja3far/iti-tasks/tree/final_project
   
   cd django_final_project
   \`\`\`

3. **Create and activate a virtual environment:**
   \`\`\`bash
   python -m venv venv

   # Windows:

   venv\Scripts\activate

   # Linux/macOS:

   source venv/bin/activate
   \`\`\`

4. **Install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

5. **Apply database migrations:**
   \`\`\`bash
   python manage.py migrate
   \`\`\`

6. **Populate demo data (Seeder):**
   \`\`\`bash
   python manage.py seed_data
   \`\`\`

7. **Create an admin superuser (optional):**
   \`\`\`bash
   python manage.py createsuperuser
   \`\`\`

8. **Run the development server:**
   \`\`\`bash
   python manage.py runserver
   \`\`\`
   Access the app at \`http://127.0.0.1:8000/\`.

## Demo Credentials

- **Student User:** \`omar_hassan\` | **Password:** \`pass12345\`
- **Student User:** \`nour_ali\` | **Password:** \`pass12345\`
