from minio import Minio
import urllib.request
import pandas as pd
import sys
from urllib import request
import os


def main():
    grab_data()


def grab_data() -> None:
    """Grab the data from New York Yellow Taxi

    This method download x files of the New York Yellow Taxi. 
    
    Files need to be saved into "../../data/raw" folder
    This methods takes no arguments and returns nothing.
    """
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata"
    folder = "../../data/ATL-Datamart-1/minio/parquets"

    year_range = range(2023, 2024)
    month_range = range(1, 13)

    for year in year_range:
        error_count = 0
        print(f"Downloading files for {year}")
        for month in month_range:
            month_str = str(month).zfill(2)
            url = f"{base_url}_{year}-{month_str}.parquet"
            filename = os.path.join(folder, url.split('/')[-1])
            print(f"Downloading file from {url} to {filename}")
            try:
                request.urlretrieve(url, filename)
                print(f"Downloaded file: {filename}")
            except Exception as e:
                break
        print(f"Downloaded all files for {year} !")

    print("All files downloaded")

if __name__ == '__main__':
    main()

        
def write_data_minio():
    """
    This method put all Parquet files into Minio
    Ne pas faire cette méthode pour le moment
    """
    client = Minio(
        "localhost:9000",
        secure=False,
        access_key="minio",
        secret_key="minio123"
    )
    bucket: str = "NOM_DU_BUCKET_ICI"
    found = client.bucket_exists(bucket)
    if not found:
        client.make_bucket(bucket)
    else:
        print("Bucket " + bucket + " existe déjà")

if __name__ == '__main__':
    sys.exit(main())
