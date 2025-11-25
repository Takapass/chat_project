# Django Chat Application

This project is a chat application built using Django, with Python as the backend and HTML/CSS for the frontend. The application includes various features such as user authentication, chat functionality, and profile management.

## Features

- **Chat Functionality**: Users can join chat rooms and communicate in real-time.
- **User Authentication**: Users can register, log in, and log out.
- **Profile Management**: Users can view and edit their profiles.
- **Automated Room Management**: Chat rooms are automatically created and deleted every day at midnight.
- **Random User Assignment**: Users are randomly assigned to newly created chat rooms.

## Project Structure

```
django-chat-app
├── manage.py
├── db.sqlite3
├── requirements.txt
├── chat_project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chat
│   ├── migrations
│   │   └── __init__.py
│   ├── management
│   │   ├── commands
│   │   │   └── delete_old_rooms.py
│   │   └── __init__.py
│   ├── templates
│   │   ├── chat
│   │   │   ├── room.html
│   │   │   └── room_list.html
│   │   ├── auth
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── logout.html
│   │   └── profile
│   │       ├── profile.html
│   │       └── edit_profile.html
│   ├── static
│   │   └── css
│   │       ├── style.css
│   │       └── profile.css
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── tasks.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-chat-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations to set up the database:
   ```
   python manage.py migrate
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Register a new account or log in with an existing account to start using the chat features.

## License

This project is licensed under the MIT License.