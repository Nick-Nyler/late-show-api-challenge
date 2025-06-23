# Late Show API

A Flask REST API for managing a Late Night TV show system with guests, episodes, and appearances.

## Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/<username>/late-show-api-challenge.git
cd late-show-api-challenge
```

2. **Install Dependencies**
```bash
pipenv install
pipenv shell
```

3. **Setup PostgreSQL Database**
```bash
psql -c "CREATE DATABASE late_show_db;"
```

4. **Configure Environment Variables**
Create a `.env` file in the root directory:
```bash
DATABASE_URI=postgresql://<user>:<password>@localhost:5432/late_show_db
JWT_SECRET_KEY=your-secret-key
```

5. **Run Database Migrations and Seed**
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

6. **Run the Application**
```bash
python server/app.py
```

## Authentication Flow

1. Register a new user:
```bash
POST /register
Content-Type: application/json
{
    "username": "your_username",
    "password": "your_password"
}
```

2. Login to get JWT token:
```bash
POST /login
Content-Type: application/json
{
    "username": "your_username",
    "password": "your_password"
}
```

3. Use token in protected routes:
```bash
Authorization: Bearer <your_jwt_token>
```

## API Routes

| Route | Method | Auth Required | Description |
|-------|--------|---------------|-------------|
| /register | POST | No | Register a new user |
| /login | POST | No | Login and get JWT token |
| /episodes | GET | No | List all episodes |
| /episodes/<id> | GET | No | Get episode details with appearances |
| /episodes/<id> | DELETE | Yes | Delete episode and its appearances |
| /guests | GET | No | List all guests |
| /appearances | POST | Yes | Create a new appearance |

### Sample Request/Response

**POST /appearances**
Request:
```json
{
    "rating": 4,
    "guest_id": 1,
    "episode_id": 1
}
```
Response:
```json
{
    "id": 1,
    "rating": 4,
    "guest_id": 1,
    "episode_id": 1
}
```

## Postman Testing

1. Import `challenge-4-lateshow.postman_collection.json` into Postman
2. Test all routes:
   - Register and login to get JWT token
   - Use token in Authorization header for protected routes
   - Test all endpoints with appropriate request bodies

## GitHub Repository
[late-show-api-challenge](https://github.com/<username>/late-show-api-challenge)
```

# .gitignore
```
__pycache__/
*.pyc
*.db
.env
*.sqlite3
migrations/
Pipfile.lock
```

# challenge-4-lateshow.postman_collection.json
```json
{
    "info": {
        "name": "Late Show API",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    },
    "item": [
        {
            "name": "Register",
            "request": {
                "method": "POST",
                "header": [],
                "body": {
                    "mode": "raw",
                    "raw": "{\"username\": \"testuser\", \"password\": \"testpass\"}",
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": {
                    "raw": "{{baseUrl}}/register",
                    "host": ["{{baseUrl}}"],
                    "path": ["register"]
                }
            }
        },
        {
            "name": "Login",
            "request": {
                "method": "POST",
                "header": [],
                "body": {
                    "mode": "raw",
                    "raw": "{\"username\": \"testuser\", \"password\": \"testpass\"}",
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": {
                    "raw": "{{baseUrl}}/login",
                    "host": ["{{baseUrl}}"],
                    "path": ["login"]
                }
            }
        },
        {
            "name": "Get Episodes",
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "{{baseUrl}}/episodes",
                    "host": ["{{baseUrl}}"],
                    "path": ["episodes"]
                }
            }
        },
        {
            "name": "Get Episode",
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "{{baseUrl}}/episodes/1",
                    "host": ["{{baseUrl}}"],
                    "path": ["episodes", "1"]
                }
            }
        },
        {
            "name": "Delete Episode",
            "request": {
                "method": "DELETE",
                "header": [
                    {
                        "key": "Authorization",
                        "value": "Bearer {{token}}"
                    }
                ],
                "url": {
                    "raw": "{{baseUrl}}/episodes/1",
                    "host": ["{{baseUrl}}"],
                    "path": ["episodes", "1"]
                }
            }
        },
        {
            "name": "Get Guests",
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "{{baseUrl}}/guests",
                    "host": ["{{baseUrl}}"],
                    "path": ["guests"]
                }
            }
        },
        {
            "name": "Create Appearance",
            "request": {
                "method": "POST",
                "header": [
                    {
                        "key": "Authorization",
                        "value": "Bearer {{token}}"
                    }
                ],
                "body": {
                    "mode": "raw",
                    "raw": "{\"rating\": 4, \"guest_id\": 1, \"episode_id\": 1}",
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": {
                    "raw": "{{baseUrl}}/appearances",
                    "host": ["{{baseUrl}}"],
                    "path": ["appearances"]
                }
            }
        }
    ],
    "variable": [
        {
            "key": "baseUrl",
            "value": "http://localhost:5000"
        },
        {
            "key": "token",
            "value": ""
        }
    ]
}