import os
import requests
from dotenv import load_dotenv

load_dotenv()

# .env variables
download_url = os.getenv("DOWNLOAD_URL")
destination_path = os.getenv("DESTINATION_PATH")
file_location = os.getenv("FILE_LOCATION")


# creates directory if it doesn't exist
def create_directory(destination):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

        print(f"Created directory_ {destination}")
    else:
        print(f"Directory {destination} already exists")


# checks if the file already exists
def file_exists(file):
    return os.path.exists(file)


# downloads the file and saves it in the directory
def download_file(url, destination, file):
    print(f"File-Url: {url}")
    print(f"Destination: {destination}")
    print(f"Filename: {file}")
    create_directory(os.path.dirname(destination))

    if file_exists(file):
        print(f"File {file} already exist")
    else:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file, 'wb') as file:
                file.write(response.content)
            print("File successfully downloaded")
        else:
            print(f"Download failed. Statuscode: {response.status_code}")


if __name__ == "__main__":
    print("File Downloader:")
    download_file(download_url, destination_path, file_location)
