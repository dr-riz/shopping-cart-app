from typing import Union
from .scorer.apex import ApexShoppingCartScorer
from .scorer.base import BaseShoppingCartScorer

def score_shopping_cart(scorer_type: str) -> Union[ApexShoppingCartScorer, BaseShoppingCartScorer]:
    if scorer_type == 'apex':
        return ApexShoppingCartScorer()
    elif scorer_type == 'base':
        return BaseShoppingCartScorer()
    else:
        raise ValueError(f"Invalid scorer type: {scorer_type}")
