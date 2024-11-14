# Gas Utility Service Request Portal

A Django-based web application for managing customer service requests in a gas utility company. This application allows customers to submit service requests and track their status.

## Project Overview

This application helps streamline the process of handling customer service requests by providing:
- Online service request submission
- Request tracking system
- File attachment capabilities
- Status updates and timeline tracking

## Project Structure

gas_utility/
│
├── gas_utility/                 # Main project directory
│   ├── __init__.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── customer_service/           # Main application directory
│   ├── __init__.py
│   ├── admin.py               # Admin interface configuration
│   ├── apps.py                # App configuration
│   ├── models.py              # Database models (service requests)
│   ├── forms.py               # Form for service request submission
│   ├── views.py               # View functions
│   ├── urls.py                # App-specific URLs
│   └── templates/             # HTML templates
│       └── customer_service/
│           ├── request_form.html      # Form to submit request
│           ├── request_list.html      # List of all requests
│           └── request_detail.html    # Details of a specific request
│
├── static/                    # Static files (CSS, JS)
│   └── css/
│       └── style.css
│
├── media/                     # For uploaded files
│   └── service_requests/      # Attachments storage
│
├── manage.py
└── requirements.txt           # Project dependencies


## Features

### For Customers
- Submit service requests online
- Select request types (Gas Leak, New Connection, etc.)
- Attach supporting documents
- Track request status
- View request history and details

### For Staff (Admin Interface)
- Manage service requests
- Update request status
- Add comments to requests
- View and download attachments

## Technology Stack

- Python 3.7+
- Django 3.2
- SQLite (Database)
- Bootstrap 5 (Frontend)

## Installation

1. Clone the repository:
git clone https://github.com/Vaibhavbasidoni/Gas-Utility-Portal.git
cd gas_utility


2. Install required packages:
pip install -r requirements.txt


3. Apply database migrations:
python manage.py makemigrations
python manage.py migrate


4. Create a superuser (for admin access):
python manage.py createsuperuser

5. Run the development server:
python manage.py runserver


## Usage

### Customer Portal
- Access the portal at: `http://localhost:8000/`
- Submit new request: Click "Submit New Request"
- View requests: Available on the homepage
- Track request: Click on any request to view details

### Admin Interface
- Access admin panel at: `http://localhost:8000/admin/`
- Login with superuser credentials
- Manage requests, update status, and add comments

## Models

### ServiceRequest
- customer_name: Customer's name
- customer_email: Customer's email
- request_type: Type of service request
- description: Request details
- attachment: Optional file attachment
- status: Current status (Pending/In Progress/Resolved/Closed)
- created_at: Submission timestamp
- updated_at: Last update timestamp
- resolved_at: Resolution timestamp

### RequestComment
- service_request: Related service request
- staff_name: Name of staff member
- comment: Staff comment
- created_at: Comment timestamp

## File Structure Details

### Main Project Files
- `settings.py`: Project configuration and settings
- `urls.py`: Main URL routing configuration

### Application Files
- `models.py`: Database schema definitions
- `views.py`: View logic and request handling
- `forms.py`: Form definitions for data input
- `admin.py`: Admin interface customization

### Templates
- `request_form.html`: Service request submission form
- `request_list.html`: List of all service requests
- `request_detail.html`: Detailed view of a service request

