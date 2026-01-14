# TRADE OPERATIONS - LAMFIX LTD

A modern, professional corporate-grade Django website for LAMFIX LTD's trade operations business.

## About

TRADE OPERATIONS is the brand name for LAMFIX LTD, a company specializing in the import and export of all types of merchandise. This website provides a clean, business-oriented, and trustworthy online presence with a focus on global trade and reliability.

## Features

- **Modern Design**: Clean, professional design with acid yellow (#F5FF00) and black (#000000) color scheme
- **Responsive**: Mobile-friendly design that works on all devices
- **Three Pages**:
  - **Home**: Hero section with company introduction and feature highlights
  - **About Us**: Company mission, vision, core values, and expertise
  - **Contact Us**: Contact form and company contact information
- **Customizable Logo**: Logo can be easily replaced by updating `/static/images/logo.svg` or `/static/images/logo.png`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aouili-tn/oprtrade.com-django.git
cd oprtrade.com-django
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Open your browser and navigate to `http://localhost:8000`

## Customization

### Logo
Replace the logo by updating:
- `/static/images/logo.svg` (SVG format recommended)
- `/static/images/logo.png` (PNG format as fallback)

The logo should have dimensions approximately 200x60 pixels for optimal display.

### Colors
The color scheme can be customized in `/static/css/style.css` by modifying the CSS variables:
```css
:root {
    --primary-color: #F5FF00;  /* Acid Yellow */
    --secondary-color: #000000; /* Black */
}
```

### Content
- Templates are located in `/website/templates/website/`
- Static files (CSS, images) are in `/static/`

## Technology Stack

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL for production)

## Production Deployment

Before deploying to production:

1. Update `SECRET_KEY` in `tradeops/settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS`
4. Set up a production database (PostgreSQL recommended)
5. Configure static files serving
6. Set up HTTPS/SSL certificates

## License

Copyright © 2026 LAMFIX LTD. All rights reserved.
