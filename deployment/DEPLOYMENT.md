# Deployment Guide for tradeopr.com

This guide explains how to deploy the **tradeops** Django project to an Ubuntu server using Gunicorn and Nginx with the generated configuration files.

## 1. Prerequisites

Ensure your Ubuntu server is up to date and has the following packages installed:

```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx git
```

## 2. User Setup

Create the `django` user to run the application:

```bash
sudo adduser --system --group --shell /bin/bash --home /home/django django
sudo usermod -aG sudo django
```

## 3. Project Setup

Switch to the `django` user and clone the repository (or copy the files):

```bash
sudo su - django
# Clone your repository here, for example:
# git clone <your-repo-url> tradeopr.com
# For this guide, we assume the project is located at:
# /home/django/tradeopr.com
```

Navigate to the project directory and set up the virtual environment:

```bash
cd /home/django/tradeopr.com
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

> **Note:** Ensure `gunicorn` is installed in your virtual environment.

## 4. Gunicorn/Systemd Setup

Exit the `django` user session (`exit`) to return to your root/sudo user.

Copy the systemd files from the `deployment` directory to `/etc/systemd/system/`:

```bash
# Assuming you are in the project root on the server
sudo cp deployment/gunicorn.socket /etc/systemd/system/
sudo cp deployment/gunicorn.service /etc/systemd/system/
```

Start and enable the Gunicorn socket:

```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

Check the status:

```bash
sudo systemctl status gunicorn.socket
```

## 5. Nginx Setup

Copy the Nginx configuration file to `/etc/nginx/sites-available/`:

```bash
sudo cp deployment/tradeopr.com /etc/nginx/sites-available/
```

Enable the site by linking it to `sites-enabled`:

```bash
sudo ln -s /etc/nginx/sites-available/tradeopr.com /etc/nginx/sites-enabled/
```

Test the Nginx configuration:

```bash
sudo nginx -t
```

If the test is successful, restart Nginx:

```bash
sudo systemctl restart nginx
```

## 6. Permissions

Ensure the `django` user has ownership of the project files, and Nginx (`www-data`) can access the static files if necessary (though the `gunicorn` group setting usually handles the socket, static files might need read permissions).

```bash
sudo chown -R django:django /home/django/tradeopr.com
```

## 7. Firewall (Optional)

If you have `ufw` enabled:

```bash
sudo ufw allow 'Nginx Full'
```
