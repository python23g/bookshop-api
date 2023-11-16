# bookshop

## API docs

### Endpoints

cutomer table

1. create customer - `api/v1/customers/`
2. delete customer by pk - `api/v1/customers/{id}/`
3. update customer by pk - `api/v1/customers/{id}/`
4. get customer by pk - `api/v1/customers/{id}/`
5. get customers - `api/v1/customers/`

contact table

1. create customer's contact - `api/v1/customers/{id}/contact/`
2. delete customer's contact - `api/v1/customers/{id}/contact/`
3. update customer's contact - `api/v1/customers/{id}/contact/`
4. get customer's contact - `api/v1/customers/{id}/contact/`

publisher table

1. create publisher - `api/v1/publishers/`
2. delete publisher by pk - `api/v1/publishers/{id}/`
3. update publisher by pk - `api/v1/publishers/{id}/`
4. get publisher by pk - `api/v1/publishers/{id}/`
5. get publishes - `api/v1/publishers/`

language table

1. create language - `api/v1/languages/`
2. delete language by pk - `api/v1/languages/{id}/`
3. update language by pk - `api/v1/languages/{id}/`
4. get language by pk - `api/v1/languages/{id}/`
5. get languages - `api/v1/languages/`

book table

1. create book - `api/v1/books/`
2. delete book by pk - `api/v1/books/{id}/`
3. update book by pk - `api/v1/books/{id}/`
4. get book by pk - `api/v1/books/{id}/`
5. get books - `api/v1/books/`

## Database schema

customer

- id
- first_name
- last_name
- username
- password

contact

- id
- customer_id
- email
- address
- phone

publisher

- id
- name
- description

language

- id
- lang

author

- id
- first_name
- last_name
- bio

genre

- id 
- name

book

- id
- title
- description
- price
- quantity
- isbn
- languege FK
- pages
- publisher FK
- published_date 
- authors
- genres
