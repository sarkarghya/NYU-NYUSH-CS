import json
from binascii import hexlify
from hashlib import sha256
from django.conf import settings
from os import urandom, system

SEED = settings.RANDOM_SEED
CARD_PARSER = 'giftcardreader'

# KG: Something seems fishy here. Why are we seeding here?
def generate_salt(length, debug=True):
    import random
    random.seed(SEED)
    return hexlify(random.randint(0, 2**length-1).to_bytes(length, byteorder='big'))

def hash_pword(salt, pword):
    assert(salt is not None and pword is not None)
    hasher = sha256()
    hasher.update(salt)
    hasher.update(pword.encode('utf-8'))
    return hasher.hexdigest()

def parse_salt_and_password(user):
    return user.password.split('$')

def check_password(user, password): 
    salt, password_record = parse_salt_and_password(user)
    verify = hash_pword(salt.encode('utf-8'), password)
    if verify == password_record:
        return True
    return False

def write_card_data(card_file_path, product, price, customer):
    data_dict = {}
    data_dict['merchant_id'] = product.product_name
    data_dict['customer_id'] = customer.username
    data_dict['total_value'] = price
    record = {'record_type':'amount_change', "amount_added":2000,'signature':'[ insert crypto signature here ]'}
    data_dict['records'] = [record,]
    with open(card_file_path, 'w') as card_file:
        card_file.write(json.dumps(data_dict))

def parse_card_data(card_file_data, card_path_name):
    print(card_file_data)
    try:
        test_json = json.loads(card_file_data)
        return card_file_data
    except (json.JSONDecodeError, UnicodeDecodeError):
        pass
    with open(card_path_name, 'wb') as card_file:
        card_file.write(card_file_data)
    # KG: Are you sure you want the user to control that input?
    ret_val = system(f"./{CARD_PARSER} 2 {card_path_name} > tmp_file")
    if ret_val != 0:
        return card_file_data
    with open("tmp_file", 'r') as tmp_file:
        return tmp_file.read()
