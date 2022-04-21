

def vdir(obj):
    return [x for x in dir(obj) if not x.startswith("__")]
