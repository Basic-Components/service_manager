from pathlib import Path
DEFAULT_SETTING = {
    "ACCESS_LOG": True,
    'DEBUG': True,
    'HOST': '0.0.0.0',
    'SECRET_KEY': 'some secret words',
    'PORT': 5000,
    "JSON_AS_ASCII": False,
    "DB_URL": "postgresext+pool+async://postgres:postgres@localhost:5432/postgres",
    "WORKER": 4,
    "SET_LOG_FMT": "json",
    "SET_LOG_MAIL_LOG": False,
    "TEMPLATE_PATH": str(Path("./templates").absolute()),
    "STATIC_FOLDER": str(Path("./static").absolute()),
    "WEBSOCKET": True
}
