# Apple store inventory tracker
- Status: Just get started ...
    
    - [x] Crawl a single iphone 15 pro's availability and parse data correctly.
    
        Input:

            product Id: MTQU3LL/A
            zip code: 97204 (Portland, OR)

        Output:
        ```
        No.1 stores:
            store_name: Pioneer Place
            reservation_url: http://www.apple.com/retail/pioneerplace
            product_name: iPhone 15 Pro 256GB Natural Titanium
            product_id: MTQU3LL/A
            availability_status: unavailable
            store_address: ('Apple Pioneer Place, 450 SW Yamhill Street', 'Portland, OR, 97204')
            store_hours: [{'day': 'Sun:', 'timing': '11:00 AM-6:00 PM'}, {'day': 'Mon-Sat:', 'timing': '10:00 AM-7:00 PM'}]


        No.2 stores:
            store_name: Washington Square
            reservation_url: http://www.apple.com/retail/washingtonsquare
            product_name: iPhone 15 Pro 256GB Natural Titanium
            product_id: MTQU3LL/A
            availability_status: unavailable
            store_address: ('Apple Washington Square, 9585 SW Washington Square Rd', 'Tigard, OR, 97223')
            store_hours: [{'day': 'Sun:', 'timing': '11:00 AM-7:00 PM'}, {'day': 'Mon-Sat:', 'timing': '10:00 AM-9:00 PM'}]


        No.3 stores:
            store_name: Bridgeport Village
            reservation_url: http://www.apple.com/retail/bridgeportvillage
            product_name: iPhone 15 Pro 256GB Natural Titanium
            product_id: MTQU3LL/A
            availability_status: unavailable
            store_address: ('Apple Bridgeport Village, 7273 SW Bridgeport Road', 'Tigard, OR, 97224')
            store_hours: [{'day': 'Mon-Sat:', 'timing': '10:00 AM-8:00 PM'}, {'day': 'Sun:', 'timing': '11:00 AM-6:00 PM'}]


        No.4 stores:
            store_name: Tacoma Mall
            reservation_url: http://www.apple.com/retail/tacomamall
            product_name: iPhone 15 Pro 256GB Natural Titanium
            product_id: MTQU3LL/A
            availability_status: unavailable
            store_address: ('Apple Tacoma Mall, 4502 S Steele Street', 'Tacoma, WA, 98409')
            store_hours: [{'day': 'Mon-Sat:', 'timing': '10:00 AM-8:00 PM'}, {'day': 'Sun:', 'timing': '11:00 AM-6:00 PM'}]


        No.5 stores:
            store_name: Southcenter
            reservation_url: http://www.apple.com/retail/southcenter
            product_name: iPhone 15 Pro 256GB Natural Titanium
            product_id: MTQU3LL/A
            availability_status: unavailable
            store_address: ('Apple Southcenter, 801 Southcenter Mall', 'Tukwila, WA, 98188')
            store_hours: [{'day': 'Sun:', 'timing': '11:00 AM-7:00 PM'}, {'day': 'Mon-Sat:', 'timing': '10:00 AM-9:00 PM'}]


        No.6 stores:
            store_name: Bellevue Square
            reservation_url: http://www.apple.com/retail/bellevuesquare
            product_name: iPhone 15 Pro 256GB Natural Titanium
            product_id: MTQU3LL/A
            availability_status: unavailable
            store_address: ('Apple Bellevue Square, 213 Bellevue Square', 'Bellevue, WA, 98004')
            store_hours: [{'day': 'Sun:', 'timing': '11:00 AM-7:00 PM'}, {'day': 'Mon-Sat:', 'timing': '10:00 AM-9:00 PM'}]


        No.7 stores:
            store_name: University Village
            reservation_url: http://www.apple.com/retail/universityvillage
            product_name: iPhone 15 Pro 256GB Natural Titanium
            product_id: MTQU3LL/A
            availability_status: unavailable
            store_address: ('Apple University Village, 2651 NE 49th St', 'Seattle, WA, 98105')
            store_hours: [{'day': 'Mon-Sat:', 'timing': '10:00 AM-8:00 PM'}, {'day': 'Sun:', 'timing': '11:00 AM-6:00 PM'}]


        No.8 stores:
            store_name: Alderwood
            reservation_url: http://www.apple.com/retail/alderwood
            product_name: iPhone 15 Pro 256GB Natural Titanium
            product_id: MTQU3LL/A
            availability_status: unavailable
            store_address: ('Apple Alderwood, 3000 184th Street S.W.', 'Lynnwood, WA, 98037')
            store_hours: [{'day': 'Sun:', 'timing': '11:00 AM-7:00 PM'}, {'day': 'Mon-Sat:', 'timing': '10:00 AM-8:00 PM'}]

        ``` 
        - [ ] Crawl all iphone 15 Pro and iphone 15 Pro Max, colors + capacity
        - [ ] Crawl from all apple stores in the United States.
        - [ ] Support apple watch ultra + bands
        - [ ] Support Alert and Notification


## Use cases:
- View apple product's avalability of apple stores
    - Filers:
        - Product
        - Model
        - Zip code
        - State

- Alert & Notification
    - Push to Email for a requested product
