import hashlib

def hash_fn(text):
    h = hashlib.new('sha512_256')
    h.update(text.encode('utf-8'))
    return h.hexdigest()