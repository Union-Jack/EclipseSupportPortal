# Eclipse Support Portal Project
Eclipse Support Portal is a Flask-based web application designed to assist IT support ticket management. It allows users to create, view, update, and delete tickets with role-based permissions. The backend uses Flask for routing and authentication, Flask-Login for session handling and SQLAlchemy as the ORM layer. Password encryption is handled  using bcrypt and form inputs are managed and validated through WTForms. On the frontend, the interface is styled with Bootstrap, supported by HTML, CSS, and Jinja2 templating. Data is stored in a SQLite3 database, and the system is tested using Pytest.

## Features
- **Secure User Registration & Login** – Users can sign up and log in with encrypted credentials using Flask-Login and bcrypt.
- **Role-Based Access Control (RBAC)** – Admins (support staff) and standard users (clients/internal staff) have access to specific functionality based on their role.
- **Ticket Lifecycle Management** – Users can perform full CRUD operations on support tickets, with restrictions applied according to user roles.
- **Commenting System** – Users can create and edit comments within tickets, enabling discussion and clarification between support staff and users.
- **Modular Codebase with Flask Blueprints** – Structured architecture promotes maintainability and scalability of application components.
- **Form Validation** – WTForms ensures valid user inputs throughout the application's forms.
- **Seed Data** – Preloaded, non-sensitive sample data showcases functionality for development and demonstration.
- **Testing Suite** – Pytest tests ensure the quality and functionality of the application throughout development.  

## Getting Started
#### Prerequisites:
Ensure you have installed Python 3 and Git.

#### Installation: 
In git Bash:
1. git clone https://github.com/Union-Jack/EclipseSupportPortal.git
2. cd EclipseSupportPortal
3. py -m venv venv
4. source venv/Scripts/activate
5. pip install -r requirements.txt

#### Usage:
Running the project:
flask run 

Testing the project:
pytest tests/

## File Structure
    EclipseSupportPortal/
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
    ├── references.md          # Script to populate the database with initial seed data
    ├── seed_data.py           # List of sources cited within the code
    └── app.py                 # Entry point for running the app

## Notes
To run the application and tests from the Visual Studio Code terminal you may need to:
1. Install the python extension
2. Ctrl+Shift+P enter Python: Select Interpreter 
3. Select the interpriter with the route .\venv\Scripts\python.exe

## Seed Data
To demonstrate functionality, the application currently wipes all data on startup before seeding new data from the seed_data.py class.
To remove seed data and persist changes, simply remove db.drop_all() and seed_database() from app_factory.py

The seeded data is currently as follows:
##### User Seed Data
| Role  | Username               | Password         |
|-------|------------------------|------------------|
| Admin | EclipseManager_Jack    | Management#987   |
| Admin | EclipseSupport_Pete    | Eclipse@123!     |
| Admin | EclipseSupport_Lucy    | Support!678      |
| User  | MediHire_John          | Health#321!      |
| User  | CareTalent_Sarah       | CareRecruit@25   |
| User  | HealthBridge_Mark      | NurseXyz!        |
| User  | BuildForce_Mike        | Constuct123      |
| User  | TradeSkills_Emma       | TradeHire@2025   |
| User  | EduTalent_Lisa         | TeachHire456!    |
| User  | UniHire_Daniel         | UniRecruit@24    |

##### Ticket Seed Data
| Ticket ID | Title                              | Priority  | Status       | Author              | Assignee               |
|-----------|------------------------------------|-----------|--------------|---------------------|------------------------|
| 1         | Issue with Login                   | High      | Open         | HealthBridge_Mark   | EclipseSupport_Pete    |
| 2         | Email Notifications Not Working    | Medium    | Pending      | TradeSkills_Emma    | EclipseManager_Jack    |
| 3         | Database Connection Issue          | Critical  | In Progress  | CareTalent_Sarah    | EclipseSupport_Lucy    |
| 4         | UI Glitch on Mobile                | Low       | Open         | MediHire_John       | EclipseManager_Jack    |
| 5         | Access Denied Error                | High      | Resolved     | CareTalent_Sarah    | EclipseSupport_Lucy    |
| 6         | Integration Issue                  | Medium    | Pending      | HealthBridge_Mark   | EclipseSupport_Pete    |
| 7         | Server Downtime                    | Critical  | In Progress  | BuildForce_Mike     | EclipseManager_Jack    |
| 8         | Ticket Assignment Bug              | High      | Open         | TradeSkills_Emma    | Unassigned             |
| 9         | Performance Lag                    | Medium    | In Progress  | EduTalent_Lisa      | EclipseManager_Jack    |
| 10        | User Profile Updates Not Saving    | Low       | Open         | UniHire_Daniel      | Unassigned             |

##### Comment Seed Data
| Ticket ID | Author              | Comment Snippet                                                              |
|-----------|---------------------|------------------------------------------------------------------------------|
| 1         | EclipseSupport_Pete | “Looks like a password caching issue...”                                     |
| 1         | HealthBridge_Mark   | “I’ve cleared saved credentials and tried again…”                            |
| 2         | EclipseManager_Jack | “I've checked the email server logs…”                                        |
| 3         | EclipseSupport_Lucy | “I've confirmed that this is a database timeout.”                            |
| 4         | EclipseManager_Jack | “Confirmed: Mobile UI breaks on Safari…”                                     |
| 5         | EclipseSupport_Lucy | “Can you please provide some additional clarification…”                      |
| 5         | CareTalent_Sarah    | "It’s specifically the create candidate and create client functionality."    |
| 6         | EclipseSupport_Pete | "Investigating API authentication logs now."                                 |
| 7         | EclipseManager_Jack | "Investigating downtime reported at peak hours…”                             |
| 9         | EclipseManager_Jack | "Confirmed: High latency caused by large dataset queries."                   |

## Contact
For questions or issues, please contact me at jack-summerville@hotmail.co.uk.