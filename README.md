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
To populate the db with data from studentDetails.txt, run the `dbscript.py` script
```bash
$ python3 ./dbscript.py
```

To add a cronjob for the db backup, run 
```bash
$ ./cronjob.sh
```

**Hostel and Mess Management Automation Checklist**

**Normal Mode:**

- [x] Dockerize the server setup from Task 1.
- [x] Display the mess file using Apache and proxy requests to the container.
- [x] Store user details in a database instead of files.
**SuperUser Mode:**

- [x] Set up a cronjob for periodic database backups.
- [x] Modify the Docker setup to preserve database data during restarts.
- [x] Add PHPMyAdmin Docker service for viewing the database.
- [x] Create a website for displaying user details based on permissions.
- [x] Design the website frontend.

