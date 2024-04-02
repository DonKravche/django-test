# Django
This repository includes a Django tutorial on how to create a Django environment and how to create a superuser in it.

# What you need to do?
- 1. you should install
     ```py
     pip install django
- 2. after that type command to run server (which will redirect you to the main Django page) and click localhost destination link:
     ```py
     python manage.py runserver
     
     
![image](https://github.com/DonKravche/django-test/assets/138400870/6f77ee07-9d1d-4cc4-b73f-4b5cde059c85)
![image](https://github.com/DonKravche/django-test/assets/138400870/dccc17e9-6652-4039-8047-3883fcfcd7c0)

- 3. type in search bar (/admin after localhost address) to move Administering Django page
     ```
     http://127.0.0.1:8000/admin/login/?next=/admin/

- 4. Before you enter the users in the fields, you must run the migrations to create the basic Jago database.
     ```py
     python manage.py migrate

- 5. To Create super user write:
     ```py
     python manage.py createsuperuser
     
- 6. Follow the instructions

- 7. now you are ready to write created user to the Administering Django page and log in <3
     ![image](https://github.com/DonKravche/django-test/assets/138400870/e00afa62-409a-40dd-8d08-f67fa41a3471)
     
- 8. Congratulations You made it !
  ![image](https://github.com/DonKravche/django-test/assets/138400870/9ac3de9b-f6e2-4ff6-96e2-ebff650bdb80)

- 9. Fell Free to test and use my code !
