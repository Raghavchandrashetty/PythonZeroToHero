import requests
import csv
from  google.cloud import storage

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

querystring = {"formatType":"odi"}

headers = {
	"x-rapidapi-key": "eac9b65493msheb0ca0a4aee5489p1d1c56jsne17d6fc69016",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

if response.status_code == 200:
    data = response.json().get('rank', [])
    csv_filename = 'batsmen_ranking.csv'

    if data:
        field_names = ['rank', 'name', 'country']

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)

            for  entry in data:
                writer.writerow( {field: entry.get(field) for field in field_names})

        print(f"Data fetched successfully and written to {csv_filename}")
        # Upload the CSV file to a GCS bucket

        # Set your GCS bucket name and destination file name
        source_file_name = 'batsmen_ranking.csv'
        bucket_name = 'bkt-cricket-ranking-data'  # Replace with your bucket name
        destination_blob_name = f'{csv_filename}'  # Replace with the desired path in your bucket
        project_id = 'stately-timing-428423-b4'

        storage_client = storage.Client(project_id)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(f'File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}.')

    else:
        print(f"No data available from API")


else:
    print("Failed to fetch the data : ", response.status_code)
