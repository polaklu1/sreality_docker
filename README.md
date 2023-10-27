# sreality_docker
## Description

Scraper for sreality.cz website that scapes first 500 items, stores title, locality and image url into postgresql database. Results are shown using uvicorn webserver on address : 127.0.0.1:8080. All in single docker container.

### Running
```
docker-compose up
```