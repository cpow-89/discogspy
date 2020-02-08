# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/07_core.rq_wantlist.ipynb (unless otherwise specified).

__all__ = ['get_user_wantlist', 'add_release_to_wantlist', 'change_notes_of_a_release_from_wantlist',
           'change_rating_of_a_release_from_wantlist', 'delete_release_from_wantlist']

# Cell
import requests
from typing import Union
from . import *

# Cell


def get_user_wantlist(user: Union[UserWithoutAuthentication,
                                  UserWithUserTokenBasedAuthentication],
                      username: str,
                      page: Union[int, None] = None,
                      per_page: Union[int, None] = None,
                      ) -> requests.models.Response:
    """
    Get a list of releases from the wantlist of a given user.

    Note: If the wantlist has been made private by its owner,
          you must be authenticated as the owner to view it.

    No user Authentication needed.
    """

    url = f"{USERS_URL}/{username}/wants"
    headers = user.headers
    params = user.params

    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)

    return requests.get(url, headers=headers, params=params)

# Cell


def add_release_to_wantlist(user: UserWithUserTokenBasedAuthentication,
                            username: str,
                            release_id: int,
                            notes: Union[str, None] = None,
                            rating: Union[int, None] = None
                            ) -> requests.models.Response:
    """
    Add a releases to the wantlist of a given user.

    User Authentication needed.
    """

    url = f"{USERS_URL}/{username}/wants/{release_id}"
    params = user.params
    data = {}

    if rating:
        rating = min(max(0, rating), 5)
        data["rating"] = rating
    if notes:
        data["notes"] = notes

    return requests.put(url, params=params, json=data)

# Cell


def change_notes_of_a_release_from_wantlist(user: UserWithUserTokenBasedAuthentication,
                                            username: str,
                                            release_id: int,
                                            notes: str
                                            ) -> requests.models.Response:
    """
    Change the notes of a releases from the wantlist of a given user.

    User Authentication needed.
    """

    url = f"{USERS_URL}/{username}/wants/{release_id}"
    params = user.params

    data = {"notes": notes}

    return requests.post(url, params=params, json=data)

# Cell


def change_rating_of_a_release_from_wantlist(user: UserWithUserTokenBasedAuthentication,
                                             username: str,
                                             release_id: int,
                                             rating: int
                                             ) -> requests.models.Response:
    """
    Change the rating of a releases from the wantlist of a given user.

    User Authentication needed.
    """

    url = f"{USERS_URL}/{username}/wants/{release_id}"
    params = user.params

    rating = min(max(0, rating), 5)
    data = {"rating": rating}

    return requests.post(url, params=params, json=data)

# Cell


def delete_release_from_wantlist(user: UserWithUserTokenBasedAuthentication,
                                 username: str,
                                 release_id: int
                                 ) -> requests.models.Response:
    """
    Delete a releases from the wantlist of a given user.

    User Authentication needed.
    """

    url = f"{USERS_URL}/{username}/wants/{release_id}"
    headers = user.headers
    params = user.params

    return requests.delete(url, headers=headers, params=params)