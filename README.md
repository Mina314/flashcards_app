# flashcards_app

This is a full-stack web app with database connectivity that replicates the Leitner system for efficient flashcard learning.

* The Leitner system is a widely used method of efficiently using flashcards that was proposed by the German science journalist Sebastian Leitner in 1972. It is a simple implementation of the principle of spaced repetition, where cards are reviewed at increasing intervals.
<img width="555" alt="Screen Shot 2023-07-22 at 10 01 40 AM" src="https://github.com/Mina314/flashcards_app/assets/64227723/1d59b382-a209-4f6c-a253-cfacca8fb3c1">

But in this project, I implemented a three-box system for flashcards instead of three, it allows users to test their knowledge and move cards to higher boxes upon correct answers.

This project is run in a virtual environment, you can find the venv folder inside. 
# Why Do You Need Virtual Environments?
Python isn’t great at dependency management. Virtual environments are like isolated bubbles for projects. They help keep things organized and prevent any messy clashes between different packages. By using them, you can manage dependencies, test code, and ensure your projects run smoothly without causing chaos in the system. They also make it easier to share projects with teammates and deploy them on different machines. 

** I used Visual Studio Code built this project. If you are using Visual Studio Code too, please nake sure that you installed Django extension and check if you have selected the correct Python interpreter in Visual Studio Code by the steps below:
Open your Django project in Visual Studio Code, and in the bottom status bar, click on the Python version. Select the correct Python interpreter that has Django installed. (Usually, it has the recommended one with the 'venv' in it)

## Create a Virtual Environment and Add Dependencies
First, you can make a folder called 'flashcards-app' and go to the folder in the terminal. 
```

mkdir flashcards_app
cd flashcards_app

```

Then, set up a virtual environment and active it:
```

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

```

After active the virtual environment, we can add dependincies (in the terminal, you should see (venv) in the front of your username):
```
pip install django
```

After installing Django, you can check its version using the following command:
```
python -m django --version

```

Initialize your Django project:
```
django-admin startproject flashcards .

```

## Run the Django project: 
Once the virtual environment is activated, you can run your Django project by using the following command:
```
python manage.py runserver

```

## Demo:

<img width="486" alt="Screenshot 2023-10-09 at 12 28 38 PM" src="https://github.com/Mina314/flashcards_app/assets/64227723/92d530da-1a45-4158-a680-d7f82a3212ac">

<img width="467" alt="Screenshot 2023-10-09 at 12 28 50 PM" src="https://github.com/Mina314/flashcards_app/assets/64227723/5a20d24a-3655-4295-80ed-41fb50996bf2">

<img width="440" alt="Screenshot 2023-10-09 at 12 29 58 PM" src="https://github.com/Mina314/flashcards_app/assets/64227723/6159bcd5-8ddc-4fd3-830a-e07ba7f46575">
