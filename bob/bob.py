def response(hey_bob:str):
    match hey_bob:
        case _ if hey_bob.strip().endswith('?') and not hey_bob.isupper() :
            return 'Sure.'
        case _ if hey_bob.isupper() and not hey_bob.endswith('?'):
            return "Whoa, chill out!"
        case _ if hey_bob.isupper() and hey_bob.endswith('?'):
            return "Calm down, I know what I'm doing!"
        case _ if not hey_bob or hey_bob.isspace():
            return "Fine. Be that way!"
        case _ :
            return "Whatever."
