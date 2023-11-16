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
| `/api/books/`               | GET    | Get a list of all books                          |
| `/api/books/{book_id}/`     | GET    | Get details of a specific book                   |
| `/api/books/`               | POST   | Create a new book                                |
| `/api/books/{book_id}/`     | PUT    | Update details of a specific book                |
| `/api/books/{book_id}/`     | DELETE | Delete a specific book                           |

### Orders

| Endpoint                    | Method | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| `/api/orders/`              | GET    | Get a list of all orders                         |
| `/api/orders/{order_id}/`   | GET    | Get details of a specific order                  |
| `/api/orders/`              | POST   | Place a new order                                |
| `/api/orders/{order_id}/`   | PUT    | Update details of a specific order               |
| `/api/orders/{order_id}/`   | DELETE | Cancel a specific order                          |

### Payments

| Endpoint                    | Method | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| `/api/payments/`            | GET    | Get a list of all payments                       |
| `/api/payments/{payment_id}/`| GET    | Get details of a specific payment                |
| `/api/payments/`            | POST   | Process a new payment                            |
| `/api/payments/{payment_id}/`| PUT    | Update details of a specific payment             |
| `/api/payments/{payment_id}/`| DELETE | Cancel a specific payment                        |

### Reviews

| Endpoint                       | Method | Description                                      |
|--------------------------------|--------|--------------------------------------------------|
| `/api/books/{book_id}/reviews/` | GET    | Get reviews for a specific book                  |
| `/api/books/{book_id}/reviews/` | POST   | Add a review for a specific book                 |
| `/api/reviews/{review_id}/`     | GET    | Get details of a specific review                 |
| `/api/reviews/{review_id}/`     | PUT    | Update details of a specific review              |
| `/api/reviews/{review_id}/`     | DELETE | Delete a specific review                         |

### Users

| Endpoint                    | Method | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| `/api/users/`               | GET    | Get a list of all users                          |
| `/api/users/{user_id}/`     | GET    | Get details of a specific user                   |
| `/api/users/`               | POST   | Register a new user                              |
| `/api/users/{user_id}/`     | PUT    | Update details of a specific user                |
| `/api/users/{user_id}/`     | DELETE | Delete a specific user                           |

### Genres

| Endpoint                    | Method | Description                                      |
|-----------------------------|--------|--------------------------------------------------|
| `/api/genres/`              | GET    | Get a list of all genres                         |
| `/api/genres/`              | POST   | Create a new genre                               |
| `/api/genres/{genre_id}/`   | PUT    | Update details of a specific genre               |
| `/api/genres/{genre_id}/`   | DELETE | Delete a specific genre                          |

### Publishers

| Endpoint                       | Method | Description                                      |
|--------------------------------|--------|--------------------------------------------------|
| `/api/publishers/`              | GET    | Get a list of all publishers                     |
| `/api/publishers/`              | POST   | Create a new publisher                           |
| `/api/publishers/{publisher_id}/`| PUT    | Update details of a specific publisher           |
| `/api/publishers/{publisher_id}/`| DELETE | Delete a specific publisher                      |

### Languages

| Endpoint                     | Method | Description                                      |
|------------------------------|--------|--------------------------------------------------|
| `/api/languages/`            | GET    | Get a list of all languages                      |
| `/api/languages/`            | POST   | Create a new language                            |
| `/api/languages/{lang_id}/`  | PUT    | Update details of a specific language            |
| `/api/languages/{lang_id}/`  | DELETE | Delete a specific language                       |
