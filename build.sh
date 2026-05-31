#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
if [ -n "${DATABASE_URL:-}" ]; then
  if ! python manage.py migrate --no-input; then
    echo "WARNING: migrate failed (database suspended or unreachable). Continuing build."
  fi
else
  echo "DATABASE_URL not set; skipping migrate."
fi
