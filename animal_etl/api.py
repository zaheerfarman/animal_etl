import requests
from tenacity import retry, stop_after_attempt, wait_random
from typing import List

BASE_URL = "http://localhost:3123"

@retry(stop=stop_after_attempt(5), wait=wait_random(2, 5))
def get_animals_page(page: int):
    res = requests.get(f"{BASE_URL}/animals/v1/animals", params={"page": page})
    res.raise_for_status()
    return res.json()

@retry(stop=stop_after_attempt(5), wait=wait_random(2, 5))
def get_animal_detail(animal_id: str):
    res = requests.get(f"{BASE_URL}/animals/v1/animals/{animal_id}")
    res.raise_for_status()
    return res.json()

@retry(stop=stop_after_attempt(5), wait=wait_random(2, 5))
def post_animals_home(animals: List[dict]):
    res = requests.post(f"{BASE_URL}/animals/v1/home", json=animals)
    res.raise_for_status()
