import uuid
from ddd_attempt1.domain.storageroom import StorageRoom


def test_storageroom_model_init():
    code = uuid.uuid4()
    size = 200
    price = 10
    long = -0.099123213
    lat = 51.75436293
    storageroom = StorageRoom(code, size=size, price=price,
                              longitude=long,
                              latitude=lat)
    assert storageroom.code == code
    assert storageroom.size == 200
    assert storageroom.price == 10
    assert storageroom.longitude == long
    assert storageroom.latitude == lat


def test_storageroom_model_from_dict():
    code = uuid.uuid4()
    size = 200
    price = 10
    long = -0.099123213
    lat = 51.75436293

    _dict = {
        'code': code,
        'size': size,
        'price': price,
        'longitude': long,
        'latitude': lat
    }

    storageroom = StorageRoom.from_dict(_dict)

    assert storageroom.code == code
    assert storageroom.size == size
    assert storageroom.price == price
    assert storageroom.longitude == long
    assert storageroom.latitude == lat


def test_storageroom_model_to_dict():
    code = uuid.uuid4()
    size = 200
    price = 10
    long = -0.099123213
    lat = 51.75436293

    _dict = {
        'code': code,
        'size': size,
        'price': price,
        'longitude': long,
        'latitude': lat
    }

    storageroom = StorageRoom.from_dict(_dict)

    assert storageroom.to_dict() == _dict


def test_storageroom_model_comparison():
    code = uuid.uuid4()
    size = 200
    price = 10
    long = -0.099123213
    lat = 51.75436293

    _dict = {
        'code': code,
        'size': size,
        'price': price,
        'longitude': long,
        'latitude': lat
    }

    storageroom1 = StorageRoom.from_dict(_dict)
    storageroom2 = StorageRoom.from_dict(_dict)

    assert storageroom1 == storageroom2

