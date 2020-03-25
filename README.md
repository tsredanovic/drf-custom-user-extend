# Custom users using Django REST framework

- Custom User model set with an email address as the primary identifier.
- API endpoints for the custom User.
- Django admin for the custom User.
- Swagger documentation.

## Init project

```bash
python3 -m venv ./venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

## Run project

```bash
source venv/bin/activate
python manage.py runserver
```

## Swagger

http://localhost:8000/swagger/

## User

- Registration: POST http://localhost:8000/api/v1/registration/
  ```json
  {
    "email": "test@test.com",
    "password1": "ujmik,ol.",
    "password2": "ujmik,ol."
  }
  ```
  - sends email containing verification key

- Email verification: POST http://localhost:8000/api/v1/registration/verify-email/
  ```json
  {
    "key": "MjU:1jH4oH:d8z_aLgQeKL5wY5UJFNTs2RpmeY"
  }
  ```

- Log in: POST http://localhost:8000/api/v1/login/
  ```json
  {
    "email": "test@test.com",
    "password": "ujmik,ol."
  }
  ```

- Current user interaction: GET, PUT, PATCH http://localhost:8000/api/v1/user/

- Log out: POST http://localhost:8000/api/v1/logout/

- Password change: POST http://localhost:8000/api/v1/password/change/
  ```json
  {
    "new_password1": ".lo,kimju",
    "new_password2": ".lo,kimju"
  }
  ```

- Password reset: POST http://localhost:8000/api/v1/password/reset/
  ```json
  {
    "email": "test@test.com"
  }
  ```
  - sends email containing user's uid and password reset token

- Password reset confirmation: POST http://localhost:8000/api/v1/password/reset/confirm/
  ```json
  {
    "new_password1": ".lo,kimju",
    "new_password2": ".lo,kimju",
    "uid": "OA",
    "token": "5f3-bc905e96b7be9d31e5ac"
  }
  ```
