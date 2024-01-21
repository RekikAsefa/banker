## Project Title: SWIFT Connect Service

### Project Overview:

This project provides a seamless electronic onboarding process for Company A's SWIFT Connect service, enabling business customers to connect to the SWIFT network and facilitate SWIFT transfer operations within their platform.

### Access to wireframe

Follow this link [Wireframe](<https://www.figma.com/file/y0lkmRxvWhqbkXQ0pFv1YX/Wireframing-(Copy)?type=design&node-id=77%3A432&mode=design&t=Bswyh5vmpaNtjLsQ-1>) to see the wireframe.

### Installation and Setup:

1. **Install Python:**
   Ensure Python is installed on your system. If not, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Pipenv:**
   If Pipenv is not already installed on your system, install it by running:

   ```bash
   pip install pipenv
   ```

3. **Clone the Repository:**
   Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/bisratawoke/banker.git
   ```

4. **Install Packages:**
   Navigate to the project directory and install dependencies using Pipenv:

   ```bash
   pipenv install
   ```

5. **Create Virtual Environment:**
   Activate the virtual environment using:

   ```bash
   pipenv shell
   ```

6. **Create MySQL Database:**

   - Option 1: Manually create a MySQL database with root password 'password' and database name 'mybase'.
   - Option 2: Use Docker and Docker Compose to create a MySQL container:
     ```bash
     docker-compose up -d
     ```

7. **Apply Database Migrations:**
   Change directory to the 'application' folder and run:

   ```bash
   python manage.py migrate
   ```

8. **Create CRM Administrators:**
   Run the following command to create superuser accounts for CRM administrators:

   ```bash
   python manage.py createsuperuser
   ```

9. **Run the Development Server:**
   Start the development server by running:

   ```bash
   python manage.py runserver
   ```

10. **Access Admin Panel:**
    Visit [localhost:8000/admin](http://localhost:8000/admin) and log in with the superuser credentials created in step 8.

11. **Create Customer Service Representatives Group:**

    - Navigate to the 'Groups' section in the admin panel.
    - Create a group named 'Customer Service Representatives'.
    - Add all admin permissions and view/change permissions for 'Business Customer' and 'SWIFT Information' models.

12. **Access Application:**
    Visit [localhost:8000](http://localhost:8000) to log in or create an account as a business customer.
13. **Chat with Staff**
    **_ In order to chat with an admin you are expected to have created a super user and customer service representatives as indicated in steps 9 - 12 _**

    1. navigate to the [localhost:8000](http://localhost:8000) and click on the chat button on bottom right corner and write a message.

    2. head over to [localhost:8000](http://localhost:8000/admin) and login using superuser credentails or any staff member that you have created. click on the chat messages list then find the message with and respond by creating a new chat message and selecting the chat session. p.s dont forget to select the approprate user to sign the message as.

    3. head back to public facing portal and continue your chat

### Project Structure:

- **application/:** Contains the main Django application files.
- **docker-compose.yml:** Docker Compose configuration for MySQL database.
- **Pipefile:** List of Python dependencies.

### Additional Notes:

- Ensure Docker and Docker Compose are installed for the database container setup.
- For production deployment, customize database configurations and secret settings.
- Refer to the documentation for more detailed information on the project's features and functionalities.

Feel free to reach out if you encounter any issues or have questions related to the project. Happy coding!
