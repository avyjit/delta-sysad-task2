# Setup
To initialize the mess.txt serving and apache reverse proxy, run the initialze.sh script
```bash
$ chmod +x ./initialize.sh
$ ./initialize.sh
```

To start the database, pgadmin and the user details website
```bash
$ docker compose up --build
```

**Hostel and Mess Management Automation Checklist**

**Normal Mode:**

- [x] Dockerize the server setup from Task 1.
  - [x] Select an appropriate base image (e.g., Ubuntu) for the Docker container.
  - [x] Copy all the required scripts to their appropriate locations inside the Docker container.
  - [x] Set up and run the scripts inside the Docker container.

- [x] Display the mess file using Apache and proxy requests to the container.
  - [x] Configure Apache to serve files from the local directory of the Docker container.
  - [x] Set up a proxy to route requests from gamma-z.hm to the Docker container.
  - [x] Verify that opening gamma-z.hm displays the mess.txt file directly.

- [x] Store user details in a database instead of files.
  - [x] Create a database (MySQL or PostgreSQL) to store all user details.
  - [x] Use raw SQL queries to interact with the database (avoid ORMs like SQLAlchemy).
  - [x] Dockerize the database along with the server using docker-compose.

**SuperUser Mode:**

- [ ] Set up a cronjob for periodic database backups.
  - [ ] Configure a cronjob to run at 10:10 every three days of the month and on Sundays for May, June, and August.

- [x] Modify the Docker setup to preserve database data during restarts.
  - [x] Ensure that restarting Docker does not destroy the data stored in the database.

- [ ] Add PHPMyAdmin Docker service for viewing the database.
  - [ ] Set up a PHPMyAdmin Docker container to manage and view the database.
  - [ ] Create a read-only account in PHPMyAdmin to access user details in the database.

- [ ] Create a website for displaying user details based on permissions.
  - [ ] Choose a backend framework (PHP, Node.js-Express, or Flask) to create the website.
  - [ ] Implement a login feature using user ID and password.
  - [ ] Retrieve user permissions based on the logged-in user ID.
  - [ ] Implement access control:
    - [ ] HAD can see everyone's details.
    - [ ] Wardens can see details of their hostel's students only.
    - [ ] Students can see only their own details.

- [ ] Design the website frontend.
  - [ ] Create HTML and CSS templates for the website.
  - [ ] Optionally, use Bootstrap to simplify the CSS styling.

