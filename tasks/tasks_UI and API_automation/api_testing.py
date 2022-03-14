import requests
import json
from check_data_type import *


def post_value():
    url = "https://petstore.swagger.io/v2/pet"

    payload = json.dumps({
        "id": 333,
        "category": {
            "id": 1,
            "name": "My doggy"
        },
        "name": "Sheru",
        "photoUrls": [
            "https://media.istockphoto.com/photos/australian-shepherd-sitting-against-white-background-picture-id1154953522"
        ],
        "tags": [
            {
                "id": 0,
                "name": "dog, sheru, pet"
            }
        ],
        "status": "available"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    status = response.status_code
    if status == 200:
        print(f'Get API response is successful with stats code {status}')
    else:
        print(f'Data upload failed with status code {status}')

def get_value():
    url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)
    status = response.status_code
    if status == 200:
        print(f'Get API response is successful with stats code {status}')
    else:
        print(f'Get API response failed with status code {status}')
    res = response.json()
    for val in res:
        d_type = check_integer(val['id'])
        if d_type:
            print('Response data type matched for id')
        else:
            raise Exception(f"Data type mis-matched for {val['id']}")

        try:
            cat_id = val['category']['id']
            cat_id = check_integer(cat_id)
            if cat_id:
                print('Response data type matched for categoryID')
            else:
                raise Exception(f"Data type mis-matched for {cat_id}")
            cat_iname = val['category']['name']
            cat_iname = check_string(cat_iname)
            if cat_iname:
                print('Response data type matched category name')
            else:
                raise Exception(f"Data type mis-matched for {cat_iname}")
        except Exception as e:
            print(e)

        name = check_string(val['name'])
        if name:
            print('Response data type matched name')
        else:
            raise Exception(f"Data type mis-matched for {val['name']}")

        photoUrls = check_list(val['photoUrls'])
        if photoUrls:
            print('Response data type matched for photoUrls')
        else:
            raise Exception(f"Data type mis-matched for {val['photoUrls']}")

        for values in val['tags']:
            tags_id = values['id']
            tags_name = values['name']
            tags_id = check_integer(tags_id)
            if tags_id:
                print('Response data type matched for tags id')
            else:
                raise Exception(f"Data type mis-matched for {tags_id}")

            tags_name = check_string(tags_name)
            if tags_name:
                print('Response data type matched for tags name')
            else:
                raise Exception(f"Data type mis-matched for {tags_name}")

        response_status = val['status']
        response_status = check_string(response_status)
        if response_status:
            print('Response data type matched for status')
        else:
            raise Exception(f"Data type mis-matched for {response_status}")

def update_value():
    url = "https://petstore.swagger.io/v2/pet"

    payload = json.dumps({
        "id": 333,
        "category": {
            "id": 0,
            "name": "New value updated"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "update value new"
            }
        ],
        "status": "available"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    response_json = response.json()
    status = response.status_code
    if status == 200:
        print(f'Get API response is successful with status code {status}')
    else:
        print(f'Data upload failed with status code {status}')

    cat_name = response_json['category']['name']
    if cat_name == 'New value updated':
        print(f"Value updated successfully to {cat_name} ")
    else:
        print('Value update failed')

def delete_order():
    orderID = [3, 5, 6, 10, 12, 15, 18, 34, 55, 66, 111, 444, 564]
    for ids in orderID:
        url = f"https://petstore.swagger.io/v2/store/order/{ids}"

        payload = {}
        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload)
        status = response.status_code
        if status == 200:
            print(f'Get API response is successful with status code {status}')
            print(f'orderID {ids} exists and deleted successfully!')
        else:
            print(f'orderID {ids} doesn\'t exists in our database and returns status code {status}!')
