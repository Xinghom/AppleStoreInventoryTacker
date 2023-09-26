# Functional requirements
- View apple product's avalability of apple stores
    - Filers:
        - Product
        - Model
        - Zip code
        - State

- Alert & Notification
    - Push to Email for a requested product

- Respect rules - https://www.apple.com/robots.txt

## Workflow
### Write path:
while True:
1. crawl URLs - static content
   Example:
   - https://www.apple.com/shop/fulfillment-messages?pl=true&mts.0=regular&mts.1=compact&cppart=UNLOCKED/US&parts.0=MTQV3LL/A&location=98005
2. store data in google sheet (as a database)
3. pause for 10 mins

### Read/View path:

If the data is available from google sheet with in 5 mins:

- Read the latest availability from google sheet.
 
else:
- Run "write path" to get the lastest data for that specific product and zip code

### Alert path:


