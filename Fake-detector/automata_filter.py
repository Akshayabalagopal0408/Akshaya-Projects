import re

def automata_detect(message):
    message = message.lower()
    spam_patterns = [
        r"(free\s+money|win\s+cash|congratulations|urgent\s+action)",
        r"(click\s+here|limited\s+offer|claim\s+now)",
        r"(http[s]?://|www\.)",  # URLs
        r"(\d{10,})"  # long number strings
    ]
    
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return "Spam (Detected by Automata)"
    
    return "Genuine (Passed Automata)"
