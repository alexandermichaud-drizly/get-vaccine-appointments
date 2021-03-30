import sys
import json 
from time import sleep, localtime

locations = json.load(sys.stdin)['responsePayloadData']['data']['MA']
available_locations = list(filter(lambda l: l['status'] != "Fully Booked", locations))

if len(available_locations) > 0:
    from os import getenv
    from twilio.rest import Client

    cities = map(lambda obj: obj['city'], available_locations)

    sid = getenv('TWILIO_SID')
    auth_token = getenv('TWILIO_AUTH_TOKEN')

    client = Client(sid, auth_token)

    body_text = "Vaccine appointments now available in " + ",".join(cities) + "\n https://www.cvs.com/immunizations/covid-19-vaccine \n https://www.cvs.com/store-locator/landing?icid=cvsheader:storelocator"

    message = client.messages.create(
        to="+16033980413",
        from_="+13396744164",
        body=body_text)
    
    print(body_text)
    sys.exit(0)
now = localtime()
print(f'No appointments available as of {now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}. Fetching again...')
sleep(2)
sys.exit(2)

