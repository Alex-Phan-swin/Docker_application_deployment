# Student Grade Tracker

A simple Flask web application for calculating student grades. The application is containerized using Docker.

## Project Structure

```text
docker-task4.2/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Requirements

* Docker Desktop
* Git (optional)

## Run Locally with Docker

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd docker-task4.2
```

Or open the project folder directly if you already have it.

### 2. Build the Docker image

```bash
docker build -t student-grade-tracker .
```

### 3. Run the container

```bash
docker run -d --name grade-tracker -p 5000:5000 student-grade-tracker
```

The application will now be running inside a Docker container.

### 4. Open the application

Open your browser and visit:

```text
http://localhost:5000
```

You should see the **Student Grade Tracker** application.

## Run with Environment Variables

The application supports the `APP_NAME` and `PORT` environment variables.

```bash
docker run -d --name grade-tracker -p 5000:5000 -e APP_NAME="Student Grade Tracker" -e PORT=5000 student-grade-tracker
```

## Check the Container

View running containers:

```bash
docker ps
```

View application logs:

```bash
docker logs grade-tracker
```

Check the configured environment variables:

```bash
docker exec grade-tracker printenv
```

Check the port mapping:

```bash
docker port grade-tracker
```

## Stop the Container

```bash
docker stop grade-tracker
```

## Remove the Container

```bash
docker rm grade-tracker
```

## Rebuild the Application

If you modify `app.py`, rebuild the Docker image:

```bash
docker build -t student-grade-tracker .
```

Then run a new container:

```bash
docker run -d --name grade-tracker -p 5000:5000 student-grade-tracker
```

## Grade Calculation

The application calculates the overall mark using:

```text
Overall = Assignment × 40% + Exam × 60%
```

The grade boundaries are:

| Overall Mark | Grade |
| -----------: | :---- |
|       80–100 | HD    |
|        70–79 | D     |
|        60–69 | C     |
|        50–59 | P     |
|     Below 50 | F     |
