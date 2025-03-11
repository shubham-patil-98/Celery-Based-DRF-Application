# **Django Backend Application with Celery**

## **Overview**
This is a Django-based backend application with the following features:
- CRUD operations for Orders and Products using Django REST Framework.
- Customer authentication and token-based login.
- Signals when models are feched and saved using django signals
- Celery integration for background tasks and periodic task scheduling.
- Scheduled periodic tasks to update product data daily at 2:30 PM IST using `django-celery-beat`.

---

## **Features**
1. **Authentication**:
   - Token-based authentication using Django REST Framework's `TokenAuthentication`.

2. **CRUD APIs**:
   - Manage `Orders` and `Products` with full CRUD functionality.
   - Customers can only view their own orders.

3. **Background Tasks**:
   - Celery is used to process background tasks, such as importing product data from an Excel file.

---

## **Setup Instructions**

### **1. Clone the Repository**

git clone <repository-url>
cd <repository-directory>


### **2.  Install Dependencies**

python -m venv env
source env/bin/activate
pip install -r requirements.txt

#### **3. Apply Migrations**

python manage.py makemigrations
python manage.py migrate

### ^^4. Create a Superuser**

python manage.py createsuperuser

### **5. Start the Development Server**

python manage.py runserver

### **6. Start Redis**

Ensure Redis is installed and running:

redis-server

### **7. Start Celery Worker**

Run the Celery worker to process tasks:

celery -A ecommerce worker --loglevel=info

### **8. Start Celery Beat**

Run Celery Beat for periodic tasks:

celery -A ecommerce beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=info

File Path Argument:

["/home/<user>/Celery_App/ecommerce/uploads/Product_data.xlsx"]

Testing
1. Manual Task Testing

Run the task manually to test product import:

python manage.py shell

Inside the shell:

from orders.tasks import import_products_from_excel
import_products_from_excel.delay('/home/<user>/Celery_App/ecommerce/uploads/Product_data.xlsx')

2. API Testing

Use tools like Postman or cURL to test the APIs:

curl -X GET -H "Authorization: Token <your-token>" http://127.0.0.1:8000/api/orders/

License

This project is licensed under the MIT License.


---

Let me know if you need additional edits or have any other requests! 

