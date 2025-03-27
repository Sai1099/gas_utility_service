# gas_utility_service

# Gas Utility Service

## Overview
This is a Django-based web application designed for managing gas utility services. It provides features for customer support, request management, and seamless database operations using MongoDB.

## Features
- **User Authentication**: Secure user login and authentication.
- **Support Requests**: Users can submit support requests.
- **Request Management**: Admins can manage service requests efficiently.
- **MongoDB Integration**: The system uses MongoDB as the backend database for scalability.

## Installation
### Prerequisites
Ensure you have Python 3.10+ installed on your system.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/gas-utility-service.git
   cd gas-utility-service
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the environment variables:
   - Create a `.env` file in the project root.
   - Add MongoDB connection details and other configurations.

5. Run database migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the server:
   ```sh
   python manage.py runserver
   ```
7. Open your browser and visit `http://127.0.0.1:8000/`

## API Endpoints
| Endpoint                | Method | Description               |
|-------------------------|--------|---------------------------|
| `/support/submit/`      | POST   | Submit a support request  |
| `/support/requests/`    | GET    | List all requests         |
| `/support/request/<id>` | GET    | Retrieve request details  |

## Project Structure
```
Gas_Utility_Service/
│-- gas_utility/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│-- support/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│-- templates/
│-- static/
│-- manage.py
│-- requirements.txt
│-- README.md
```

## Requirements
### `requirements.txt`
```txt
Django==4.2
djangorestframework==3.14.0
pymongo==4.5.0
dnspython==2.3.0
python-dotenv==1.0.0
```

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

---
**Happy Coding! 🚀**

