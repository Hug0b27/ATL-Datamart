from urllib import request
import os
import re
import requests

def main():
    grab_latest_data()  

# def grab_data() -> None:
#     """Grab the data from New York Yellow Taxi

#     This method download x files of the New York Yellow Taxi. 
    
#     Files need to be saved into "../../data/raw" folder
#     This methods takes no arguments and returns nothing.
#     """

#     # Constants
#     base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata"
#     folder = "../../data/raw/"

#     year_range = range(2018, 2024)
#     month_range = range(1, 13)

#     for year in year_range:
#         error_count = 0
#         print(f"Downloading files for year {year}")
#         for month in month_range:
#             month_str = str(month).zfill(2)
#             url = f"{base_url}_{year}-{month_str}.parquet"  # Correction ici : changement de baseurl à base_url
#             filename = os.path.join(folder, url.split('/')[-1])
#             print(f"Downloading file from {url} to {filename}")
#             try:
#                 request.urlretrieve(url, filename)  # Correction ici : changement de requests à request
#                 print(f"Downloaded file: {filename}")
#             except Exception as e:
#                 break
#         print(f"Downloaded all files for year {year} !")

#     print("Downloaded all files !")

# if __name__ == '__main__':  # Correction ici : changement de name à __name__
#     main()


def grab_latest_data() -> None:
    """Grab the latest data file from New York Yellow Taxi

    This method identifies and downloads the latest file of the New York Yellow Taxi from the URL. 
    
    The file needs to be saved into the "../../data/raw" folder.
    This method takes no arguments and returns nothing.
    """

    # Constants
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata"
    folder = "../../data/raw/"
    latest_file = None  # Initialize the variable to store the latest file

    year = 2023
    month = 8
    month_str = str(month).zfill(2)
    url = f"{base_url}_{year}-{month_str}.parquet"
    filename = os.path.join(folder, url.split('/')[-1])

    # Check if the file exists
    response = requests.head(url)
    if response.status_code == 200:
        latest_file = filename
        print(f"Latest file available: {latest_file}")

        # Download the latest file
        request.urlretrieve(url, latest_file)
        print(f"Downloaded latest file to: {latest_file}")
    else:
        print("No files were found.")

if __name__ == '__main__':
    main()
