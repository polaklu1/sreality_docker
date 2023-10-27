# sreality_docker
## Description

This project is a web scraper for sreality.cz that extracts data from the website's first 500 items and stores the title, locality, and image URL into a PostgreSQL database. The results are then displayed using a Uvicorn web server at address http://127.0.0.1:8080, all within a single Docker container.

## Features

- Scrapes data from sreality.cz, including title, locality, and image URL.
- Stores the scraped data in a PostgreSQL database.
- Displays the scraped data using a web server powered by Uvicorn.

## Getting Started

Follow these steps to get the project up and running:

1. Clone this repository.

2. Build the Docker image:

   ```shell
   docker-compose up