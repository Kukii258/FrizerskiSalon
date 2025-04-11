# 💇‍♀️ Hair Salon

A full-featured web application for a hair salon located in Križevci, Croatia — showcasing modern styles, products, and services for women, men, and children.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

## ✨ Features

- **Homepage** with salon notifications and featured sections.
- **Latest Haircuts**: Displays 4 recent women’s and kids’ hairstyles.
- **Featured Products**: Shows 4 recently added beauty/hair products.
- **Product Showcase**: A section with images and descriptions like advertisements.
- **About Page**: Learn more about the salon, its team, and their specialties (hair, makeup, etc.).
- **Gallery Pages**:
  - Women’s Haircuts
  - Men’s Haircuts
  - Kids’ Haircuts
  - Full product gallery

---

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Deployment**: Dokku-ready setup (great for Heroku-like self-hosting)

---

## 🚀 Local Development

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Type Checking

```bash
mypy salon_jelena
```

### Run Tests

```bash
pytest
```

### Coverage Report

```bash
coverage run -m pytest
coverage html
open htmlcov/index.html
```

---

## ⚙️ Background Jobs with Celery

Start the worker:

```bash
cd salon_jelena
celery -A config.celery_app worker -l info
```

Start the beat scheduler:

```bash
cd salon_jelena
celery -A config.celery_app beat
```

---

## 📦 Deployment

This app is ready for **Dokku** deployment. It can also be adapted to platforms like Heroku.

For Heroku, see [Cookiecutter Django Heroku Docs](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-on-heroku.html).

---


## 🙋 About the Team

**Salon Jelena** is operated by a team of professionals offering:
- Hair styling for women, men, and children
- Makeup services
- Personalized beauty consultations

---

## 📬 Contact

For questions, suggestions, or appointments:
- Location: Križevci, Croatia

---

## 📄 License

This project is licensed under the MIT License.
