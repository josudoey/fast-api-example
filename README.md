# FastAPI Production-Ready Example

This repository provides a production-ready example of a FastAPI application.

It includes a basic API with data validation, testing, and a Dockerfile for containerization.

## Features

*   **FastAPI:** For building high-performance APIs.
*   **Pydantic:** For data validation.
*   **Pytest:** For testing the application.
*   **Docker:** For containerizing the application.

## Getting Started

### Prerequisites

*   Python 3.9+
*   pip
*   Docker (optional, for containerization)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd fast-api-example
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```

## Running the Application

To run the application in development mode with auto-reload:

```bash
uvicorn cmd.server:app --reload
```

Alternatively, you can run the application directly using Python:

```bash
python cmd/server.py
```

The application will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Running Tests

To run the tests, use pytest:

```bash
pytest
```

## Docker

A `Dockerfile` is included for containerizing the application.

1.  **Build the Docker image:**
    ```bash
    docker build -t fastapi-example-app .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -d -p 8080:80 fastapi-example-app
    ```
    The application will be accessible at `http://localhost:8080`.

## Running with Docker Compose

A `docker-compose.yml` file is also provided for easier development and deployment.

To build and run the application using Docker Compose:

```bash
docker-compose up --build
```

This will start the application, and it will be accessible at `http://localhost:8000`. The `--build` flag ensures the image is rebuilt if there are any changes.

To run in detached mode (in the background):

```bash
docker-compose up -d --build
```

To stop the services:

```bash
docker-compose down
```

## API Endpoints

| Method | Path                | Description                   |
|--------|---------------------|-------------------------------|
| `GET`  | `/`                 | Returns a welcome message.    |
| `GET`  | `/items/{item_id}`  | Retrieves an item by its ID.  |
| `PUT`  | `/items/{item_id}`  | Updates an item by its ID.    |
