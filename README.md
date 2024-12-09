Job Finder Application: Backend-Only Django Project

This is a backend application built using Django for managing job postings and applications. It allows users to register, create profiles, search for jobs, and apply for them. Admins can manage job postings and view applications. The application provides API endpoints for all these functionalities.

Features:
User Registration & Login: Users can create accounts and log in to access features.

Profile Management: Users can create and update their profiles.

Job Search: Users can browse and search for jobs using filters such as title, location, and salary.

Job Application: Users can apply for jobs, and their applications are stored and tracked.

Admin functionality: Admins can create, edit, delete jobs, and view job applications.

Role-based Access Control: Only admins can manage jobs and view applications. Regular users can only search and apply for jobs.

Requirements:
Python 3.x, Django 4.x, Django REST Framework, SQLite (default) or any other database supported by Django, API Endpoints

Register:

POST /api/register/ json { "username": "username", "password": "password" }

Manage Profile:

GET/POST /api/profile/

Headers: Authorization: Token

Job Listings:

GET /apiview/jobs/

Apply for Job:

POST /apiview/jobs/<job_id>/apply/

Headers: Authorization: Token

Admin Job Management (Create/Update/Delete Jobs, View Applications):

Requires Admin Token.

Run Tests

python manage.py test

Tools (Postman/cURL)

Use Postman or cURL to interact with the API. For authenticated routes, provide the Authorization: Token header.
