# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API using the FastAPI framework to manage a list of resources and practice building endpoints for common CRUD operations.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Start by creating a simple FastAPI application with a basic in-memory data store. Your API should respond with JSON data and serve as the foundation for a working web service.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app
- Define a resource model using Python data structures or Pydantic models
- Create at least one endpoint that returns a list of items
- Return JSON responses in a clear, readable format
- Run the app locally with Uvicorn

### 🛠️ Build CRUD Endpoints

#### Description
Expand your application so it supports creating, reading, updating, and deleting items through REST-style routes.

#### Requirements
Completed program should:

- Add a POST endpoint to create a new item
- Add a GET endpoint to return all items
- Add a GET endpoint to fetch a single item by ID
- Add a PUT or PATCH endpoint to update an existing item
- Add a DELETE endpoint to remove an item
- Return clear status codes such as 200, 201, and 404
- Validate required fields and reject invalid input gracefully

### 🛠️ Add a Polished API Experience

#### Description
Improve the app so it feels complete and easier to use, including request validation and helpful responses.

#### Requirements
Completed program should:

- Use Pydantic models for request validation
- Handle missing items with a clear error message
- Keep the API logic organized and easy to read
- Include a short description of how to run the app and test the endpoints
- Demonstrate at least one example request and response in the project notes
