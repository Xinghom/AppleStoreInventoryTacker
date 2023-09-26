import time
import requests
from bs4 import BeautifulSoup
import json

CRAWL_INTERVAL = 600 # 10 mins
URL_PATTERN = ("https://www.apple.com/shop/fulfillment-messages?pl=true&mts.0=regular"
               "&mts.1=compact&cppart=UNLOCKED/US&parts.0={product_id}&location={zip_code}")

IPHONE_MODEL = {"iPhone 15 Pro" : "ip_15_pro",
                "iPhone 15 Pro Max" : "ip_15_pro_max"}
COLORS = {"White" : '0'}
PRODUCT_IDS = {IPHONE_MODEL["iPhone 15 Pro"] + COLORS["White"] + "256GB" : "MTQT3LL/A"}

def crawl_url(product_id, zip_code):
    url = URL_PATTERN.format(product_id=product_id, zip_code=zip_code)
    response = requests.get(url)

    if response.status_code == 200:
        extracted_data = parse_data(response.content, product_id)
        return extracted_data
    else:
        msg = (f"failed to fetch data for product_id: {product_id}, "
               "zip_code: {zip_code}, "
               "code: {response.status_code}")
        raise ValueError(msg)

def parse_data(content, product_id):
    data = json.loads(content)
    all_stores_data = data['body']['content']['pickupMessage']['stores']
    parsed_data_list = []
    for store_data in all_stores_data:
        # Avoid indexing repeatly
        parts_data = store_data['partsAvailability'].get(product_id, {})
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
        print(f"No.{i + 1} stores:")
        for k, v in store.items():
            print(f"    {k}: {v}")
        print('\n')

    return

def get_and_print_interested_data(data):
    target_stores = []
    for store in data:
        if store['availability_status'] != "unavailable":
            target_stores.append(store)
    if target_stores:
        print_parsed_data(target_stores)
    else:
        print("No interested product found yet ...")
    

if __name__ == "__main__":
    # prototyping purpose
    product_id = "MTQU3LL/A" # iPhone 15 Pro 256GB Natural Titanium
    zip_code = "97204" # Portland
    try:
        data = crawl_url(product_id, zip_code)
        get_and_print_interested_data(data)
        product_id = "MTQT3LL/A" # white 15 pro 256GB
        get_and_print_interested_data(crawl_url(product_id, zip_code))
    except ValueError as e:
        print(e)

    # while True:
    #     product_id = "MTQU3LL/A"
    #     zip_code = "97204"
    #     data = crawl_url(product_id, zip_code)
    #     if data != -1:
    #         print(data)
        # store_data(data)
        # time.sleep(CRAWL_INTERVAL)
