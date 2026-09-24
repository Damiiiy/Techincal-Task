# Expert Listing API

Property Listings API built with Django REST Framework.

## Setup Instructions

1.  Clone the repository.
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  Start the development server:
    ```bash
    python manage.py runserver
    ```
6.  Access the API documentation at `http://127.0.0.1:8000/api/docs/`.

## Running Tests

Run the following command to execute the test suite:
```bash
python manage.py test
```

## Design Choices

*   Used Django REST Framework for API development.
*   Used SQLite to simplify the setup process.
*   Distance searching is implemented using a custom Haversine formula filter in the ViewSet. This avoids the requirement of setting up PostGIS while satisfying the location search requirement.
*   Added drf-spectacular for Swagger API documentation.

## Potential Improvements

*   Implement PostGIS for true geospatial queries.
*   Add caching layer with Redis.
*   Introduce Elasticsearch or Meilisearch for full-text search capabilities on titles or descriptions.
*   Implement JWT authentication.
*   Add CI/CD pipeline.