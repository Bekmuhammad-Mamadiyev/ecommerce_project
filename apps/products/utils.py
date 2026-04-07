from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
#
def validate_rating(rank):
    if rank > 5:
        raise ValidationError(_('Rank must be between 0 and 5'))
    return rank
#
#
# # services.py yoki utils.py
# from django.core.cache import cache
# from .models import Product
#
#
# def get_cached_home_products(limit=10):
#     cache_key = f"home_top_products_{limit}"
#     products = cache.get(cache_key)
#
#     if not products:
#         products = list(Product.active_objects.filter(discount__gt=0).order_by('-discount')[:limit])
#
#         cache.set(cache_key, products, timeout=60 * 15)
#
#     return products