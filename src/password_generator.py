import random
import string

def generate_password(lenght: int = 12, use_digits: bool = True, use_specials: bool = True) -> str:
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += "!@#$%^&*"
    

    if not chars:
        return "Mistake: change 1 symbol"
    
    return ''.join(random.choice(chars) for _ in range(lenght))
