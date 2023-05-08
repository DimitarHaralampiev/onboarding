from testing.city_country import city_country


def test_city_country():
    """Test method city, country with two parameters"""
    sofia_bulgaria = city_country('sofia', 'bulgaria')
    assert sofia_bulgaria == 'Sofia, Bulgaria'


def test_city_country_population():
    """Test method city, country with three parameters"""
    sofia_bulgaria = city_country('sofia', 'bulgaria', population=1_000_000)
    assert sofia_bulgaria == 'Sofia, Bulgaria - population 1000000'
