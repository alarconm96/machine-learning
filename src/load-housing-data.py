# fetch and load housing data
# if it doesn't exist, create the directory datasets/housing.tgz

from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        # mkdir "datasets" with any missing parents of that directory also being created
        # additioanlly, if the directory already exists, a FileExistsError is ignored rather than being thrown, which is the default
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"

        # retrieve data from the URL arg into the local directory provided in the second arg
        urllib.request.urlretrieve(url, tarball_path)
        
        # with statements work like try-catch from Java, simplifying how code is run while accounting for error handling
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing.csv"))