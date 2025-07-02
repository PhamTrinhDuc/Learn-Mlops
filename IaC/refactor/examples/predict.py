import sys

import requests

sys.path.append("..")
from app.utils.logging import logger

API_ENDPOINT = "http://localhost:30001/predict"


def main():
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    json_data = {
        "MSSubClass": 60,
        "MSZoning": "RL",
        "LotArea": 7844,
        "LotConfig": "Inside",
        "BldgType": "1Fam",
        "OverallCond": 7,
        "YearBuilt": 1978,
        "YearRemodAdd": 1978,
        "Exterior1st": "HdBoard",
        "BsmtFinSF2": 0,
        "TotalBsmtSF": 672,
    }

    # Post request to prediction endpoint.
    response = requests.post(API_ENDPOINT, headers=headers, json=json_data)
    if response.status_code == 200:
        logger.info("Successful!")
        logger.info(response.json())
    else:
        logger.info("Failed to get prediction!")


if __name__ == "__main__":
    main()
