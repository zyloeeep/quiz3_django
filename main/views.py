from django.shortcuts import render
from .models import Student

from django.shortcuts import render

def home(request):
    students = [
        {
            "student_id": "024-12033",
            "first_name": "Cielo",
            "last_name": "Seco",
            "course": "BS Information Technology",
            "year_level": 3,
            "email": "cieloseco@gmail.com",
        },
        {
            "student_id": "024-12034",
            "first_name": "Gab",
            "last_name": "Reyz",
            "course": "BS Computer Science",
            "year_level": 2,
            "email": "gabreyz@gmail.com",
        },
        {
            "student_id": "024-12035",
            "first_name": "Kataru",
            "last_name": "Raven",
            "course": "BS Accountancy",
            "year_level": 1,
            "email": "kataruraven@gmail.com",
        },
    ]
    return render(request, "main/home.html", {"students": students})