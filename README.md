# Django + Stripe Payment

## About

This project is a simple Django application integrated with Stripe.
It allows viewing a product and paying for it using Stripe Checkout (test mode).

The main part of the task is implemented according to the requirements, and a few additional features were also added.

---

## Live Demo

https://payment-task.onrender.com/item/1

---

## Admin Panel

https://payment-task.onrender.com/admin/

login: admin
password: 123

---

## Functionality

### Main

* Django model `Item` (name, description, price)
* Endpoint `/buy/<id>/` that creates a Stripe Checkout session
* Endpoint `/item/<id>/` that renders a simple HTML page
* Buy button redirects to Stripe Checkout

---

### Additional

* Docker setup
* Environment variables
* Deployment on Render
* Django Admin for managing data
* Order model (multiple items in one payment)
* Discount and Tax support
* Currency field for items
* PaymentIntent endpoint
* Basic unit tests

---

## Run locally

```bash
git clone <repo_url>
cd project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Environment variables

Create a `.env` file in the root:

```
SECRET_KEY=your_secret_key
DEBUG=True

STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...

DOMAIN=http://127.0.0.1:8000
```

---

## Docker

```bash
docker-compose up --build
```

---

## Stripe test card

```
4242 4242 4242 4242
Any future date
Any CVC
```

---

## Notes

* Stripe is used in test mode
* SQLite database is used
* On free hosting the database may reset
* Additional endpoints (order, payment intent) are implemented separately and do not affect the main flow
