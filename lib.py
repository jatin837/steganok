def message_to_binary(msg: str) -> str:
    return ''.join([format(ord(i), '08b') for i in msg])

