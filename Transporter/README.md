# Transporter

## Architecture

![](https://i.imgur.com/gPySCmC.jpg)

## Database design

![](https://i.imgur.com/vBqqmqi.png)

## tldr

To make this project work in your machine, just follow those instructions:

1. Create a database and note its name. For this example, since the application is called "transporter", we'll call the database `transporter`.
2. In the root directory, ensure you have a file named exactly `env.json`, containing the details to connect to your database (password, username, etc.). Refer to the **Environment** section in this README for the correct format. You should also find a file called `env.backup`, which you can use as a reference to create your `env.json` file correctly.
3. Since this is your first time running the application, set the `WORKING_ENV` key in the `env.json` file to `dev`. This ensures that any existing tables in your database will not be deleted. If your database is not empty and you want a fresh start, set `WORKING_ENV` to `test`, which will delete all tables listed under the `MYSQL_DB` key in the `env.json` file.
4. To seed (populate the database with dummy data) your database with random data, follow the instructions in the **Seeding new data** section of this README.

#### Example:

```python
# seed.py
from db_seed import Seed

s = Seed()
s.up()
```

```bash
python3 seed.py
```

You can use the `db.Sql` file, which will create the database, all tables, and dummy data. In this case, the database will be named `transporter`, so ensure it is included in the `env.json` file.
```bash
sudo mysql -u`root` `db_name` < db.sql
```
## Environment

The file called `env.json` is the file contains all the database details, Be sure to check it out first and give it your database connection details.

This is it's structure:

```json
{
    "MYSQL_USER" : "root", /* User of your db */
    "MYSQL_PWD" : "root", /* password of your database */
    "MYSQL_HOST" : "localhost", /* host of your db */
    "MYSQL_DB" : "db_name",
    "WORKING_ENV" : "dev", /* 'dev' or 'test' */
    "API_HOST": "127.0.0.1",
    "API_PORT": "5000"
}
```

**WORKING_ENV** will be used by the application to decide the environment type (should it use a fresh database or the existing database).

> NOTE: Setting `WORKING_ENV` to `test` will Cause all the tables in the database `MYSQL_DB` to be **deleted**. 

## Seeding new data

To seed new data to the database, you can use the class `Seed` in the file `db_seed.py`, then create new instance and set the optional `reset` value to `True` if you want a fresh seeded database.

```python
from db_seed import Seed
s = Seed() 
# Set the optional value 'reset' to True to delete all the existing tables
```

To seed just a particular table you can call on of those functions:

```python
# Integers represent many rows that will be created
# All those integers are optional, there default value is 69
s.seed_cities_locations(12)
s.seed_customers(20)
s.seed_drivers(30)
s.seed_deliveries(15)
s.seed_ratings(14)
```

Or to seed all tables at once you do it like this:

```python
# All those arguments are optional, there default value is the some as the intgers that I sepesifiedd in this example
s.up(self, customers=2, drivers=3, deliveries=10, ratings=30)
```


