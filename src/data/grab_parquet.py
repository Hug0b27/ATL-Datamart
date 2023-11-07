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
    folder = "../../data/raw/"

    year_range = range(2018, 2024)
    month_range = range(1, 13)

    for year in year_range:
        error_count = 0
        print(f"Telechargement des fichiers pour l'annee {year}")
        for month in month_range:
            month_str = str(month).zfill(2)
            url = f"{base_url}_{year}-{month_str}.parquet"
            filename = os.path.join(folder, url.split('/')[-1])
            print(f"Telechargement de {url} vers {filename}")
            try:
                request.urlretrieve(url, filename)
                print(f"Fichier telecharge: {filename}")
            except Exception as e:
                break
        print(f"Tous les fichiers sont telecharges pour l'annee {year} !")

    print("Tous les fichiers sont telecharges !")

if __name__ == '__main__':
    main()