# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/03_core.rq_marketplace.ipynb (unless otherwise specified).

__all__ = ['get_inventory', 'get_listing', 'update_listing', 'delete_listing', 'add_new_listing', 'get_order',
           'update_order_status', 'update_order_shipping', 'get_orders', 'get_order_messages', 'post_message_on_order']

# Cell
import requests
from typing import Union
from . import *

# Cell


def get_inventory(user: Union[UserWithoutAuthentication,
                              UserWithUserTokenBasedAuthentication],
                  username: str,
                  status: Union[StatusInventory, None] = None,
                  page: Union[int, None] = None,
                  per_page: Union[int, None] = None,
                  sort: Union[SortOptionsInventory, None] = None,
                  sort_order: Union[SortOrder, None] = None
                  ) -> requests.models.Response:
    """
    Get a list of listings of a given user inventory.

    No user Authentication needed.

    Note from the Discogs API: "If you are not authenticated as the inventory owner,
    only items that have a status of For Sale will be visible.
    If you are authenticated as the inventory owner you will get additional weight,
    format_quantity, external_id, and location keys.
    If the user is authorized, the listing will contain a in_cart boolean
    field indicating whether or not this listing is in their cart."
    """
    url = f"{USERS_URL}/{username}/inventory"
    headers = user.headers
    params = user.params
    if status:
        if type(user) is UserWithoutAuthentication:
            params["status"] = StatusInventory.for_sale.value
        else:
            params["status"] = status.value
    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)
    if sort:
        if type(user) is UserWithoutAuthentication and (sort is not SortOptionsInventory.status and
                                                        sort is not SortOptionsInventory.location):
            params["sort"] = sort.name
        else:
            params["sort"] = sort.name
    if sort_order:
        params["sort_order"] = sort_order.name
    return requests.get(url, headers=headers, params=params)

# Cell


def get_listing(user: Union[UserWithoutAuthentication,
                            UserWithUserTokenBasedAuthentication],
                listing_id: int,
                curr_abbr: Union[CurrAbbr, None] = None
                ) -> requests.models.Response:
    """
    Get all the information about the requested listing from the given user inventory.

    No user Authentication needed.

    Note from the Discogs API: "If the authorized user is the listing owner the listing
    will include the weight, format_quantity, external_id, and location keys.
    If the user is authorized, the listing will contain a in_cart boolean field
    indicating whether or not this listing is in their cart."
    """
    url = f"{LISTINGS_URL}/{listing_id}"
    headers = user.headers
    params = user.params
    if curr_abbr:
        params["curr_abbr"] = curr_abbr.value
    return requests.get(url, headers=headers, params=params)

# Cell


def update_listing(user: UserWithUserTokenBasedAuthentication,
                   listing_id: int,
                   release_id: int,
                   condition: ReleaseCondition,
                   sleeve_condition: SleeveCondition,
                   price: float,
                   status: StatusInventory,
                   comments: Union[str, None] = None,
                   allow_offers: Union[bool, None] = None,
                   external_id: Union[str, None] = None,
                   location: Union[str, None] = None,
                   weight: Union[int, None] = None,
                   format_quantity: Union[int, None] = None,
                   curr_abbr: Union[CurrAbbr, None] = None
                   ) -> requests.models.Response:
    """
    Update the data associated with a listing.

    User Authentication needed.
    """

    url = f"{LISTINGS_URL}/{listing_id}"
    headers = user.headers

    params = user.params
    if curr_abbr:
        params["curr_abbr"] = curr_abbr.value

    data = {
        "release_id": release_id,
        "condition": condition.value,
        "sleeve_condition": sleeve_condition.value,
        "price": price,
        "status": status.value,
        "comments": comments,
        "allow_offers": allow_offers,
        "external_id": external_id,
        "location": location,
        "weight": weight,
        "format_quantity": format_quantity
    }

    return requests.post(url, headers=headers, params=params, json=data)

# Cell
def delete_listing(user: UserWithUserTokenBasedAuthentication,
                   listing_id: int
                   ) -> requests.models.Response:
    """
    Delete a given item from the inventory.

    User Authentication needed.
    """

    url = f"{LISTINGS_URL}/{listing_id}"
    headers = user.headers
    params = user.params

    return requests.delete(url, headers=headers, params=params)

# Cell


def add_new_listing(user: UserWithUserTokenBasedAuthentication,
                    release_id: int,
                    condition: ReleaseCondition,
                    sleeve_condition: SleeveCondition,
                    price: float,
                    status: StatusNewListing,
                    comments: Union[str, None] = None,
                    allow_offers: Union[bool, None] = None,
                    external_id: Union[str, None] = None,
                    location: Union[str, None] = None,
                    weight: Union[int, None] = None,
                    format_quantity: Union[int, None] = None
                    ) -> requests.models.Response:
    """
    Update the data associated with a listing.

    User Authentication needed.
    """

    url = f"{LISTINGS_URL}"
    headers = user.headers

    params = user.params

    data = {
        "release_id": release_id,
        "condition": condition.value,
        "sleeve_condition": sleeve_condition.value,
        "price": price,
        "status": status.value,
        "comments": comments,
        "allow_offers": allow_offers,
        "external_id": external_id,
        "location": location,
        "weight": weight,
        "format_quantity": format_quantity
    }

    return requests.post(url, headers=headers, params=params, json=data)

# Cell


def get_order(user: UserWithUserTokenBasedAuthentication,
              order_id: str
              ) -> requests.models.Response:
    """
    Get the data associated with an order.

    User Authentication needed.
    """
    url = f"{ORDERS_URL}/{order_id}"
    headers = user.headers
    params = user.params
    return requests.get(url, headers=headers, params=params)

# Cell


def update_order_status(user: UserWithUserTokenBasedAuthentication,
                        order_id: str,
                        status: StatusOrder
                        ) -> requests.models.Response:
    """
    Update the status associated with the given order.

    Note: Use get_order to get the next_status key – an array of valid next statuses for this order.

    User Authentication needed.
    """
    url = f"{ORDERS_URL}/{order_id}"
    headers = user.headers
    params = user.params

    data = {
        "status": status.value
    }

    return requests.post(url, headers=headers, params=params, json=data)

# Cell


def update_order_shipping(user: UserWithUserTokenBasedAuthentication,
                          order_id: str,
                          shipping_cost: float
                          ) -> requests.models.Response:
    """
    Update the shipping costs associated with the given order.

    Note: If the order status is neither cancelled, Payment Received, nor Shipped, you can change the shipping.
          Doing so will send an invoice to the buyer and set the order status to Invoice Sent.

    User Authentication needed.
    """
    url = f"{ORDERS_URL}/{order_id}"
    headers = user.headers
    params = user.params

    data = {
        "shipping": shipping_cost
    }

    return requests.post(url, headers=headers, params=params, json=data)

# Cell


def get_orders(user: UserWithUserTokenBasedAuthentication,
               status: Union[StatusOrders, None] = None,
               page: Union[int, None] = None,
               per_page: Union[int, None] = None,
               sort: Union[SortOptionsOrders, None] = None,
               sort_order: Union[SortOrder, None] = None
               ) -> requests.models.Response:
    """
    Get a list of the user's orders.

    Note: In the original API is an optional parameter called "archived".
          I did not implement it because it always caused a server-sided crash.

    User Authentication needed.
    """
    url = f"{ORDERS_URL}"
    headers = user.headers
    params = user.params

    if status:
        params["status"] = status.value
    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)
    if sort:
        params["sort"] = sort.name
    if sort_order:
        params["sort_order"] = sort_order.name
    return requests.get(url, headers=headers, params=params)

# Cell


def get_order_messages(user: UserWithUserTokenBasedAuthentication,
                       order_id: str,
                       page: Union[int, None] = None,
                       per_page: Union[int, None] = None
                       ) -> requests.models.Response:
    """
    Get a list of messages related to an order, with the most recent first.

    User Authentication needed.
    """
    url = f"{ORDERS_URL}/{order_id}/messages"
    headers = user.headers
    params = user.params

    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)

    return requests.get(url, headers=headers, params=params)

# Cell


def post_message_on_order(user: UserWithUserTokenBasedAuthentication,
                          order_id: str,
                          message: str,
                          ) -> requests.models.Response:
    """
    Post a new message to a given order.

    User Authentication needed.
    """
    url = f"{ORDERS_URL}/{order_id}/messages"
    headers = user.headers
    params = user.params

    data = {
        "message": message
    }

    return requests.post(url, headers=headers, params=params, json=data)