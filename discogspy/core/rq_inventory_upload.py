# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/05_core.rq_inventory_upload.ipynb (unless otherwise specified).

__all__ = ['add_new_listings_using_csv', 'update_existing_listings_using_csv', 'delete_listings_using_csv']

# Cell
import requests
from typing import Union
import io
from . import *

# Cell


def add_new_listings_using_csv(user: UserWithUserTokenBasedAuthentication,
                               file: io.BufferedReader) -> requests.models.Response:
    """
    Upload a csv file of listings to add to your inventory.

    User Authentication needed.
    """

    url = f"{INVENTORY_UPLOAD_URL}/add"
    params = user.params
    files = {"upload": file}

    return requests.post(url, params=params, files=files)

# Cell


def update_existing_listings_using_csv(user: UserWithUserTokenBasedAuthentication,
                                       file: io.BufferedReader) -> requests.models.Response:
    """
    Upload a CSV file with updated information for existing listings.

    User Authentication needed.
    """

    url = f"{INVENTORY_UPLOAD_URL}/change"
    params = user.params
    files = {"upload": file}

    return requests.post(url, params=params, files=files)

# Cell


def delete_listings_using_csv(user: UserWithUserTokenBasedAuthentication,
                              file: io.BufferedReader) -> requests.models.Response:
    """
    Upload a CSV file with listings to delete from your inventory.

    User Authentication needed.
    """

    url = f"{INVENTORY_UPLOAD_URL}/delete"
    params = user.params
    files = {"upload": file}

    return requests.post(url, params=params, files=files)