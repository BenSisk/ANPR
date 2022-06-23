import requests
import time

with open('ip.txt', 'r') as f:
    ip = f.read()

response = requests.get(ip + "/api/events")

with open('latest.txt', 'r') as f:
    last_time = f.read()
    try:
        newFiles = False
        last_time = int(last_time)
        latest = int(time.time())
        for event in response.json():
            start_time = float(event['start_time'])
            if(start_time > last_time):
                newFiles = True
                id = str(event['id'])
                url = ip + "/api/events/" + id + "/snapshot.jpg"
                img_data = requests.get(url).content
                with open("new/" + id + ".jpg", 'wb') as handler:
                    handler.write(img_data)

        with open('latest.txt', 'w') as f:
            f.write(str(latest))
        if (not newFiles):
            print("No New Images")
    except Exception as e:
        print("Something went wrong:", e)