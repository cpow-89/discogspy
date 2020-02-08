# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_core.rq_database.ipynb (unless otherwise specified).

__all__ = ['get_release', 'get_user_release_rating', 'update_user_release_rating', 'delete_user_release_rating',
           'get_community_release_rating', 'get_master_release', 'get_releases_related_to_master_release', 'get_artist',
           'get_artist_releases', 'get_label', 'get_label_releases']

# Cell
import requests
from typing import Union
from . import *

# Cell


def get_release(user: Union[UserWithoutAuthentication,
                            UserWithUserTokenBasedAuthentication],
                release_id: int,
                curr_abbr: Union[CurrAbbr, None] = None
                ) -> requests.models.Response:
    """
    Get information about a particular release from the Discogs database.
    A release represents a particular physical or digital object released by
    one or more Artists.

    No user Authentication needed.

    Parameter
    ----------
    user: user object

    release_id : number (required)
        The Release ID.

    curr_abbr: string (optional)
        Currency for marketplace data. Defaults to the authenticated users currency.
    """
    url = f"{RELEASES_URL}/{release_id}"
    headers = user.headers
    params = user.params
    if curr_abbr:
        params["curr_abbr"] = curr_abbr.value
    return requests.get(url, headers=headers, params=params)

# Cell


def get_user_release_rating(user: Union[UserWithoutAuthentication,
                                        UserWithUserTokenBasedAuthentication],
                            release_id: int,
                            username: str
                            ) -> requests.models.Response:
    """
    Get the rating of a release made by the given user.

    No user Authentication needed.

    Parameters
    ----------
    user: user object

    release_id : number (required)
        The Release ID.

    username: string (required)
        The username of the rating you are trying to request.
    """
    url = f"{RELEASES_URL}/{release_id}/rating/{username}"
    headers = user.headers
    params = user.params
    return requests.get(url, headers=headers, params=params)

# Cell


def update_user_release_rating(user: UserWithUserTokenBasedAuthentication,
                               release_id: int,
                               username: str,
                               rating: int
                               ) -> requests.models.Response:
    """
    Update the rating of a release made by the given user.
    If there is no rating, it will create one.

    User Authentication needed.

    Parameters
    ----------
    user: user object

    release_id : number (required)
        The Release ID.

    username: string (required)
        The username of the rating you are trying to request.

    rating: int (required)
        The new rating value. Must be a value between 1 and 5.

    """
    url = f"{RELEASES_URL}/{release_id}/rating/{username}"
    headers = user.headers
    params = user.params
    rating = min(max(0, rating), 5)
    data = {"rating": rating}
    return requests.put(url, headers=headers, params=params, json=data)

# Cell


def delete_user_release_rating(user: UserWithUserTokenBasedAuthentication,
                               release_id: int,
                               username: str
                               ) -> requests.models.Response:
    """
    Delete the rating of a release made by the given user.

    User Authentication needed.

    Parameters
    ----------
    user: user object

    release_id : number (required)
        The Release ID.

    username: string (required)
        The username of the rating you are trying to delete.

    """
    url = f"{RELEASES_URL}/{release_id}/rating/{username}"
    headers = user.headers
    params = user.params
    return requests.delete(url, headers=headers, params=params)

# Cell


def get_community_release_rating(user: Union[UserWithoutAuthentication,
                                             UserWithUserTokenBasedAuthentication],
                                 release_id: int
                                 ) -> requests.models.Response:
    """
    Get the rating of a release made by the community.
    A community release rating includes the average rating and
    the total number of user ratings for a given release.

    This function doesn't work for master releases!

    No user Authentication needed.

    Parameters
    ----------
    user: user object

    release_id : number (required)
        The Release ID.

    """
    url = f"{RELEASES_URL}/{release_id}/rating"
    headers = user.headers
    params = user.params
    return requests.get(url, headers=headers, params=params)

# Cell


def get_master_release(user: Union[UserWithoutAuthentication,
                                   UserWithUserTokenBasedAuthentication],
                       master_id: int
                       ) -> requests.models.Response:
    """
    Get information to a particular master release from Discogs database.
    A Master release represents a set of similar Releases.
    Masters releases have a “main release” which is often the chronologically earliest.

    No user Authentication needed.

    Parameters
    ----------
    user: user object

    master_id : number (required)
        The Master ID.

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
                                           sort_order: Union[SortOrder, None] = None
                                           ) -> requests.models.Response:
    """
    Get a list of all Releases that are versions of the given master release.

    No user Authentication needed.

    Parameters
    ----------
    user: user object.

    master_id : number (required)
        The Master ID.

    page: number (optional)
        The page you want to request.

    per_page: number (optional)
        The number of items per page.

    release_format: string (optional)
        The format to filter.

    label: string (optional)
        The label to filter.

    released: string (optional)
        The release year to filter.

    country: string (optional)
        The country to filter.

    sort: string (optional)
        Sort items by this field.

    sort_order: string (optional)
        Sort items in a particular order (one of asc, desc)
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
        params["sort"] = sort.value
    if sort_order:
        params["sort_order"] = sort_order.value
    return requests.get(url, headers=headers, params=params)

# Cell


def get_artist(user: Union[UserWithoutAuthentication,
                           UserWithUserTokenBasedAuthentication],
               artist_id: int
               ) -> requests.models.Response:
    """
    Get information about an artist.

    No user Authentication needed.

    Parameters
    ----------
    user: user object.

    artist_id : number (required)
        The Artist ID.

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
                        sort_order: Union[SortOrder, None] = None
                        ) -> requests.models.Response:
    """
    Get a list of releases and masters associated with the given artist.

    No user Authentication needed.

    Parameters
    ----------
    user: user object.

    artist_id : number (required)
        The Artist ID.

    page: number (optional)
        The page you want to request.

    per_page: number (optional)
        The number of items per page.

    sort: string (optional)
        Sort items by this field.

    sort_order: string (optional)
        Sort items in a particular order (one of asc, desc)
    """
    url = f"{ARTIST_URL}/{artist_id}/releases"
    headers = user.headers
    params = user.params

    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)
    if sort:
        params["sort"] = sort.value
    if sort_order:
        params["sort_order"] = sort_order.value

    return requests.get(url, headers=headers, params=params)

# Cell


def get_label(user: Union[UserWithoutAuthentication,
                          UserWithUserTokenBasedAuthentication],
              label_id: int
              ) -> requests.models.Response:
    """
    Get information about a label.

    No user Authentication needed.

    Parameters
    ----------
    user: user object.

    label_id : number (required)
        The Label ID.

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
                       sort_order: Union[SortOrder, None] = None
                       ) -> requests.models.Response:
    """
    Get a list of releases and masters associated with the given label.

    No user Authentication needed.

    Parameters
    ----------
    user: user object.

    label_id : number (required)
        The Label ID.

    page: number (optional)
        The page you want to request.

    per_page: number (optional)
        The number of items per page.

    sort: string (optional)
        Sort items by this field.

    sort_order: string (optional)
        Sort items in a particular order (one of asc, desc)
    """
    url = f"{LABEL_URL}/{label_id}/releases"
    headers = user.headers
    params = user.params

    if page:
        params["page"] = max(1, page)
    if per_page:
        params["per_page"] = max(1, per_page)
    if sort:
        params["sort"] = sort.value
    if sort_order:
        params["sort_order"] = sort_order.value

    return requests.get(url, headers=headers, params=params)