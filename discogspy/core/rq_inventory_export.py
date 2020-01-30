# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_core.rq_inventory_export.ipynb (unless otherwise specified).

__all__ = ['request_inventory_export', 'get_recent_exports', 'get_export_details']

# Cell
import requests
from typing import Union
from . import *

# Cell


def request_inventory_export(user: UserWithUserTokenBasedAuthentication) -> requests.models.Response:
    """
    Request an export of your inventory as a CSV.

    User Authentication needed.
    """
    url = f"{INVENTORY_EXPORT_URL}"
    headers = user.headers
    params = user.params

    return requests.post(url, headers=headers, params=params)

# Cell


def get_recent_exports(user: UserWithUserTokenBasedAuthentication,
                       page: Union[int, None] = None,
                       per_page: Union[int, None] = None
                       ) -> requests.models.Response:
    """
    Get a list of all recent exports of your inventory.

    User Authentication needed.
    """
    url = f"{INVENTORY_EXPORT_URL}"
    headers = user.headers
    params = user.params

    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)

    return requests.get(url, headers=headers, params=params)

# Cell


def get_export_details(user: UserWithUserTokenBasedAuthentication,
                       export_id: int
                       ) -> requests.models.Response:
    """
    Get a list of all recent exports of your inventory.

    User Authentication needed.
    """
    url = f"{INVENTORY_EXPORT_URL}/{export_id}"
    headers = user.headers
    params = user.params

    return requests.get(url, headers=headers, params=params)