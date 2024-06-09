# Database

## What is a database?

**Database** is a systematic and structured collection of data that is organized and stored in a way that allows efficient management and updating of that data.

## Why Databases?

Storing data in your application's memory or flat files has limitations such as data loss on server shutdown. Databases address these shortcomings and provide features like ACID properties:

| ACID Properties | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| Atomicity       | Ensures transactions are atomic, either fully completed or not at all.       |
| Consistency     | Enforces rules for data integrity; transactions must abide by defined rules. |
| Isolation       | Guarantees that simultaneous operations won't interfere with each other.     |
| Durability      | Persists data even in the face of unexpected server shutdowns.               |

## Why Not Flat Files?

While flat files may seem simple, they lack the robustness of databases. ACID properties ensure data integrity, and databases offer better performance and scalability.


## CRUD Operations

CRUD operations represent the four basic actions that can be performed on data:

| CRUD Operation | Description               |
| -------------- | ------------------------- |
| Create         | Add new data              |
| Read           | Retrieve existing data    |
| Update         | Modify existing data      |
| Destroy        | Remove data               |

A reliable database should support all four CRUD operations.

# How to install mysql

- [mysql 5.7](https://medium.com/@jmwangi0x01/install-mysql-5-7-x-in-ubuntu-20-x-d5c7456b72dd)
- [mysql 8](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

