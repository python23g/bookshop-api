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

### Books

| Endpoint                    | Method | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| `/api/v1/books/`               | GET    | Get a list of all books                          |
| `/api/v1/books/{book_id}/`     | GET    | Get details of a specific book                   |
| `/api/v1/books/`               | POST   | Create a new book                                |
| `/api/v1/books/{book_id}/`     | PUT    | Update details of a specific book                |
| `/api/v1/books/{book_id}/`     | DELETE | Delete a specific book                           |

### Orders

| Endpoint                    | Method | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| `/api/v1/orders/`              | GET    | Get a list of all orders                         |
| `/api/v1/orders/{order_id}/`   | GET    | Get details of a specific order                  |
| `/api/v1/orders/`              | POST   | Place a new order                                |
| `/api/v1/orders/{order_id}/`   | PUT    | Update details of a specific order               |
| `/api/v1/orders/{order_id}/`   | DELETE | Cancel a specific order                          |

### Payments

| Endpoint                    | Method | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| `/api/v1/payments/`            | GET    | Get a list of all payments                       |
| `/api/v1/payments/{payment_id}/`| GET    | Get details of a specific payment                |
| `/api/v1/payments/`            | POST   | Process a new payment                            |
| `/api/v1/payments/{payment_id}/`| PUT    | Update details of a specific payment             |
| `/api/v1/payments/{payment_id}/`| DELETE | Cancel a specific payment                        |

### Reviews

| Endpoint                       | Method | Description                                      |
|--------------------------------|--------|--------------------------------------------------|
| `/api/v1/books/{book_id}/reviews/` | GET    | Get reviews for a specific book                  |
| `/api/v1/books/{book_id}/reviews/` | POST   | Add a review for a specific book                 |
| `/api/v1/reviews/{review_id}/`     | GET    | Get details of a specific review                 |
| `/api/v1/reviews/{review_id}/`     | PUT    | Update details of a specific review              |
| `/api/v1/reviews/{review_id}/`     | DELETE | Delete a specific review                         |

### Users

| Endpoint                    | Method | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| `/api/v1/users/`               | GET    | Get a list of all users                          |
| `/api/v1/users/{user_id}/`     | GET    | Get details of a specific user                   |
| `/api/v1/users/`               | POST   | Register a new user                              |
| `/api/v1/users/{user_id}/`     | PUT    | Update details of a specific user                |
| `/api/v1/users/{user_id}/`     | DELETE | Delete a specific user                           |

### Genres

| Endpoint                    | Method | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| `/api/v1/genres/`              | GET    | Get a list of all genres                         |
| `/api/v1/genres/`              | POST   | Create a new genre                               |
| `/api/v1/genres/{genre_id}/`   | PUT    | Update details of a specific genre               |
| `/api/v1/genres/{genre_id}/`   | DELETE | Delete a specific genre                          |

### Publishers

| Endpoint                       | Method | Description                                      |
|--------------------------------|--------|--------------------------------------------------|
| `/api/v1/publishers/`              | GET    | Get a list of all publishers                     |
| `/api/v1/publishers/`              | POST   | Create a new publisher                           |
| `/api/v1/publishers/{publisher_id}/`| PUT    | Update details of a specific publisher           |
| `/api/v1/publishers/{publisher_id}/`| DELETE | Delete a specific publisher                      |

### Languages

| Endpoint                     | Method | Description                                      |
|------------------------------|--------|--------------------------------------------------|
| `/api/v1/languages/`            | GET    | Get a list of all languages                      |
| `/api/v1/languages/`            | POST   | Create a new language                            |
| `/api/v1/languages/{lang_id}/`  | PUT    | Update details of a specific language            |
| `/api/v1/languages/{lang_id}/`  | DELETE | Delete a specific language                       |
