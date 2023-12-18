# Flask Blog Application

## Description
This project is a web-based blog application built with the Flask framework. It allows users to create, edit, and delete blog posts, and supports user authentication.

## Features
- User authentication (login/logout)
- Posting blog articles
- Editing and deleting posts
- Viewing posts in reverse chronological order
- (Any additional features you have implemented)

## Technologies Used
- Flask
- SQLAlchemy
- Flask-Login
- Bootstrap (for frontend design)
- SQLite (or any other database you've used)

## Setup and Installation
To get this project up and running on your local machine, follow these steps.

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/ranil-rai/Final_Project.git
   cd your-Final_Project
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```
   python
   >>> from app import create_app, db
   >>> app = create_app()
   >>> with app.app_context():
   >>>     db.create_all()
   ```

5. Run the application:
   ```
   python run.py
   ```

6. Access the application in your browser at `http://127.0.0.1:5000/`.

## Usage
After running the application, you can:
- Register a new user account
- Log in with existing credentials
- Create, edit, and delete blog posts

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-your-issues-page) if you want to contribute.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact
Created by [ranil-rai](ranilrai22@gmail.com) - feel free to contact me!
```

