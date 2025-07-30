from animal_etl.utils import transform_animal

def test_transform_friends():
    result = transform_animal({'friends': 'dog, cat , fish'})
    assert result['friends'] == ['dog', 'cat', 'fish']

def test_transform_born_at():
    result = transform_animal({'born_at': '2021-01-01T12:00:00-05:00'})
    assert result['born_at'].endswith('Z') or result['born_at'].endswith('+00:00')
