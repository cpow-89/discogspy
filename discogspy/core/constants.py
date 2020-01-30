# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.constants.ipynb (unless otherwise specified).

__all__ = ['BASE_URL', 'RELEASES_URL', 'MASTERS_URL', 'ARTIST_URL', 'LABEL_URL', 'USERS_URL', 'MARKETPLACE_URL',
           'LISTINGS_URL', 'ORDERS_URL', 'FEE_URL', 'PRICE_SUGGESTIONS_URL', 'INVENTORY_URL', 'INVENTORY_EXPORT_URL',
           'CurrAbbr', 'SortOptionsMaster', 'SortOptionsArtist', 'SortOptionsLabel', 'SortOptionsInventory',
           'SortOptionsOrders', 'SortOrder', 'StatusInventory', 'StatusNewListing', 'StatusOrder', 'StatusOrders',
           'ReleaseCondition', 'SleeveCondition']

# Cell
from enum import Enum

# Cell


BASE_URL = "https://api.discogs.com"
RELEASES_URL = f"{BASE_URL}/releases"
MASTERS_URL = f"{BASE_URL}/masters"
ARTIST_URL = f"{BASE_URL}/artists"
LABEL_URL = f"{BASE_URL}/labels"
USERS_URL = f"{BASE_URL}/users"
MARKETPLACE_URL = f"{BASE_URL}/marketplace"
LISTINGS_URL = f"{MARKETPLACE_URL}/listings"
ORDERS_URL = f"{MARKETPLACE_URL}/orders"
FEE_URL = f"{MARKETPLACE_URL}/fee"
PRICE_SUGGESTIONS_URL = f"{MARKETPLACE_URL}/price_suggestions"
INVENTORY_URL = f"{BASE_URL}/inventory"
INVENTORY_EXPORT_URL = f"{INVENTORY_URL}/export"

# Cell


class CurrAbbr(Enum):
    """
    Valid currencies for marketplace data
    """

    USD = "USD"
    GBP = "GBP"
    EUR = "EUR"
    CAD = "CAD"
    AUD = "AUD"
    JPY = "JPY"
    CHF = "CHF"
    MXN = "MXN"
    BRL = "BRL"
    NZD = "NZD"
    SEK = "SEK"
    ZAR = "ZAR"


# Cell


class SortOptionsMaster(Enum):
    """
    Valid sort options for master releases.
    """

    released = "released"
    title = "title"
    format = "format"
    label = "label"
    catno = "catno"
    country = "country"


# Cell


class SortOptionsArtist(Enum):
    """
    Valid sort options for artist releases.
    """

    year = "year"
    title = "title"
    format = "format"


# Cell


class SortOptionsLabel(Enum):
    """
    Valid sort options for label releases.
    """

    year = "year"
    title = "title"
    format = "format"

# Cell


class SortOptionsInventory(Enum):
    """
    Valid sort options for inventory.
    """

    listed = "listed"
    price = "price"
    item = "item"
    artist = "artist"
    label = "label"
    catno = "catno"
    audio = "audio"
    status = "status" # when authenticated as the inventory owner
    location = "location" # when authenticated as the inventory owner


# Cell


class SortOptionsOrders(Enum):
    """
    Valid sort options for orders.
    """

    id = "id"
    buyer = "buyer"
    created = "created"
    status = "status"
    last_activity = "last_activity"

# Cell


class SortOrder(Enum):
    """
    Valid sort order options.
    """

    asc = "asc"
    desc = "desc"

# Cell


class StatusInventory(Enum):
    """
    Valid status options for inventory items.
    """

    for_sale = "For Sale"
    sold = "Sold"
    draft = "Draft"
    expired = "Expired"

# Cell


class StatusNewListing(Enum):
    """
    Valid status options for inventory listing.
    """

    for_sale = "For Sale"
    draft = "Draft"


# Cell


class StatusOrder(Enum):
    """
    Valid status options for updating an order.
    """

    new_order = "New Order"
    buyer_contacted = "Buyer Contacted"
    invoice_sent = "Invoice Sent"
    payment_pending = "Payment Pending"
    payment_received = "Payment Received"
    shipped = "Shipped"
    refund_sent = "Refund Sent"
    cancelled_no_payment = "Cancelled (Non-Paying Buyer)"
    cancelled_item_unavailable = "Cancelled (Item Unavailable)"
    cancelled_buyer_request = "Cancelled (Per Buyer's Request)"

# Cell


class StatusOrders(Enum):
    """
    Valid status options for filtering order list.
    """

    all = "All"
    new_order = "New Order"
    invoice_sent = "Invoice Sent"
    buyer_contacted = "Buyer Contacted"
    payment_pending = "Payment Pending"
    payment_received = "Payment Received"
    shipped = "Shipped"
    merged = "Merged"
    order_changed = "Order Changed"
    refund_sent = "Refund Sent"
    cancelled = "Cancelled"
    cancelled_no_payment = "Cancelled (Non-Paying Buyer)"
    cancelled_item_unavailable = "Cancelled (Item Unavailable)"
    cancelled_buyer_request = "Cancelled (Per Buyer's Request)"
    cancelled_refund_received = "Cancelled (Refund Received)"

# Cell


class ReleaseCondition(Enum):
    """
    Valid release conditions.
    """

    mint = "Mint (M)"
    near_mint = "Near Mint (NM or M-)"
    very_good_plus = "Very Good Plus (VG+)"
    very_good = "Very Good (VG)"
    good_plus = "Good Plus (G+)"
    good = "Good (G)"
    fair = "Fair (F)"
    poor = "Poor (P)"


# Cell


class SleeveCondition(Enum):
    """
    Valid listing conditions.
    """

    mint = "Mint (M)"
    near_mint = "Near Mint (NM or M-)"
    very_good_plus = "Very Good Plus (VG+)"
    very_good = "Very Good (VG)"
    good_plus = "Good Plus (G+)"
    good = "Good (G)"
    fair = "Fair (F)"
    poor = "Poor (P)"
    generic = "Generic"
    not_graded = "Not Graded"
    no_cover = "No Cover"
