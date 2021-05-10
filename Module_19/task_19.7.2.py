from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_invalid_user(email=valid_email):
    status, result = pf.get_api_key(email, "")
    assert status == 403
    assert "This user wasn't found in database" in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    print(result)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_with_invalid_filter_params():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, "kot")
    assert status == 400

def test_add_new_pet_with_valid_data(name='Monstro', animal_type='bull',
                                     age='5', pet_photo='tests/images/cat1.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    pet_id = result['id']
    pf.delete_pet(auth_key, pet_id)

def test_add_new_pet_with_invalid_data(name='Sil', animal_type='ork',
                                       age='1', pet_photo='tests/files/test.txt'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_add_new_pet_with_very_large_name(pet_photo='tests/images/cat1.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    name = 'koteeeee'
    status, result = pf.add_new_pet(auth_key, name * 1000, name, '0', pet_photo)
    assert status == 400

def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "sobaka", "kot", "18", "tests/images/cat1.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()

def test_delete_not_owned_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "")
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    not_owned = [x for x in pets['pets'] if x not in my_pets['pets']]
    pet_id = not_owned[0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, pets = pf.get_list_of_pets(auth_key, "")
    assert status == 403
    assert pet_id in pets.values()

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Мурзик", "кот", "3", "tests/images/cat1.jpeg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
        pet_id = my_pets['pets'][0]['id']
        pf.delete_pet(auth_key, pet_id)
    else:
        raise Exception("There is no my pets")

def test_update_not_owned_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "")
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    not_owned = [x for x in pets['pets'] if x not in my_pets['pets']]
    if len(not_owned) > 0:
        status, result = pf.update_pet_info(auth_key, not_owned[0]['id'], name, animal_type, age)
        assert status == 403
    else:
        raise Exception("There is no pets")

def test_add_new_pet_no_photo_with_valid_data(name='Звезда', animal_type='звэр',
                                              age='7'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    assert result['pet_photo'] == ""
    pet_id = result['id']
    pf.delete_pet(auth_key, pet_id)

def test_add_new_pet_no_photo_with_invalid_age(name='Азалия', animal_type='кошка',
                                              age='32565546'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 400

def test_set_photo_with_valid_data(name='Лин', animal_type='двортерьер',
                                   age='1'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    status, result = pf.set_photo(auth_key, result['id'], "tests/images/cat1.jpeg")
    assert status == 200
    assert result['name'] == name
    assert result['pet_photo'] != ""
    pet_id = result['id']
    pf.delete_pet(auth_key, pet_id)

def test_set_photo_to_not_owned_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, pets = pf.get_list_of_pets(auth_key, "")
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    not_owned = [x for x in pets['pets'] if x not in my_pets['pets']]

    status, result = pf.set_photo(auth_key, not_owned[0]['id'], "tests/images/cat1.jpeg")
    assert status == 403
