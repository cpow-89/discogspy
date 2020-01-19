# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.constants.ipynb (unless otherwise specified).

__all__ = ['BASE_URL', 'RELEASES_URL', 'MASTERS_URL', 'ARTIST_URL', 'LABEL_URL', 'VALID_CURR_ABBR',
           'VALID_SORT_OPTIONS_MASTERS', 'VALID_SORT_OPTIONS_ARTIST', 'VALID_SORT_OPTIONS_LABEL', 'VALID_SORT_ORDER']

# Cell
BASE_URL = "https://api.discogs.com"
RELEASES_URL = f"{BASE_URL}/releases"
MASTERS_URL = f"{BASE_URL}/masters"
ARTIST_URL = f"{BASE_URL}/artists"
LABEL_URL = f"{BASE_URL}/labels"

"""Valid currencies for marketplace data"""
VALID_CURR_ABBR = ["USD", "GBP", "EUR", "CAD", "AUD", "JPY",
                   "CHF", "MXN", "BRL", "NZD", "SEK", "ZAR"]

"""Valid sort options"""
VALID_SORT_OPTIONS_MASTERS = ["released", "title", "format", "label", "catno", "country"]
VALID_SORT_OPTIONS_ARTIST = ["year", "title", "format"]
VALID_SORT_OPTIONS_LABEL = ["year", "title", "format"]

"""Valid sort options"""
VALID_SORT_ORDER = ["asc", "desc"]