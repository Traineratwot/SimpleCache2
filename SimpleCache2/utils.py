import hashlib


def get_md5_hash(string: str) -> str:
    md5_hash = hashlib.md5()
    md5_hash.update(string)
    return md5_hash.hexdigest()
