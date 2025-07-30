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

### 1. Download Docker Image
Manually download the Docker image:

🔗 [Download Docker Image (.tar.gz)](https://drive.google.com/file/d/1MNt0fBJAjOu7pODx0HsStDLBemhAgBuR/view?usp=sharing)

Save it as:

```bash
lp-programming-challenge-1-1625758668.tar.gz
```

> Load The Image

```bash
docker load -i lp-programming-challenge-1-1625758668.tar.gz
```
> Load The Image

```bash
docker run --rm -p 3123:3123 -ti lp-programming-challenge-1
```

>Clone and Enter Project


```bash
git clone https://github.com/zaheerfarman/animal_etl.git
cd animal_etl
```
> Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```
>  Install Poetry and Dependencies
```bash
pip install poetry
poetry install
```
> activate your virtual environment
```bash
venv\Scripts\activate
```
> Run the ETL pipeline:
```bash
poetry run python animal_etl/main.py
```
> You should see logs like:
```bash
✔ Retrieved 450 animal IDs
✔ Posted batch 1 of 5
✔ Posted batch 2 of 5
...
🎉 ETL process complete!

> Run Tests
```bash
poetry run pytest
```
> Lint with flake8
```bash
poetry run flake8 animal_etl/
```