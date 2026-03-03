# KeyShop Affiliate (Django)

## Local setup (Windows PowerShell)

```powershell
cd keyshop-affiliate
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Open:
- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## About data (Products / Affiliate links)

- This repo intentionally does **not** ship an active `db.sqlite3` in the root.
- If you already have an old database, put it back as `db.sqlite3` next to `manage.py`.
- A backup from your previous state is stored in `backup/db.sqlite3`.

### Export current products to JSON (backup)

```powershell
py manage.py dumpdata catalog --indent 2 > data.json
```

### Import products from JSON

```powershell
py manage.py loaddata data.json
```

## Deploy (Render)

Set these environment variables on Render:
- `SECRET_KEY`
- `DEBUG=False`
- `DATABASE_URL` (Render provides this if you attach Postgres)

Run commands:
- Build: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- Start: `gunicorn config.wsgi:application`
