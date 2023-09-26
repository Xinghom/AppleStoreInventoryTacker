import time
import requests
from bs4 import BeautifulSoup
import json

CRAWL_INTERVAL = 600 # 10 mins
URL_PATTERN = ("https://www.apple.com/shop/fulfillment-messages?pl=true&mts.0=regular"
               "&mts.1=compact&cppart=UNLOCKED/US&parts.0={product_id}&location={zip_code}")

def crawl_url(product_id, zip_code):
    url = URL_PATTERN.format(product_id=product_id, zip_code=zip_code)
    response = requests.get(url)

    if response.status_code == 200:
        extracted_data = parse_data(response.content)
        return extracted_data
    else:
        msg = (f"failed to fetch data for product_id: {product_id}, "
               "zip_code: {zip_code}, "
               "code: {response.status_code}")
        raise ValueError(msg)

def parse_data(content):
    data = json.loads(content)
    all_stores_data = data['body']['content']['pickupMessage']['stores']
    parsed_data_list = []
    for store_data in all_stores_data:
        # Avoid indexing repeatly
        parts_data = store_data['partsAvailability'].get('MTQU3LL/A', {})
        compact_data_from_parts = parts_data.get('messageTypes', {}).get('compact', {})

        address = store_data['address']
        store_address = (f"{address.get('address')}, {address.get('address2')}" ,
                         f"{store_data.get('city')}, {store_data.get('state')}, "
                         f"{address.get('postalCode')}")

        parsed_store_data = {
            'store_name': store_data.get('storeName'),
            'reservation_url': store_data.get('reservationUrl'),
            'product_name': compact_data_from_parts.get('storePickupProductTitle'),
            'product_id': parts_data.get('partNumber'),
            'availability_status': parts_data.get('pickupDisplay'),
            'store_address': store_address,
            'store_hours': [{"day": hour['storeDays'], "timing": hour['storeTimings']} 
                            for hour in store_data['storeHours']['hours']]
        }
        parsed_data_list.append(parsed_store_data)
        
    return parsed_data_list

def store_data(data):
    pass

def fetch_latest_data():
    pass

def view_product_availability():
    pass

def print_parsed_data(data):
    for i, store in enumerate(data):
        print(f"No.{i} stores:")
        for k, v in store.items():
            print(f"{k}: {v}")
    return

if __name__ == "__main__":
    # prototyping purpose
    product_id = "MTQU3LL/A"
    zip_code = "98005"
    try:
        data = crawl_url(product_id, zip_code)
        print_parsed_data(data)
    except ValueError as e:
        print(e)

    # while True:
    #     product_id = "MTQU3LL/A"
    #     zip_code = "98005"
    #     data = crawl_url(product_id, zip_code)
    #     if data != -1:
    #         print(data)
        # store_data(data)
        # time.sleep(CRAWL_INTERVAL)
