# Deployment Guide for TRADE OPERATIONS Website

## Overview
This guide provides instructions for deploying the TRADE OPERATIONS Django website to production.

## Pre-Deployment Checklist

### 1. Security Configuration
- [ ] Generate a new SECRET_KEY for production
  ```python
  # In settings.py
  import os
  SECRET_KEY = os.environ.get('SECRET_KEY')
  ```
- [ ] Set `DEBUG = False` in production settings
- [ ] Configure `ALLOWED_HOSTS` with your domain(s)
  ```python
  ALLOWED_HOSTS = ['tradeoperations.com', 'www.tradeoperations.com']
  ```

### 2. Database Configuration
- [ ] Set up production database (PostgreSQL recommended)
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': os.environ.get('DB_NAME'),
          'USER': os.environ.get('DB_USER'),
          'PASSWORD': os.environ.get('DB_PASSWORD'),
          'HOST': os.environ.get('DB_HOST'),
          'PORT': os.environ.get('DB_PORT', '5432'),
      }
  }
  ```

### 3. Static Files
- [ ] Configure static files for production
  ```bash
  python manage.py collectstatic
  ```
- [ ] Set up a CDN or configure web server to serve static files

### 4. Media Files (for logo customization)
- [ ] Configure media files storage
- [ ] Set up backup for uploaded files

### 5. SSL/HTTPS
- [ ] Obtain SSL certificate
- [ ] Configure HTTPS redirect
- [ ] Enable secure cookies:
  ```python
  SECURE_SSL_REDIRECT = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True
  ```

### 6. Email Configuration (for contact form)
- [ ] Configure email backend
  ```python
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = os.environ.get('EMAIL_HOST')
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True
  EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
  EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
  ```

## Deployment Steps

### Option 1: Deploy to Heroku
```bash
# Install Heroku CLI and login
heroku login

# Create Heroku app
heroku create tradeoperations

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Collect static files
heroku run python manage.py collectstatic --noinput
```

### Option 2: Deploy to VPS (Ubuntu/Nginx/Gunicorn)
```bash
# Install dependencies
sudo apt update
sudo apt install python3-pip python3-venv nginx

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# Configure Gunicorn
gunicorn --bind 0.0.0.0:8000 tradeops.wsgi

# Set up Nginx as reverse proxy
# Configure systemd service for Gunicorn
```

### Option 3: Deploy to AWS/DigitalOcean
Follow provider-specific documentation for Django deployments.

## Post-Deployment

### 1. Testing
- [ ] Test all pages load correctly
- [ ] Test contact form submission
- [ ] Test mobile responsiveness
- [ ] Verify SSL certificate
- [ ] Check all links work

### 2. Monitoring
- [ ] Set up error logging (Sentry recommended)
- [ ] Configure uptime monitoring
- [ ] Set up analytics (Google Analytics)

### 3. Backup
- [ ] Configure database backups
- [ ] Set up media files backup

## Logo Customization

To customize the logo in production:

1. Prepare your logo in both SVG and PNG formats
   - Recommended size: 200x60 pixels
   - SVG format preferred for scalability

2. Upload files to:
   - `/static/images/logo.svg`
   - `/static/images/logo.png`

3. Run collectstatic:
   ```bash
   python manage.py collectstatic
   ```

## Environment Variables

Create a `.env` file (never commit this):
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=tradeoperations.com,www.tradeoperations.com
DB_NAME=tradeops_db
DB_USER=tradeops_user
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=info@tradeoperations.com
EMAIL_HOST_PASSWORD=your-email-password
```

## Support

For deployment assistance, refer to:
- Django deployment checklist: https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
- Django deployment documentation: https://docs.djangoproject.com/en/4.2/howto/deployment/

---
**TRADE OPERATIONS** - A LAMFIX LTD Company
