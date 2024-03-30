Project Title: Generic RESTful API for Multiple Databases with FastAPI

Description:

This project demonstrates how to build a generic RESTful API that can interact with multiple types of databases using FastAPI, a modern Python web framework. The goal of the project is to provide a flexible and extensible solution for building APIs that can seamlessly switch between different database backends, such as PostgreSQL and MongoDB, without changing the application logic.

Key Features:

Database Abstraction: Define a common interface (Database) for interacting with databases, with abstract methods for CRUD operations.
Concrete Implementations: Implement concrete database classes (PostgresDB and MongoDB) that adhere to the Database interface, providing specific implementations for PostgreSQL and MongoDB databases.
Dependency Injection: Use FastAPI's dependency injection feature to inject instances of database implementations into endpoint functions dynamically.
RESTful Endpoints: Define CRUD endpoints for creating, reading, updating, and deleting data, utilizing the injected database instances to perform the necessary operations.
Flexibility: Easily switch between different database backends by changing the database configuration, without modifying the application code.
Pydantic Models: Utilize Pydantic models for data validation and serialization/deserialization between API requests and database operations.
Scalability: Build scalable APIs with FastAPI's asynchronous capabilities, allowing for high-performance data processing.
Usage:

Clone the repository.
Install the required dependencies using pip install -r requirements.txt.
Configure the database connection settings in the config.py file.
Run the FastAPI application using uvicorn main:app --reload.
Test the API endpoints using tools like curl, Postman, or any HTTP client.
Contributing:

Contributions are welcome! If you have any ideas for improvements, feature requests, or bug fixes, feel free to open an issue or submit a pull request.





