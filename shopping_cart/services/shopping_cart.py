from dataclasses import dataclass
from typing import List, Optional   

from ..domain.fruit import Fruit
from ..domain.shopping_cart import ShoppingCart
# from ..adapters.scorer import ShoppingCartScorer
from ..adater.scorer import get_scorer

def initialize_shopping_cart() -> ShoppingCart: #/\<ShoppingCart\>
    """
    Initialize a new shopping cart object.
    """
    return ShoppingCart(items=[])


def add_fruit_to_cart(cart: ShoppingCart, fruit: Fruit) -> None:
    """
    Add fruits to the shopping cart.
    """
    cart.items.append(fruit)

def remove_fruit_from_cart(cart: ShoppingCart, fruit_name:str) -> Optional[Fruit]:
    """
    Remove fruit by name from the shopping cart.
    """

    for idx, item in enumerate(cart.items):
        if item.name == fruit_name:
            return cart.items.pop(idx)
        
    return None

def score_shopping_cart(cart: ShoppingCart):
    """
    Assign a score the shopping cart
    based on the contents using an ML model.
    """
    # scorer = ShoppingCartScorer()
    scorer = get_scorer()
    cart_score = scorer.score_shopping_cart(cart)
    cart.score = int(cart_score)