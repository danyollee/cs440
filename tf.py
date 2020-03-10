import requests
import json
import re

class tf_API:
    def __init__(self):
        self.track_url = "https://ba644d26.api.tunefind.com/api/v2/song"
        self.artist_url = "https://ba644d26.api.tunefind.com/api/v2/artist"
        self.auth=('ba644d265ab6e026a46d3d51f0f7d520','ad8a3ce60d1a5eb5d6f6f63ad37c058b')

    def get_tracks(self):
        print("Requesting API...")
        offset = 0
        counter = 0
        data = True
        while(data):
            para = {'offset': offset, 'limit': 2000}
            r = requests.get(self.track_url, auth=self.auth, params=para)
            print("API status code: ", r.status_code)
            file_name = 'track' + str(counter) + '.json'
            with open(file_name, 'w') as outfile:
                json.dump(r.json(), outfile)
            offset = offset+2000
            counter = counter+1
            a = r.json()['songs']
            if a == []:
                data = False

    def get_artists(self):
        print("Requesting API...")
        offset = 0
        counter = 0
        data = True
        while(data):
            para = {'offset': offset, 'limit': 2000}
            r = requests.get(self.artist_url, auth=self.auth, params=para)
            print("API status code: ", r.status_code)
            file_name = 'artist' + str(counter) + '.json'
            with open(file_name, 'w') as outfile:
                json.dump(r.json(), outfile)
            offset = offset+2000
            counter = counter+1
            a = r.json()['artists']
            if a == []:
                data = False


    
# REGEX: (?<=\"name\"\: \")(.*?)(?=\",)
def main():
    caller = tf_API()
    caller.get_tracks()
    caller.get_artists()

if __name__ == "__main__":
    main()