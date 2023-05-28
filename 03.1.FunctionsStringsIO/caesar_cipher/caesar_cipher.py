def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """
    st = ""
    for i in message:
        if 0 <= ord(i)-ord('a') < 26:
            st += chr(((ord(i)-ord('a') + n) % 26) + ord('a'))
        elif 0 <= ord(i)-ord('A') < 26:
            st += chr(((ord(i)-ord('A') + n) % 26) + ord('A'))
        else:
            st += i
    return st
