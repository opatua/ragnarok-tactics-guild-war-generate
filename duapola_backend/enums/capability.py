from enum import Enum


class Capability(Enum):
    ANY_LIST = 'any:list'
    ANY_RETRIEV = 'any:retrieve'

    ADDRESS_LIST = 'address:list'
    ADDRESS_CREATE = 'address:create'
    ADDRESS_RETRIEVE = 'address:retrieve'
    ADDRESS_UPDATE = 'address:update'
    ADDRESS_DESTROY = 'address:destroy'

    CATEGORY_LIST = 'category:list'
    CATEGORY_CREATE = 'category:create'
    CATEGORY_RETRIEVE = 'category:retrieve'
    CATEGORY_UPDATE = 'category:update'
    CATEGORY_DESTROY = 'category:destroy'

    CART_LIST = 'cart:list'
    CART_CREATE = 'cart:create'
    CART_RETRIEVE = 'cart:retrieve'
    CART_UPDATE = 'cart:update'
    CART_DESTROY = 'cart:destroy'

    CART_ITEM_LIST = 'cart-item:list'
    CART_ITEM_CREATE = 'cart-item:create'
    CART_ITEM_RETRIEVE = 'cart-item:retrieve'
    CART_ITEM_UPDATE = 'cart-item:update'
    CART_ITEM_DESTROY = 'cart-item:destroy'

    CITY_LIST = 'city:list'
    CITY_CREATE = 'city:create'
    CITY_RETRIEVE = 'city:retrieve'
    CITY_UPDATE = 'city:update'
    CITY_DESTROY = 'city:destroy'

    COLOR_LIST = 'color:list'
    COLOR_CREATE = 'color:create'
    COLOR_RETRIEVE = 'color:retrieve'
    COLOR_UPDATE = 'color:update'
    COLOR_DESTROY = 'color:destroy'

    COUNTRY_LIST = 'country:list'
    COUNTRY_CREATE = 'country:create'
    COUNTRY_RETRIEVE = 'country:retrieve'
    COUNTRY_UPDATE = 'country:update'
    COUNTRY_DESTROY = 'country:destroy'

    CURRENCY_LIST = 'currency:list'
    CURRENCY_CREATE = 'currency:create'
    CURRENCY_RETRIEVE = 'currency:retrieve'
    CURRENCY_UPDATE = 'currency:update'
    CURRENCY_DESTROY = 'currency:destroy'

    PRODUCT_FAMILY_LIST = 'product-family:list'
    PRODUCT_FAMILY_CREATE = 'product-family:create'
    PRODUCT_FAMILY_RETRIEVE = 'product-family:retrieve'
    PRODUCT_FAMILY_UPDATE = 'product-family:update'
    PRODUCT_FAMILY_DESTROY = 'product-family:destroy'

    PRODUCT_INVENTORY_LIST = 'product-inventory:list'
    PRODUCT_INVENTORY_CREATE = 'product-inventory:create'
    PRODUCT_INVENTORY_RETRIEVE = 'product-inventory:retrieve'
    PRODUCT_INVENTORY_UPDATE = 'product-inventory:update'
    PRODUCT_INVENTORY_DESTROY = 'product-inventory:destroy'

    PRODUCT_LIST = 'product:list'
    PRODUCT_CREATE = 'product:create'
    PRODUCT_RETRIEVE = 'product:retrieve'
    PRODUCT_UPDATE = 'product:update'
    PRODUCT_DESTROY = 'product:destroy'

    USER_LIST = 'user:list'
    USER_CREATE = 'user:create'
    USER_RETRIEVE = 'user:retrieve'
    USER_UPDATE = 'user:update'
    USER_DESTROY = 'user:destroy'
