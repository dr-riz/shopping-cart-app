from apex_scorer import shopping_cart_scorer
from ...domain.shopping_cart import ShoppingCart

class ApexShoppingCartScorer:
    def __init__(self):
        pass

    def score_shopping_cart(self, shopping_cart : ShoppingCart) -> int:
        return shopping_cart_scorer