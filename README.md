First Steps


To create a virtual environment inside Python (this is so that the changes we make to Python do not damage the main Python of the operating system and cause some things to crash):
`$ python -m venv 'virt'`

Then we enter this virtual environment using the source command:
`$ source \bin activate`

We also need to install mysql and django via pip:
`$ pip install django`
`$ pip install mysql`

If you get an error downloading mysql, the solution I use is
`$  sudo apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential`

Also install the connector specifically for mysql
`$  pip install mysql-connector-python`
`$  pip install mysql-connector`

==*check 'MySql Command' for Errors and failure*==


We migrate so that all the tables required by Django are implemented on our created database.
`$  python manage.py migrate`

Then we create a superuser.
`$  python manage.py createsuperuser`

And finally we run the server.
`$  python manage.py runserver`

If the Django welcome page appears by going to the given address "127.0.0.1:8000", it means that everything is working properly and the first step is complete!

===============================================================


mysql section:

`CREATE DATABASE <database_name>;`

## How to Create New MySQL User

```
sudo mysql -u root -p
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
```
## How to Grant Permissions in MySQL

**All databases**

```
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
```

**All tables in a specific database**

```
GRANT ALL PRIVILEGES ON database_name.* TO 'username''@'localhost';
```

**Specific table**

```
GRANT ALL PRIVILEGES ON database_name.table_name TO 'username'@'localhost';
```

 Verify that the user has been granted the new privileges:

```
SHOW GRANTS FOR 'username'@'localhost';
```

### Grant Delete Privileges

**All databases**

```
GRANT DELETE ON *.* TO 'username'@'localhost';
```

**All tables in a specific database**

```
GRANT DELETE ON database_name.* TO 'username''@'localhost';
```

**Specific table**

```
GRANT DELETE ON database_name.table_name TO 'username'@'localhost';
```

CRM panel look like this at the end:
![Pasted image 20241217042041](https://github.com/user-attachments/assets/94ac363b-0bd6-46b0-888f-58a28501044d)

**Show TABLES**
USE <database_name>; 
SHOW TABLES


