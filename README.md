# Visions Tech Website (Django)

Company website built with Django, bilingual EN/AR content, brand-aligned design, and animated sections.

## Tech Stack

- Python 3.12+
- Django 5
- WhiteNoise (static files)
- Gunicorn (production app server)
- Optional PostgreSQL via `DATABASE_URL`

## Local Run

1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run migrations:
   - `python manage.py migrate`
4. Start server:
   - `python manage.py runserver`
5. Open:
   - `http://127.0.0.1:8000/`

## Project Structure

- `hasan_test/` - Django project settings and root URLs
- `website/` - App views, URLs, templates, static files
- `website/templates/website/` - Page templates
- `website/static/website/` - CSS, JS, logo/images

## Environment Variables

Use `.env.example` as reference:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL` (optional for production, recommended)

## Production Readiness Included

- Env-based settings in `hasan_test/settings.py`
- `WhiteNoise` for static file serving
- `Procfile` for Gunicorn start
- `build.sh` for `collectstatic` + `migrate`
- `.gitignore` for local/sensitive files

## Deploy Recommendation

Recommended: **Render (app + PostgreSQL)** with **GoDaddy DNS**.

1. Push this repo to GitHub.
2. Create PostgreSQL in Render and copy `DATABASE_URL`.
3. Create Render Web Service from GitHub repo.
4. Build command:
   - `chmod +x build.sh && ./build.sh`
5. Start command:
   - `gunicorn hasan_test.wsgi:application --bind 0.0.0.0:$PORT`
6. Set environment variables in Render.
7. Point GoDaddy DNS:
   - `www` CNAME -> Render hostname
   - apex/root `@` -> forwarding or provider-recommended records

## Before First Public Launch

- Set `DJANGO_DEBUG=false`
- Set strong `DJANGO_SECRET_KEY`
- Configure `DJANGO_ALLOWED_HOSTS` for your domain
- Configure `DJANGO_CSRF_TRUSTED_ORIGINS` with `https://` domains
- Create admin user:
  - `python manage.py createsuperuser`

