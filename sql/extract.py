"""
Extract a dataset from a URL like Kaggle or data.gov.
JSON or CSV formats tend to work well

Fortune Cookie Dataset
"""
import requests


def extract(
    url="https://raw.githubusercontent.com/nogibjj/week7_afraa_simrun_fortune_cookie/main/Fortune%20Cookies%20Dataset.csv",
    file_path="data/Fortune_Cookies_Dataset.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path

extract()