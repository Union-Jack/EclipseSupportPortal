# Eclipse Support Portal Project
This project is Flask based web application for managing IT support desk tickets.

## Features
- User registration and login
- Role-based access control (admin vs. user)
- Create, edit, delete, and view support tickets
- Commenting system
- Flask blueprints and form validation

## Getting Started
1.  **Prerequisites:** 
    Ensure you have installed Python and Git.

2.  **Installation:** 
In git Bash:
1. git clone https://github.com/Union-Jack/EclipseSupportPortal.git
2. cd EclipseSupportPortal
3. py -m venv venv
4. source venv/Scripts/activate
5. pip install -r requirements.txt

3.  **Usage:** 
Running the project:
flask run 

Testing the project:
pytest tests/

## File Structure
    project-name/
    │
    ├── templates/             # Jinja2 templates for HTML rendering
    ├── static/                # Static assets (CSS, JavaScript, images)
    ├── models/                # SQLAlchemy models (User, Ticket, Comment)
    ├── forms/                 # WTForm classes for user input
    ├── routes/                # Blueprint route files (auth, tickets, comments)
    ├── app_factory.py         # Application factory that sets up the Flask app
    ├── tests/                 # Unit and integration tests
    ├── requirements.txt       # Python dependencies
    ├── readme.md              # Project documentation
    ├── seed_data.py           # Script to populate the database with initial seed data
    └── app.py                 # Entry point for running the app

## Notes
To run the application and tests from the Visual Studio Code terminal you may need to:
1. Install the python extension
2. Ctrl+Shift+P enter Python: Select Interpreter 
3. Select the interpriter with the route .\venv\Scripts\python.exe

## Contributing
If you would like to contribute, please:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them
4. Push to your fork (`git push origin feature-branch`)
5. Open a pull request with a clear description

## Contact
For questions or issues, please contact me at jack-summerville@hotmail.co.uk.