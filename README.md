
# Author-Havin API Clone

This is a clone of the Author-Havin API built using Django, Docker, Redis, and Celery. It contains several functionalities like user authentication, profiles, articles, ratings, bookmarks, responses, and search.

## Features

* **Users App**: User registration, authentication, and profile management.
* **Articles App**: CRUD functionality for articles.
* **Ratings App**: Users can rate articles.
* **Bookmarks App**: Users can bookmark articles.
* **Responses App**: Users can respond to articles.
* **Search App**: Implement search functionality for articles.
* **Redis & Celery**: Background task processing.

## Requirements

1. Docker
2. Docker Compose
3. Python 3.x
4. Redis (Managed via Docker)
5. Celery (for task management)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

* [Docker Desktop](https://www.docker.com/products/docker-desktop)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Git](https://git-scm.com/)

## Setup Instructions

### 1. **Clone the repository**

First, clone this repository using Git:

```bash
git clone git@github.com:Ali-Sina-255/Author-havin-clone-api.git
cd Author-havin-clone-api
```

### 2. **Install Docker and Docker Compose**

* **Docker Desktop**:
  [Download and Install Docker Desktop](https://www.docker.com/products/docker-desktop) for your operating system. Follow the official instructions to complete the installation.

* **Docker Compose**:
  Docker Compose is usually included with Docker Desktop, but if it's not installed, follow these steps to install it:
  [Docker Compose Installation Guide](https://docs.docker.com/compose/install/).

### 3. **Setup the Docker environment**

1. **Build the Docker images:**

   Navigate to the project directory (if you’re not already there) and run the following command to build the Docker images:

   ```bash
   docker-compose build
   ```

2. **Start the services:**

   Start the services (Django, Redis, Celery, etc.) by running:

   ```bash
   docker-compose up
   ```

   This will start all the services (e.g., Redis, Celery, Django server) defined in your `docker-compose.yml`.

3. **Create migrations and apply them:**

   After the containers are up, run the following command to apply the database migrations:

   ```bash
   docker-compose run web python manage.py migrate
   ```

4. **Create a superuser (optional):**

   If you need to create a superuser to access Django's admin panel:

   ```bash
   docker-compose run web python manage.py createsuperuser
   ```

5. **Run Celery:**

   In a new terminal window, run the following to start the Celery worker:

   ```bash
   docker-compose run web celery -A your_project_name worker --loglevel=info
   ```

   Make sure to replace `your_project_name` with the actual name of your Django project (the same name used in `celery.py`).

### 4. **Access the Application**

After everything is set up and running:

* Django's development server will be available at `http://localhost:8000`.
* The Django Admin interface can be accessed at `http://localhost:8000/admin/`.

You can log in using the superuser credentials you created earlier.

## Docker Compose Services

* **web**: The Django application.
* **redis**: Redis service for caching and Celery.
* **celery**: Celery worker for asynchronous task processing.

## Example Commands for Docker Compose

1. **Start the services in the background:**

   ```bash
   docker-compose up -d
   ```

2. **Stop the services:**

   ```bash
   docker-compose down
   ```

3. **View logs:**

   You can view the logs for all services or for a specific service like `web`:

   ```bash
   docker-compose logs
   ```

4. **Access the Django shell:**

   To access the Django shell:

   ```bash
   docker-compose run web python manage.py shell
   ```

## Useful Links

* [Django Documentation](https://docs.djangoproject.com/en/stable/)
* [Celery Documentation](https://docs.celeryproject.org/en/stable/)
* [Redis Documentation](https://redis.io/documentation)

## Additional Setup (Optional)

If you want to set up **environment variables** such as `DATABASE_URL`, `SECRET_KEY`, or others, you can create a `.env` file in the root of the project and add the necessary variables there.

Example:

```dotenv
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgres://user:password@db:5432/database_name
```

Make sure to update your Docker Compose setup and Django settings to read from these environment variables.

## Troubleshooting

If you run into issues:

1. **Ensure Docker Desktop is running**.

2. **Check Docker Compose logs** for errors:

   ```bash
   docker-compose logs
   ```

3. **Check the Django logs** for potential issues with migrations or the database.

---

https://raw.githubusercontent.com/Ali-Sina-255/Author-havin-clone-api/main/my_project_models.png
![Project Image](https://raw.githubusercontent.com/Ali-Sina-255/Author-havin-clone-api/main/my_project_models.png)
