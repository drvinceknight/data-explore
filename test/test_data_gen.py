from randomdatagen import generate_random_testing_data


def test_generate_random_testing_data():
    """
    create and verify a randomly gentrated testing dataset
    """
    data = generate_random_testing_data(20)
    assert len(data) == 60
