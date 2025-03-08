import os

# Set a secure secret key (generate a new one using: openssl rand -hex 32)
SECRET_KEY = "i63X/c0sUnekrn2EjLBoQ5vEfxyo3ThExnZn4ST3epU1xhXVu2dFDASQ"

# Default database for metadata storage (SQLite, change to PostgreSQL later)SQLALCHEMY_DATABASE_URI = "sqlite:///~/.superset/superset.db"

# Enable or disable features
FEATURE_FLAGS = {
    "DASHBOARD_CROSS_FILTERS": True,
}

# Allow connections to external databases
ENABLE_PROXY_FIX = True

SQLALCHEMY_DATABASE_URI = postgresql://superset_user:bNWINYk7Y7C6THcC7QFSefQO6ihIYoYE@dpg-cv62cjl6l47c73d3bbjg-a/superset_db_jeaf
