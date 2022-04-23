# auto reminder

This simple app sends email with remind that somene should give you back some item

items are stored in sqlite database

## run

To run this app you should clone this repository and create .env file, in project root directory, based on .env.example file. File contains credentials to your smtp mail server

next run folow instructions:

```
pip install -r requirements.txt
python3 database_setup.py
```

if you wont add som dummy data to your database run:
```
python3 database_add_fixtures.py
```

Finaly to send emails with reminds run:
```
python3 auto_reminder.py
```

if you want regulary send emails with reminds you can add tis script to your crontab

---
project inspired by [pycamp.pl](https://www.pycamp.pl/)
