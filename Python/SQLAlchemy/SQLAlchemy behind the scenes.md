# The Core/ORM Dichotomy

![](https://i.imgur.com/u2y6cFM.png)

- **Engine** is stored information about the database that is connects to.
- **Dialect** makes interacting with deferent DBAPIs easy, by abstracting the layer of writing SQL queries for specific database.
- **Connection Pool** - Holds a collection of database connections in memory for easy re-use. 
- **Schema** - Uses Python objects to represent tables, columns and datatypes.