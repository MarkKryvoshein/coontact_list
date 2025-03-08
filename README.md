# Contact List

#### This project is a web application built using Django (Python) and Jinja templating. It allows users to submit contact forms, which are then saved to a database and displayed on the main page. The application demonstrates how to handle form submissions, store data in a database, and dynamically render the saved data on the front end using Jinja templates.

Technologies Used:
Backend: Django (Python)

Frontend: HTML, CSS, JavaScript (with Jinja templating for dynamic content)

Database: SQLite

Templating Engine: Jinja

How It Works:
A user visits the website and fills out the contact form.

Upon submission, the form data is sent to the Django backend.

The backend validates the data and saves it to the database.

The main page fetches the saved contact form entries from the database and displays them dynamically using Jinja templates.





# django_template
Template for django start projects
1. Обрати розміщення для майбутнього проєкту

    `D:` - перейти на обраний диск <br>
    `cd розміщення/назва теки` - зайти до директорії <br>
    `cd..` - перейти до попередньої директорії <br>
    `dir` - показати вміст поточної теки <br>

2. Створити теку
    ``` bash
   md "Назва-тексту"
   ```
3. Клонувати 
    ```bash
   git clone "<https://github.com/MarkKryvoshein/django_template.git>"
   ```
4. Віртуальне середовище
   - Створити віртуальне середовище `.venv`
   ```bash
     #створення віртуального середовища 
     python -m vevn .venv
    ```
   - Активація віртуального середовища
      ```bash
      #Windows
      .venv\Scripts\activate
   
      #Linux/Mac OS
      .venv\bin\activate
     ```
   
становлення необхідних модулей
   ```bash
   pip install request.txt
   ```



# Example Table

| Photo     	| Lastname   	| Name   	| Phone    	| Email               	|
|-----------	|------------	|--------	|----------	|---------------------	|
| image.png 	| Ivanov     	| Ivan   	| +38..... 	| something@gmail.com 	|
| image.png 	| Melnik     	| Maksim 	| +38..... 	| something@gmail.com 	|
| image.png 	| Ribbentrop 	| Ulrich 	| +38..... 	| something@gmail.com 	|

Additional Notes:

You can extend this project by adding features like:

Pagination for the contact list.

Search and filtering functionality.

Exporting contact data to CSV or Excel.

User authentication for secure access to the contact list.