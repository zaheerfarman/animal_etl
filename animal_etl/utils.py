from dateutil import parser
from datetime import timezone
from typing import Dict


def transform_animal(animal: Dict) -> Dict:
    animal['friends'] = [
        f.strip()
        for f in animal.get('friends', '').split(',')
        if f.strip()
    ]

    if animal.get('born_at'):
        try:
            dt = parser.parse(animal['born_at']).astimezone(timezone.utc)
            animal['born_at'] = dt.isoformat()
        except Exception:
            animal['born_at'] = None
    return animal
