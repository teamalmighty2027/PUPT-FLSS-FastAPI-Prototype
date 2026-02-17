# PUPT-FLSS-FastAPI-Prototype
FastAPI based backend prototype for PUPT-FLSS

## How to Run

### Development
``` python
fastapi dev app/main.py --port 5000
```

### Production
``` python
fastapi run app/main.py
```

## Project Structure
```
.
├── app                  # "app" is a Python package
│   └── db               # "database" is a "Python subpackage"
│   |   ├── __init__.py  # makes "database" a "Python subpackage"
│   |   └── base.py      # "base" file that connects to the database
|   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  #  makes "routers" a "Python subpackage"
│   │   ├── auth/        # "auth" subfolder
│   │   └── ...          # other subfolder for related routes
|   └── models           # contains database models
|   └── services         # "services" is a "Python subpackage", contains logic
│   |   ├── __init__.py  # makes "services" a "Python subpackage"
|   └── security         # "security" is a "Python subpackage"
│   |   ├── __init__.py  # makes "security" a "Python subpackage"
│   ├── __init__.py      # this file makes "app" a "Python package"
|   ├── config.py        # "config" module, imports settings from .env
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── main.py          # "main" module, e.g. import app.main
└── README.md
```