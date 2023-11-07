import os
import requests
import pandas as pd

# URL du répertoire contenant les fichiers .parquet
base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'

# Répertoire local de destination pour les fichiers .parquet
local_directory = '../../data/raw'

# Créer un répertoire local s'il n'existe pas
if not os.path.exists(local_directory):
    os.makedirs(local_directory)

# Dates de début et de fin de la plage souhaitée
start_date = (2018, 1)
end_date = (2023, 8)

# Fonction pour télécharger des fichiers .parquet pour une plage de dates
def download_parquet_files_between_dates(base_url, local_dir, start_date, end_date):
    for year in range(start_date[0], end_date[0] + 1):
        for month in range(1, 13):
            if (year, month) < start_date or (year, month) > end_date:
                continue
            file_name = f'yellow_tripdata_{year}_{month:02d}.parquet'
            file_url = base_url + file_name
            local_file_path = os.path.join(local_dir, file_name)

            with requests.get(file_url, stream=True) as r:
                r.raise_for_status()
                with open(local_file_path, 'wb') as local_file:
                    for chunk in r.iter_content(chunk_size=8192):
                        local_file.write(chunk)
                print(f'Téléchargé : {file_name}')

# Télécharger les fichiers .parquet pour la plage de dates spécifiée
download_parquet_files_between_dates(base_url, local_directory, start_date, end_date)
