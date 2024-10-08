			
![](https://i.imgur.com/wNevAVO.png)
# ORM?

Object Relational Mapping (ORM) is a technique used in creating a "bridge" between object-oriented programs and, in most cases, relational databases.

An ORM tool is software designed to help OOP developers interact with relational databases. So instead of creating your own ORM software from scratch, you can make use of these tools.

## Making the engine

`create_engine` is a function used to create a connection to the database. It takes a database URL as an argument and returns an Engine instance. The Engine represents the core interface to the database, providing methods for executing SQL statements and managing connections.


```python
from sqlalchemy import create_engine

engine = create_engine('URL')
```

### Wait URL, what? where?

URL is just a string formatting providing a way to give the instance engine the data that will use to connect to Database, and it is as simple as this:

```
dialect+driver://username:password@host:port/database
```

- **Dialect:**  Name of the SQLAlchemy dialect, a name such as `sqlite`, `mysql`, `postgresql`, `oracle`, or `mssql`.
- **Driver:** Usually it's optional as alchemy tries its best to include the default DBAPI (if it available) - this default is typically the most widely known driver available for that backend. in my case using the default wasn't working because it wasn't available in my system, so the solution was one of those:
	- **Specify a different driver:** an alternative driver may already be installed on your system but isn't the default one used by SQLAlchemy. **mysqlconnector** driver is in my system but wasn't the default one that SQLAlchemy using, so putting it in the URL does the trick. 
		- Download the required file for the default driver to work, I used this [link](https://askubuntu.com/questions/1321141/unable-to-install-mysqlclient-on-ubuntu-20-10) to download the necessary files for the SQLAlchamy default required driver.
## Executing a direct a query

```python
conn = engine.connect()
result = conn.execute("select * from table")
print(result.fetchall())
conn.close()
```

## Table Mapping with SQLAlchemy's Declarative System

In Declarative, we create classes that directly map to database tables. These classes are based on a special `base` class that keeps track of our classes and tables. We typically create just one instance of this base class in a module that we import across our application.

To create this base class, we simply use the `declarative_base()` function. This base class helps us manage our classes and tables smoothly.

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

Then we can use `Base` instance as blueprint to define a class that inherits from it and represents the table structure. After you can use the `create_all()` method to create the table in the database:

```python
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'  # Table name

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    age = Column(Integer, ForeignKey("city_table.id"), default=18)

Base.metadata.create_all(engine)
```

Here, we create an SQLite database engine and use `create_all()` to create the table defined by our `User` class.

## Connection to the database  

`Session` is a class that represents a connection to the database and provides a context for making changes to the database. It acts as a middleman between your Python code and the database. You use a session to query the database, insert, update, or delete records, and manage transactions. Sessions keep track of objects loaded from the database and changes made to those objects, allowing you to commit or rollback changes as needed.

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()
```

Every change that have been made is considering in one of those state:

- **Transient**: Change have been made, but not in the session, or in the database
- **Pending**: Change is new currently in the session, but wasn't flushed to database

```python
session.add(users_instances)
```

- **Persistent**: An instance which is present in the session and has a record in the database

```python
session.commit()
# OR by querying the database for existing instances
```

Note:

```python
# pending objects recently added to the Session
session.new

# persistent objects which currently have changes detected
# (this collection is now created on the fly each time the property is called)
session.dirty

# persistent objects that have been marked as deleted via session.delete(obj)
session.deleted

# dictionary of all persistent objects, keyed on their
# identity key
session.identity_map
```
## Create new record

### Adding one record

```python
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)
session.commit()
```

### Adding multiple records

```python
session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
```

# Querying

## Get one record
#### ``Query.one()`` 
- ``MultipleResultsFound ``if the number of rows was more than 1
- ``NoResultFound`` if no rows were found.
- Returns the sole result row
#### ``Query.first()`` executes the query with LIMIT 1
- Returns the result row as tuple
- ``None`` if no rows were found
#### ``Query.scalar()`` 
- Raises ``MultipleResultsFound`` if the number of rows was more than 1
- Returns None If no rows were found.
- Returns the first column of the sole result row.

## Get all records

```python
session.query(User, User.name).all()
session.query(User, User.name).all()[5:69] # [limit:offset]
```

```python
session.query(User).order_by(User.id)
```

```python
for name, in session.query(User.name).filter_by(fullname='Ed Jones'):

# Or filter

session.query(User).filter(User.name=='ed')
session.query(User).filter(User.name.in_(['ed', 'fakeuser']))
session.query(User).filter(User.name=='ed').filter(User.fullname=='Ed Jones')

query.filter(User.name == 'ed')
query.filter(User.name != 'ed')
query.filter(User.name.like('ed%'))
query.filter(User.name.ilike('ed%')) # case-insensitive 

from sqlalchemy import or_, and_
query.filter(or_(User.name == 'ed', User.name == 'wendy'))
query.filter(and_(User.name == 'ed', User.name == 'wendy'))
```

```python
session.query(User.name, User.fullname)  
# [("ali", "ali jbari"), ("test", "testing")]
```

```python
# SELECT name as name_label from users;

for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)
```

```python
session.query(User).from_statement (
	text("SELECT * FROM users where name=:name")
).params(name='ed').all()
```

#### Count and group trick

```python
session.query(func.count(User.name), User.name).group_by(User.name).all()
```

## Generic Types

![](https://i.imgur.com/Y9kmnlU.png)

## Declare relationship between tables

[Check this link](https://overiq.com/sqlalchemy-101/defining-schema-in-sqlalchemy-core/)

## Join tables

```python
result = session.query(State, City).join(City, State.id == City.state_id).all()
```

## Relationships
### One to One

```python
class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    designation = Column(String(255), nullable=False)
    doj = Column(Date(), nullable=False)
    dl = relationship('DriverLicense', backref=backref('person', uselist=False), uselist=False)

class DriverLicense(Base):
    __tablename__ = 'driverlicense'
    id = Column(Integer(), primary_key=True)
    license_number = Column(String(255), nullable=False)
    renewed_on = Column(Date(), nullable=False)
    expiry_date = Column(Date(), nullable=False)
    person_id = Column(Integer(), ForeignKey('persons.id'))  # Foreign key
```

If we hadn't passed `uselist=False` to the `relationship()` function then the relationship between `Person` and `DriverLicense` would be one-to-many and `p.dl` would return a list of `DriverLicense` objects rather than a single object, the some thing goes with `dl.person`.
### One To Many

```python
class City(Base):
	__tablename__ = 'cities'
	state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
	name = Column(String(128), nullable=False)

class State(Base):
	__tablename__ = 'states'
	name = Column(String(128), nullable=False)
	cities = relationship(
		"City",
		backref="state",
		cascade="all, delete-orphan"
	)
```
### Many To Many

```python
Base = declarative_base()

author_book = Table('author_book', Base.metadata, 
    Column('author_id', Integer(), ForeignKey("authors.id")),
    Column('book_id', Integer(), ForeignKey("books.id"))
)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    copyright = Column(SmallInteger, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    authors = relationship("Author", secondary=author_book, backref="books")
```

- Given an `Author` object `a`, we can access all books written by him as `a.books` (because of ``backref``). 
- Given a `Book` object `b`, `b.authors` (because of book class method `authors`) will return a list of `Author` objects.
## Remove all tables

```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData


db_str = "mysql://alien:password@localhost:3360/dbname"
engine = create_engine(db_str)

def clean_db():
    m = MetaData()
    m.reflect(engine)
    m.drop_all(engine)
```