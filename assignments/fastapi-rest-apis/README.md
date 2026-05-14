# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a REST API using the FastAPI framework to practice building HTTP endpoints, handling request data, and returning JSON responses. This assignment helps students learn API design, routing, and basic request validation.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description

Build a FastAPI app that exposes endpoints for listing items and retrieving item details. Use Python data structures to store sample items and return JSON responses for each route.

#### Requirements

Completed application should:

- Use FastAPI to create a web server
- Provide a `GET /items` endpoint that returns a list of items
- Provide a `GET /items/{item_id}` endpoint that returns details for a single item
- Return data in JSON format with appropriate fields
- Run with Uvicorn and respond correctly to HTTP requests

### 🛠️ Add a create endpoint and validation

#### Description

Extend the API with a route that accepts new item data and validates the request body using FastAPI models.

#### Requirements

Completed application should:

- Use Pydantic models to validate request data
- Provide a `POST /items` endpoint that accepts a new item payload
- Return the created item with a success status
- Handle invalid input with a meaningful validation error response
