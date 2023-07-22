from django import template

from cards.models import BOXES, Card

register = template.Library()

# tells Django that boxes_as_links is an inclusion tag
@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    boxes = []
    
    # loops over BOXES.
    for box_num in BOXES:
        # keep track of the number of cards in the current box
        card_count = Card.objects.filter(box=box_num).count()
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })
        
    # a dictionary with boxes data.
    return {"boxes": boxes}