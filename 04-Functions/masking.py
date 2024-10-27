def hide(card_number):

    if len(card_number) != 16 or not card_number.isdigit():
        return "Card number must be a 16-digit number."

    masked_number = card_number[:2] + '*' * 10 + card_number[-4:]
    
    return masked_number