from .api import get_animals_page, get_animal_detail, post_animals_home
from .utils import transform_animal
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

def extract_animal_ids() -> List[str]:
    page, ids = 1, []
    while True:
        data = get_animals_page(page)
        if not data:
            break
        animals = data.get("items", []) 
        ids.extend([a['id'] for a in animals])
        page += 1
    return ids

def fetch_details_parallel(ids: List[str]) -> List[dict]:
    details = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(get_animal_detail, aid): aid for aid in ids}
        for future in as_completed(futures):
            try:
                details.append(future.result())
            except Exception as e:
                print(f"Error fetching {futures[future]}: {e}")
    return details

def etl_process():
    ids = extract_animal_ids()
    details = fetch_details_parallel(ids)
    transformed = [transform_animal(a) for a in details]

    for i in range(0, len(transformed), 100):
        batch = transformed[i:i+100]
        post_animals_home(batch)
