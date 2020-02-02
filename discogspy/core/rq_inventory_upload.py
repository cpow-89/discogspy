# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/05_core.rq_inventory_upload.ipynb (unless otherwise specified).

__all__ = ['upload_list_of_listings']

# Cell
import requests
from typing import Union
import io
from . import *

# Cell


def upload_list_of_listings(user: UserWithUserTokenBasedAuthentication,
                            file: io.BufferedReader) -> requests.models.Response:
    """
    Upload a csv file of listings to add to your inventory.

    User Authentication needed.
    """

    url = f"{INVENTORY_UPLOAD_URL}/add"
    params = user.params
    files = {"upload": file}

    return requests.post(url, params=params, files=files)