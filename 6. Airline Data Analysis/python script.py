import os
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi

# Set your Kaggle username and API key
os.environ['KAGGLE_USERNAME'] = 'sohilamohey'
os.environ['KAGGLE_KEY'] = 'b4da573f71a70f83fbfb36544c116b33'

# Specify the competition/dataset name or URL slug
dataset_name = 'usdot/flight-delays'


# Define function to clean up old files
def cleanup_old_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error cleaning up old file: {e}")


# Check if the dataset directory already exists
if not os.path.exists('flight-delays'):
    os.makedirs('flight-delays')

# Dataset doesn't exist, download it
api = KaggleApi()
api.authenticate()
api.dataset_download_files(dataset_name, path='flight-delays')

print("Dataset downloaded successfully.")

# Extract the downloaded zip file
with ZipFile('flight-delays/flight-delays.zip', 'r') as zip_ref:
    zip_ref.extractall('flight-delays')

print("Dataset extracted successfully.")

# Remove the zip file
os.remove('flight-delays/flight-delays.zip')

print("Zip file removed.")

# Check for updates
api = KaggleApi()
api.authenticate()
dataset_info = api.dataset_list_files(dataset_name)

# Get the list of existing files
existing_files = os.listdir('flight-delays')

# Check if any new files are present on Kaggle
new_files = [file.name for file in dataset_info.files if file.name not in existing_files]

if new_files:
    # Clean up old files
    cleanup_old_files('flight-delays')

    # Download updates
    api.dataset_download_files(dataset_name, path='flight-delays')

    print("New files found. Old files deleted and new files downloaded successfully.")
else:
    print("No new files found. Dataset is already up to date.")


import pandas as pd
# Adjust file paths for Windows
path=r"E:\ITI\11. Power BI\Second Time\Day 6\Lab 6\New folder"
mydata1 = pd.read_csv(os.path.join('flight-delays', 'flights.csv'))
mydata2 = pd.read_csv(os.path.join('flight-delays', 'airports.csv'))
mydata3 = pd.read_csv(os.path.join('flight-delays', 'airlines.csv'))