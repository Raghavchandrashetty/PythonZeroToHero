from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage
import os

app = Flask(__name__)

# Set up Google Cloud Storage client
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/service-account-file.json'
client = storage.Client("stately-timing-428423-b4")
bucket_name = 'raghav-ecommerce-sales-data'
bucket = client.bucket(bucket_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file)
        return f"File {file.filename} uploaded to {bucket_name}."

if __name__ == '__main__':
    app.run(debug=True)
