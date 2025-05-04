# How to Run the Project

Follow the steps below to set up the project on your local machine.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Node.js (for Tailwind CSS)
- Git (for version control)

## 1. Clone the Repository
#### First, clone the repository to your local machine.
- git clone https://github.com/leodellosa/learning_and_dev_project.git "Learning and Dev Project"
- cd Learning and Dev Project

## 2. Set Up a Virtual Environment
#### Create and activate a Python virtual environment:
- python -m venv .venv
- source .venv/scripts/activate

## 3. Install Dependencies
#### Install Python dependencies via pip:
- pip install -r requirements.txt

## 4. Set Up Tailwind CSS
#### Since Tailwind CSS is used for styling, run the following to set up Tailwind:
- python manage.py tailwind install

## 5. Set Up the Database
#### Run the following commands to set up the database:
- python manage.py makemigrations
- python manage.py migrate

## 6. Create a superuser account to access the Django admin:
#### Follow the prompts to set up the superuser credentials.
- python manage.py createsuperuser

## 7. Collect Static Files
### Run the following to collect all static files:
- python manage.py collectstatic

## 8. Run the Development Server
#### Now, you can run the Django development server:
- python manage.py runserver
- The application will now be available at http://localhost:8000.

## 9. Tailwind CSS
#### For development with hot-reloading:
- python manage.py tailwind start

#### If you're preparing for production:
- python manage.py tailwind build
- python manage.py collectstatic

## 10. Accessing Django Admin
-  Once the server is running, you can access the Django Admin by visiting http://localhost:8000/admin/ and logging in with the superuser credentials you just created.

## 11. Stopping the Application
- To stop the development server, simply press Ctrl+C in your terminal.


