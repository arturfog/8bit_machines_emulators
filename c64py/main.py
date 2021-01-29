from . import c64
from . import loader

def loader_cb() -> bool:
    if not loader.emulate():
        pass
    return True

def load_file(f: str):
    pass

if __name__ == main:
    c64 = c64.C64()
    loader = loader.Loader()

    load_file("/tmp/test.rom")
    c64.start()