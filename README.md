# Research Assistant Backend

A backend service built with Django and Django REST Framework that receives research requests from users, selects the
appropriate external source, retrieves relevant information, and stores the execution process and final result.

---

## Features

- User authentication and authorization
- Create research requests
- View user's own research requests
- View research request details
- External tool integration:
    - GitHub REST API
    - Books to Scrape
- Request processing workflow tracking
- PostgreSQL database support
- API validation and error handling
- Pagination support
- Automated tests
- Docker support

---

# Technology Stack

- Python 3.12
- Django 6.1
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- BeautifulSoup4
- Requests

---

# Project Architecture

The project is divided into several main components:

ResearchAssistant/

├── accounts/
│ └── User authentication and authorization

├── inquiries/
│ └── Research request management
│ - Create requests
│ - Store results
│ - Track processing steps

├── tools/
│ └── External service integrations
│ - GitHub API client
│ - Books scraper
│ - Query processing logic

├── ResearchAssistant/
│ └── Django project configuration

├── Dockerfile
├── docker-compose.yml
└── requirements.txt

---

#### Each research request is processed through a workflow:

User Request
|

Request Processor
|

Tool Selection |

+------------+

GitHub Tool Books Tool
|

Result Storage

---

# Running Project

Install dependencies:
pip install -r requirements.txt

Apply migrations: python manage.py migrate

Run development server: python manage.py runserver

---

Running Tests

Run all tests: python manage.py test

Run tests for a specific app: python manage.py test accounts