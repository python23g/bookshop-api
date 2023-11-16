# bookshop

## project file structure

```bash
├── manage.py
└── core
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
└── apps
    ├── __init__.py
    └── books
        ├── __init__.py
        └── migrations
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
    └── orders
        ├── __init__.py
        └── migrations
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
    └── payments
        ├── __init__.py
        └── migrations
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
    └── reviews
        ├── __init__.py
        └── migrations
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
    └── users
        ├── __init__.py
        └── migrations
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
```

## Database schema

### User

- id
- username
- email
- password
- first_name
- last_name

### Order

- id
- user FK
- order_date
- total_price
- status

### OrderItem

- id
- order FK
- book FK
- quantity
- unit_price

### Payment

- id
- order FK
- payment_date
- amount
- payment_method

### Review

- id
- user FK
- book FK
- rating
- comment
- review_date

### BookAuthor (Many-to-Many Relationship Table)

- id
- book FK
- author FK

### BookGenre (Many-to-Many Relationship Table)

- id
- book FK
- genre FK

## API endpoints

| Endpoint                      | Method | Description                                      |
|-------------------------------|--------|--------------------------------------------------|
| `/api/v1/books/`                 | GET    | Get a list of all books                          |
| `/api/v1/books/{book_id}/`       | GET    | Get details of a specific book                   |
| `/api/v1/books/{book_id}/reviews/` | GET    | Get reviews for a specific book                 |
| `/api/v1/orders/`                | GET    | Get a list of all orders                         |
| `/api/v1/orders/{order_id}/`     | GET    | Get details of a specific order                  |
| `/api/v1/orders/`                | POST   | Place a new order                                |
| `/api/v1/orders/{order_id}/items/` | GET    | Get items in a specific order                   |
| `/api/v1/payments/`              | GET    | Get a list of all payments                       |
| `/api/v1/payments/{payment_id}/` | GET    | Get details of a specific payment                |
| `/api/v1/books/{book_id}/reviews/` | POST   | Add a review for a specific book                |
| `/api/v1/users/{user_id}/reviews/` | GET    | Get reviews posted by a specific user            |
| `/api/v1/users/{user_id}/orders/`  | GET    | Get orders placed by a specific user             |
