import json
import csv

def main():
    convert_tracks()
    convert_artists()
    

def convert_tracks():
    counter = 0

    csv_file = open('tracks.csv', 'w')
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(["track", "album"])

    while(counter <= 111):

        file_name = "track" + str(counter) + ".json"
        with open(file_name) as data_file:
            data = json.load(data_file)

        track_info = data['songs']

        for track in track_info:
            csv_writer.writerow([track['name'], track['album']])

        counter += 1

    csv_file.close()

def convert_artists():
    counter = 0

    csv_file = open('artists.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["artists"])

    while(counter <= 35):
        file_name = "artist" + str(counter) + ".json"
        with open(file_name) as f:
            data = json.load(f)

        artist_info = data['artists']

        for artist in artist_info:
            csv_writer.writerow([artist['name']])

        counter += 1


if __name__ == "__main__":
    main()