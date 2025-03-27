# gas_utility_service

# Gas Utility Service

## Overview
This is a Django-based backend service for a **Gas Utility Management System**. It includes modules for managing customers, handling support requests, and sending notifications. MongoDB is used as the database.

## Features
- **Customers Module**: Manage customer profiles and gas service details.
- **Support Module**: Handle support requests and issue tracking.
- **Notifications Module**: Send real-time notifications to users.

---

## Installation

### Prerequisites
- Python 3.10+
- MongoDB
- Django
- Virtual Environment (optional but recommended)

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/gas-utility-service.git
   cd gas-utility-service
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**
   - Ensure MongoDB is running.
   - Update your `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'djongo',
             'NAME': 'gas_utility_db',
         }
     }
     ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the server**
   ```bash
   python manage.py runserver
   ```

---

## Modules

### 1️⃣ Customers Module
- **API Endpoints**
  - `POST /customers/create/` → Create a new customer.
  - `GET /customers/` → Get all customers.
  - `GET /customers/<id>/` → Retrieve customer details.
  - `PUT /customers/<id>/update/` → Update customer data.
  - `DELETE /customers/<id>/delete/` → Delete a customer.

- **Model Structure**
  ```python
  class Customer(models.Model):
      customer_id = models.CharField(max_length=100, unique=True)
      name = models.CharField(max_length=255)
      address = models.TextField()
      email = models.EmailField()
      phone = models.CharField(max_length=15)
      connection_status = models.BooleanField(default=True)
  ```

### 2️⃣ Support Module
- **API Endpoints**
  - `POST /support/submit/` → Submit a support request.
  - `GET /support/requests/` → List all requests.
  - `PUT /support/<id>/update/` → Update a request.
  - `DELETE /support/<id>/delete/` → Delete a request.

- **Model Structure**
  ```python
  class SupportRequest(models.Model):
      request_id = models.CharField(max_length=100, unique=True)
      customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
      issue_description = models.TextField()
      status = models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open')
  ```

### 3️⃣ Notifications Module
- **API Endpoints**
  - `POST /notifications/send/` → Send a notification.
  - `GET /notifications/` → Retrieve notifications.

- **Model Structure**
  ```python
  class Notification(models.Model):
      notification_id = models.CharField(max_length=100, unique=True)
      recipient = models.ForeignKey(Customer, on_delete=models.CASCADE)
      message = models.TextField()
      timestamp = models.DateTimeField(auto_now_add=True)
  ```

---

## Running Tests
Run the test suite to ensure everything works fine:
```bash
python manage.py test
```

---

## API Documentation
For a detailed API reference, use **Swagger**:
```bash
pip install drf-yasg
```
Then, visit:
- `http://127.0.0.1:8000/swagger/`

---



## License
This project is licensed under the MIT License.

