import os
import requests
from datetime import datetime

# URL du répertoire contenant les fichiers
url = 'https://exemple.com/chemin_du_dossier/'

# Répertoire local de destination
local_directory = '/votre_chemin_local/'

# Années de début et de fin de la plage souhaitée
start_year = 2018
end_year = 2023

# Fonction pour télécharger des fichiers dans une plage d'années
def download_files_between_years(url, local_dir, start_year, end_year):
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            file_name = f'yellow_tripdata_{year}_{month:02d}.parquet'
            file_url = url + file_name
            local_file_path = os.path.join(local_dir, file_name)

            response = requests.get(file_url, stream=True)
            if response.status_code == 200:
                with open(local_file_path, 'wb') as local_file:
                    for chunk in response.iter_content(chunk_size=8192):
                        local_file.write(chunk)
                print(f'Téléchargé : {file_name}')

# Télécharger les fichiers entre les années de début et de fin spécifiées
download_files_between_years(url, local_directory, start_year, end_year)