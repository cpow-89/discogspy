# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_core.database_rq.ipynb (unless otherwise specified).

__all__ = ['get_release', 'get_release_rating_by_user', 'update_release_rating_for_given_user',
           'delete_release_rating_by_user', 'get_release_rating_by_community', 'get_master_release',
           'get_releases_related_to_master_release', 'get_artist', 'get_artist_releases', 'get_label',
           'get_label_releases']

# Cell
import requests
from typing import Union
from . import *

# Cell


def get_release(user: Union[UserWithoutAuthentication,
                            UserWithUserTokenBasedAuthentication],
                release_id: int,
                curr_abbr: Union[CurrAbbr, None] = None) -> requests.models.Response:
    """
    Get information to a particular release from discogs database.
    A release represents a particular physical or digital object released by
    one or more Artists.

    No user Authentication needed.
    """
    url = f"{RELEASES_URL}/{release_id}"
    headers = user.headers
    params = user.params
    if curr_abbr:
        params["curr_abbr"] = curr_abbr.name
    return requests.get(url, headers=headers, params=params)

# Cell


def get_release_rating_by_user(user: Union[UserWithoutAuthentication,
                                           UserWithUserTokenBasedAuthentication],
                               release_id: int,
                               username: str) -> requests.models.Response:
    """
    Get the rating of a release made by a given user.

    No user Authentication needed.
    """
    url = f"{RELEASES_URL}/{release_id}/rating/{username}"
    headers = user.headers
    params = user.params
    return requests.get(url, headers=headers, params=params)

# Cell


def update_release_rating_for_given_user(user: UserWithUserTokenBasedAuthentication,
                                         release_id: int,
                                         username: str,
                                         rating: int) -> requests.models.Response:
    """
    Update the rating of a release made by a given user.
    If there is no rating, it will create one.

    User Authentication needed.
    """
    url = f"{RELEASES_URL}/{release_id}/rating/{username}"
    headers = user.headers
    params = user.params
    rating = min(max(0, rating), 5)
    data = {"rating": rating}
    return requests.put(url, headers=headers, params=params, json=data)

# Cell


def delete_release_rating_by_user(user: UserWithUserTokenBasedAuthentication,
                                  release_id: int,
                                  username: str) -> requests.models.Response:
    """
    Delete the rating of a release made by a given user.

    User Authentication needed.
    """
    url = f"{RELEASES_URL}/{release_id}/rating/{username}"
    headers = user.headers
    params = user.params
    return requests.delete(url, headers=headers, params=params)

# Cell


def get_release_rating_by_community(user: Union[UserWithoutAuthentication,
                                                UserWithUserTokenBasedAuthentication],
                                    release_id: int) -> requests.models.Response:
    """
    Get the rating of a release made by the community.
    A community release rating includes the average rating and
    the total number of user ratings for a given release.

    This function doesn't work for master releases!

    No user Authentication needed.
    """
    url = f"{RELEASES_URL}/{release_id}/rating"
    headers = user.headers
    params = user.params
    return requests.get(url, headers=headers, params=params)

# Cell


def get_master_release(user: Union[UserWithoutAuthentication,
                                   UserWithUserTokenBasedAuthentication],
                       master_id: int) -> requests.models.Response:
    """
    Get information to a particular master release from discogs database.
    A Master release represents a set of similar Releases.
    Masters releases have a “main release” which is often the chronologically earliest.

    No user Authentication needed.
    """
    url = f"{MASTERS_URL}/{master_id}"
    headers = user.headers
    params = user.params
    return requests.get(url, headers=headers, params=params)

# Cell


def get_releases_related_to_master_release(user: Union[UserWithoutAuthentication,
                                                       UserWithUserTokenBasedAuthentication],
                                           master_id: int,
                                           page: Union[int, None] = None,
                                           per_page: Union[int, None] = None,
                                           release_format: Union[str, None] = None,
                                           label: Union[str, None] = None,
                                           released: Union[str, None] = None,
                                           country: Union[str, None] = None,
                                           sort: Union[SortOptionsMaster, None] = None,
                                           sort_order: Union[SortOrder, None] = None) -> requests.models.Response:
    """
    Get a list of all Releases that are versions of a given master release.

    No user Authentication needed.
    """

    url = f"{MASTERS_URL}/{master_id}/versions"
    headers = user.headers
    params = user.params
    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)
    if release_format:
        params["format"] = release_format
    if label:
        params["label"] = label
    if released:
        params["released"] = released
    if country:
        params["country"] = country
    if sort:
        params["sort"] = sort.name
    if sort_order:
        params["sort_order"] = sort_order.name
    return requests.get(url, headers=headers, params=params)

# Cell


def get_artist(user: Union[UserWithoutAuthentication,
                           UserWithUserTokenBasedAuthentication],
               artist_id: int) -> requests.models.Response:
    """
    Get information about an artist.
    An Artist represents a person in the Discogs database who contributed to a Release in some capacity.

    No user Authentication needed.
    """
    url = f"{ARTIST_URL}/{artist_id}"
    headers = user.headers
    params = user.params
    return requests.get(url, headers=headers, params=params)

# Cell


def get_artist_releases(user: Union[UserWithoutAuthentication,
                                    UserWithUserTokenBasedAuthentication],
                        artist_id: int,
                        page: Union[int, None] = None,
                        per_page: Union[int, None] = None,
                        sort: Union[SortOptionsArtist, None] = None,
                        sort_order: Union[SortOrder, None] = None) -> requests.models.Response:
    """
    Get a list of releases and masters associated with the given artist.

    No user Authentication needed.
    """
    url = f"{ARTIST_URL}/{artist_id}/releases"
    headers = user.headers
    params = user.params

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


def get_label(user: Union[UserWithoutAuthentication,
                          UserWithUserTokenBasedAuthentication],
              label_id: int) -> requests.models.Response:
    """
    Get information about an label.
    A label resource represents a label, company,
    recording studio, location, or other entity involved with artists and releases.

    No user Authentication needed.
    """
    url = f"{LABEL_URL}/{label_id}"
    headers = user.headers
    params = user.params

    return requests.get(url, headers=headers, params=params)

# Cell


def get_label_releases(user: Union[UserWithoutAuthentication,
                                   UserWithUserTokenBasedAuthentication],
                       label_id: int,
                       page: Union[int, None] = None,
                       per_page: Union[int, None] = None,
                       sort: Union[SortOptionsLabel, None] = None,
                       sort_order: Union[SortOrder, None] = None) -> requests.models.Response:
    """
    Get a list of releases and masters associated with the given label.

    No user Authentication needed.
    """
    url = f"{LABEL_URL}/{label_id}/releases"
    headers = user.headers
    params = user.params

    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)
    if sort:
        params["sort"] = sort.name
    if sort_order:
        params["sort_order"] = sort_order.name

    return requests.get(url, headers=headers, params=params)