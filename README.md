# Dua Saif - Personal Portfolio Website

This is my final project for CS50W: Web Programming with Python and JavaScript. I created a **personal portfolio website** to showcase my skills, projects, education, and contact information in a clean, professional, and responsive layout. Built using Django, HTML/CSS, and JavaScript, this website reflects both my technical experience and creative design choices.

Visitors can explore my projects, download my CV, view certificates and educational history, and get in touch via the contact form. The project is fully dynamic, with project entries managed via the Django admin interface, making it easy to update over time.

---

## Distinctiveness and Complexity

This project satisfies the **Distinctiveness and Complexity** requirements in the following ways:

### Distinctiveness:
- Unlike common CS50W project templates (e.g., e-commerce sites or Wikipedia clones), this portfolio was built from scratch to serve a real personal need.
- It integrates Django’s admin functionality to dynamically manage project entries.
- The design features custom animations (e.g., an envelope-flip effect on the contact section) that enhance user experience.
- It includes a fully responsive design for desktop and mobile viewing, with a custom sidebar layout and JavaScript interactivity.

### Complexity:
- The application consists of multiple pages with custom views, templates, and logic: Home, About, Projects, Skills, CV, Contact, and Education.
- A dynamic "Projects" section uses Django models to pull data from the database and display them automatically on the frontend.
- The "Contact" form processes user input using Django’s form handling and displays success messages upon submission.
- Frontend JavaScript adds interactivity, like toggleable menus and animated transitions.
- The entire site structure is modular, using reusable templates and separate static files for maintainability.

---

## File Structure and Description

portfolio-site/
├── portfolio-site/ # Django project settings and root configuration
│ ├── settings.py # Configures installed apps, templates, static/media handling
│ ├── urls.py # Main URL routing to portfolio_app
│ └── wsgi.py / asgi.py # Server entry points
│
├── portfolio_app/ # Main application logic
│ ├── admin.py # Registers the Project model for admin interface
│ ├── models.py # Defines Project model
│ ├── views.py # View logic for each page
│ ├── urls.py # URL patterns for app views
│ ├── templates/ # HTML templates
│ │ ├── home.html
│ │ ├── about.html
│ │ ├── projects.html
│ │ ├── contact.html
│ │ ├── cv.html
│ │ ├── dua_saif_cv.html
│ │ └── education.html
│ ├── static/portfolio/ # CSS and JavaScript assets
│ │ ├── styles.css
│ │ ├── script.js
│ │ └── envelope-flip.css # Special effect used on contact form
│
├── images/portfolio_app/ # Images for projects, profile, etc.
├── manage.py # Django's management script
├── db.sqlite3 # SQLite database
├── requirements.txt # Python dependencies
└── README.md # This file


---

## How to Run the Application

To run this project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/dua-saif/portfolio-site.git
   cd portfolio-site

