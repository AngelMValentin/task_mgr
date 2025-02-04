
# This environment variable tell Flask how to find you app ( so it can run it)
export FLASK_APP=app/routes.py
# This environment variable sets your environment to development, which enhances debug mode
export FLASK_ENV=development
# This enables debug mode, which will also trigger "auto-reload" (the server restarts when you save changes )
export FLASK_DEBUg=1

flask run