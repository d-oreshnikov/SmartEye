import hashlib


def get_hash(string):

  hasher = hashlib.sha256()
  encoded_string = string.encode()
  hasher.update(encoded_string)
  return hasher.hexdigest()
