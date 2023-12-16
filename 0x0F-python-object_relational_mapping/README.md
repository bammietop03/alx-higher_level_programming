## Learning Object Relational Mapping ORM

## Install and activate venv
To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

	$ sudo apt-get install python3.8-venv
	$ python3 -m venv venv
	$ source venv/bin/activate

## Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

	$ sudo apt-get install python3-dev
	$ sudo apt-get install libmysqlclient-dev
	$ sudo apt-get install zlib1g-dev
	$ sudo pip3 install mysqlclient
	...
	$ python3
	>>> import MySQLdb
	>>> MySQLdb.version_info 
	(2, 0, 3, 'final', 0)

## Install SQLAlchemy module version 1.4.x
	$ sudo pip3 install SQLAlchemy
	...
	$ python3
	>>> import sqlalchemy
	>>> sqlalchemy.__version__ 
	'1.4.22'

## How to Execute Queries in MySQLdb
In a Python file using MySQLdb, you can execute queries in a few steps:

1. Connecting to the Database:
First, establish a connection to your MySQL database using MySQLdb. This involves providing the necessary connection details like host, username, password, and database name.

	import MySQLdb
	// Establish connection
	db = MySQLdb.connect(host="your_host",
        	             user="your_username",
                	     passwd="your_password",
        		     db="your_database")

2. Creating a Cursor:
Next, create a cursor object to execute SQL queries.

	cursor = db.cursor()

3. Executing Queries:
Now, you can execute SQL queries using the execute() method on the cursor.

For example, to retrieve data:

	cursor.execute("SELECT * FROM your_table")
	data = cursor.fetchall()
	for row in data:
    		print(row)

4. Handling Transactions:
Remember to commit any changes made (if necessary) and close the cursor and database connection when you're done.

	db.commit()

	# Close the cursor and database connection
	cursor.close()
	db.close()

Replace "your_host", "your_username", "your_password", "your_database", and "your_table" with your actual database details and table name.

## How to Execute Queries in SQLAlchemy
Certainly! Here's a step-by-step breakdown of using SQLAlchemy with MySQL:

1. Installation:
Ensure you have the necessary packages installed. For SQLAlchemy with MySQL, you need sqlalchemy and a compatible MySQL connector like mysql-connector-python.

	pip install sqlalchemy mysql-connector-python

2. Connecting to MySQL Database:

	from sqlalchemy import create_engine

	# Create an engine to connect to a MySQL database
	# Replace 'username', 'password', 'host', 'port', and 'database_name' with your MySQL connection details
	engine = create_engine('mysql+mysqlconnector://username:password@host:port/database_name', echo=True)
	Use can also use 'mysql+mysqldb'

3. Creating a Table Model:
Define a Python class representing the table structure. This will be your model that SQLAlchemy uses to interact with the database.

	from sqlalchemy.ext.declarative import declarative_base
	from sqlalchemy import Column, Integer, String

	# Create a base class for declarative class definitions
	Base = declarative_base()

	# Define a Person model
	class Person(Base):
	    __tablename__ = 'people'

 	   id = Column(Integer, primary_key=True)
	    name = Column(String(50))
	    age = Column(Integer)
	    occupation = Column(String(50))

4. Create Table in Database:
Create the table in the database using the defined model.

	# Create the table in the database
	Base.metadata.create_all(engine)

5. Establishing a Session:

	from sqlalchemy.orm import sessionmaker

	# Create a session to interact with the database
	Session = sessionmaker(bind=engine)
	session = Session()

6. Inserting Data:

	# Add your details to the database
	me = Person(name='Your Name', age=25, occupation='Your Occupation')
	session.add(me)
	session.commit()

7. Querying Data:

	# Querying your data
	your_info = session.query(Person).filter_by(name='Your Name').first()
	if your_info:
	    print(f"Name: {your_info.name}, Age: {your_info.age}, Occupation: {your_info.occupation}")
	else:
	    print("No information found for your name.")

8. Closing the Session:

	# Close the session
	session.close()

Replace 'username', 'password', 'host', 'port', and 'database_name' with your actual MySQL connection details. This set of steps demonstrates connecting to a MySQL database, defining a table model, creating a table, adding data, querying the data, and finally, closing the session. Adjust the table structure and columns based on your needs.

Certainly! When using session.query(Person), you can add various methods to perform operations or filtering on the query. Here are some common methods used after session.query(Person):

.all(): Fetches all records from the table.

	session.query(Person).all()

.filter(): Filters the records based on specified conditions.

	session.query(Person).filter(Person.name == 'John')

.first(): Fetches the first record that matches the query conditions.

	session.query(Person).filter_by(name='John').first()

.order_by(): Orders the records by a specified column.

	session.query(Person).order_by(Person.age)

.count(): Returns the count of records that match the query conditions.

	session.query(Person).filter(Person.age > 25).count()

.delete(): Deletes records that match the query conditions.

	session.query(Person).filter(Person.age > 30).delete()

Chained methods: Methods can be chained together to combine functionalities.

	session.query(Person).filter(Person.age > 20).order_by(Person.name).all()


