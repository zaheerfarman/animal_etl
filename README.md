# 🐾 Animal ETL Project

This project extracts, transforms, and loads animal data from a local API (Dockerized), handling pagination, retries, and data transformation. It is built with Python and Poetry, and includes unit tests, linting, and CI integration via GitHub Actions.

---

## 🚀 Features

- Extracts paginated animal data from `/animals/v1/animals`
- Fetches individual animal details
- Transforms:
  - `friends` from comma-separated string → array
  - `born_at` → ISO8601 UTC timestamp
- Posts transformed animals to `/animals/v1/home` in batches of 100
- Handles API delays and transient failures (500/502/503/504) with retry logic
- Includes unit tests and CI pipeline
- Fully linted and formatted with `flake8`

---

## 🐳 Setup Instructions

### 1. Load Docker Image

> Replace with the exact name of your downloaded `.tar.gz` file

```bash
docker load -i lp-programming-challenge-1-1625758668.tar.gz
