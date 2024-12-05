def success_message(msg="succes"):
    etoiles = '*'*50
    print(f"\033[1;32m{etoiles}\033[0m")
    print(f"\033[1;32m {msg}\033[0m")
    print(f"\033[1;32m{etoiles}\033[0m")
    

def error_message(msg="Erreur"):
    etoiles = '*'*50
    print(f"\033[1;31m{etoiles}\033[0m")
    print(f"\033[1;31m {msg}\033[0m")
    print(f"\033[1;31m{etoiles}\033[0m")