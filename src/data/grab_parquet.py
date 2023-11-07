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

    # Constants
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata"
    folder = "../../data/raw/"

    year_range = range(2018, 2024)
    month_range = range(1, 13)

    for year in year_range:
        error_count = 0
        print(f"Downloading files for year {year}")
        for month in month_range:
            month_str = str(month).zfill(2)
            url = f"{base_url}_{year}-{month_str}.parquet"  # Correction ici : changement de baseurl à base_url
            filename = os.path.join(folder, url.split('/')[-1])
            print(f"Downloading file from {url} to {filename}")
            try:
                request.urlretrieve(url, filename)  # Correction ici : changement de requests à request
                print(f"Downloaded file: {filename}")
            except Exception as e:
                break
        print(f"Downloaded all files for year {year} !")

    print("Downloaded all files !")

if __name__ == '__main__':  # Correction ici : changement de name à __name__
    main()