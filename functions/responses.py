import random

def get_response(message: str) -> str:
    proc_message = message.lower().strip()

    if proc_message == "hello":
        return f"Hey there!"
    
    if message == "roll":
        return str(random.randint(1,6))
    
    if proc_message == "!help":
        return "no"

    else:
        return "I didn't understand your message."