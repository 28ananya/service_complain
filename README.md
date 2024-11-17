## Gas Utility Services Application
## Project Overview
The Gas Utility Services Application is a web-based platform designed to streamline the process of submitting and managing service requests for gas utilities. It provides a user-friendly interface for customers to:

Submit service requests online.
Track the status of their requests.
View account information.
Additionally, customer support representatives can manage these requests and provide timely support to customers.

## Features
Customer Features
## Service Requests:
Submit service requests with details and attachments.
Track the status of service requests (e.g., Pending, Resolved).
## Account Management:
Register and log in to access personalized services.
View and manage submitted service requests.

## clone the project

git clone "https://github.com/28ananya/service_complain.git "

## installation

pip install -r requirements.txt

## migrate

python manage.py migrate

## Run the Development Server
python manage.py runserver
## http://127.0.0.1:8000

## API END POINTS

API Endpoints
1. Login API (/accounts/login/)
Method: POST
Description: Logs in a user with their username and password.

2. Register API (/accounts/register/)
Method: POST
Description: Registers a new user account.

3. Logout API (/accounts/logout/)
Method: POST
Description: Logs out the authenticated user.

4. Home Page API (/)
Method: GET
Description: Displays the home page of the application.

5. Create Service Request API (/service-requests/create/)
Method: POST
Description: Allows a user to create a new service request.

6. List All Service Requests API (/service-requests/list/)
Method: GET
Description: Lists all service requests submitted by the logged-in user.

7. Service Request Details API (/service-requests/<int:pk>/)
Method: GET
Description: Fetches the details of a specific service request by ID.
