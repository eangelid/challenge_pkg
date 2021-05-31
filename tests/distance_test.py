from challenge_pkg.distance import haversine

def test_type_of_haversine_calc():
    assert type(haversine(48.865070, 2.380009, 48.235070, 2.393409)) is float