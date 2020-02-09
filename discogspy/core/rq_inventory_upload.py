# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/05_core.rq_inventory_upload.ipynb (unless otherwise specified).

__all__ = ['add_new_listings_using_csv', 'update_existing_listings_using_csv', 'delete_listings_using_csv',
           'get_list_of_recent_uploads', 'get_upload']

# Cell
import requests
from typing import Union
import io
from . import *

# Cell


def add_new_listings_using_csv(user: UserWithUserTokenBasedAuthentication,
                               file: io.BufferedReader
                               ) -> requests.models.Response:
    """
    Upload a csv file of listings to add to the given user inventory.

    Note: The file you upload must be a comma-separated CSV.
          The first row must be a header with lower case field names.
          All listings will be marked “For Sale” immediately.
          Currency information will be pulled from your marketplace settings.
          Any fields that aren’t optional or required will be ignored.

    User Authentication needed.

    Parameters:

    user: user object (required)

    file: file (required)
        -> The CSV file of items to add to your inventory.

    Csv File Values:

    release_id: number (required)
        -> This value corresponds with the Discogs database Release ID.

    media_condition: string (required)
        -> The condition of the release you are posting.

    price: number (required)
        -> The price of the item (in the seller’s currency).

    status: string (required)
        -> The status of the listing. Defaults to For Sale.

    sleeve_condition: string (optional)
        -> The condition of the sleeve of the item you are posting.

    comments: string (optional)
        -> Any remarks about the item that will be displayed to buyers.

    allow_offers: boolean (optional)
        -> Must be Y or N.

    external_id: string (optional)
        -> A freeform field that can be used for the seller’s own reference.
        -> Information stored here will not be displayed to anyone other than the seller.
        -> This field is called “Private Comments” on the Discogs website.

    location: string (optional)
        -> A freeform field that is intended to help identify an item’s physical storage location.
        -> Information stored here will not be displayed to anyone other than the seller.
        -> This field will be visible on the inventory management page and will be available in inventory exports via the website.

    weight: number (optional)
        -> The weight, in grams, of this listing, for the purpose of calculating shipping.
        -> Set this field to auto to have the weight automatically estimated for you.

    format_quantity: number (optional)
        -> The number of items this listing counts as, for the purpose of calculating shipping.
        -> This field is called “Counts As” on the Discogs website.
        -> Set this field to auto to have the quantity automatically estimated for you.
    """

    url = f"{INVENTORY_UPLOAD_URL}/add"
    headers = user.headers
    params = user.params
    files = {"upload": file}

    return requests.post(url, headers=headers, params=params, files=files)

# Cell


def update_existing_listings_using_csv(user: UserWithUserTokenBasedAuthentication,
                                       file: io.BufferedReader
                                       ) -> requests.models.Response:
    """
    Upload a CSV file with updated information for existing listings in given user inventory.

    Note: The file you upload must be a comma-separated CSV.
          The first row must be a header with lower case field names.
          All listings will be marked “For Sale” immediately.
          Currency information will be pulled from your marketplace settings.
          Any fields that aren’t optional or required will be ignored.

    User Authentication needed.

    Parameters:

    user: user object (required)

    file: file (required)
        -> The CSV file of items to add to your inventory.

    Csv File Values:

    release_id: number (optional)
        -> This value corresponds with the Discogs database Release ID.

    media_condition: string (optional)
        -> The condition of the release you are posting.

    price: number (optional)
        -> The price of the item (in the seller’s currency).

    status: string (optional)
        -> The status of the listing. Defaults to For Sale.

    sleeve_condition: string (optional)
        -> The condition of the sleeve of the item you are posting.

    comments: string (optional)
        -> Any remarks about the item that will be displayed to buyers.

    allow_offers: boolean (optional)
        -> Must be Y or N.

    external_id: string (optional)
        -> A freeform field that can be used for the seller’s own reference.
        -> Information stored here will not be displayed to anyone other than the seller.
        -> This field is called “Private Comments” on the Discogs website.

    location: string (optional)
        -> A freeform field that is intended to help identify an item’s physical storage location.
        -> Information stored here will not be displayed to anyone other than the seller.
        -> This field will be visible on the inventory management page and will be available in inventory exports via the website.

    weight: number (optional)
        -> The weight, in grams, of this listing, for the purpose of calculating shipping.
        -> Set this field to auto to have the weight automatically estimated for you.

    format_quantity: number (optional)
        -> The number of items this listing counts as, for the purpose of calculating shipping.
        -> This field is called “Counts As” on the Discogs website.
        -> Set this field to auto to have the quantity automatically estimated for you.
    """

    url = f"{INVENTORY_UPLOAD_URL}/change"
    headers = user.headers
    params = user.params
    files = {"upload": file}

    return requests.post(url, headers=headers, params=params, files=files)

# Cell


def delete_listings_using_csv(user: UserWithUserTokenBasedAuthentication,
                              file: io.BufferedReader
                              ) -> requests.models.Response:
    """
    Upload a CSV file with listings to delete from the given inventory.

    Note: The file you upload must be a comma-separated CSV.
          The first row must be a header with lower case field names.

    User Authentication needed.

    Parameters:

    user: user object (required)

    file: file (required)
        -> The CSV file of items to add to your inventory.

    Csv File Values:

    release_id: number (required)
        -> This value corresponds with the Discogs database Release ID.
    """

    url = f"{INVENTORY_UPLOAD_URL}/delete"
    headers = user.headers
    params = user.params
    files = {"upload": file}

    return requests.post(url, headers=headers, params=params, files=files)

# Cell


def get_list_of_recent_uploads(user: UserWithUserTokenBasedAuthentication,
                               page: Union[int, None] = None,
                               per_page: Union[int, None] = None
                               ) -> requests.models.Response:
    """
    Get a list of all recent inventory uploads for the given inventory.

    User Authentication needed.

    Parameters:

    user: user object (required).

    page: number (optional)
        -> The page you want to request.

    per_page: number (optional)
        -> The number of items per page.
    """

    url = f"{INVENTORY_UPLOAD_URL}"
    headers = user.headers
    params = user.params

    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)

    return requests.get(url, headers=headers, params=params)

# Cell


def get_upload(user: UserWithUserTokenBasedAuthentication,
               upload_id: int
               ) -> requests.models.Response:
    """
    Get details about the status of the given inventory upload.

    User Authentication needed.

    Parameters:

    user: user object (required).

    upload_id: number (required)
        -> Id of the upload.
    """

    url = f"{INVENTORY_UPLOAD_URL}/{upload_id}"
    headers = user.headers
    params = user.params

    return requests.get(url, headers=headers, params=params)