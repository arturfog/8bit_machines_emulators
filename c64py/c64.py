from . import cpu
from . import memory
from . import cia1
from . import cia2
from . import io

class C64:
    def __init__(self):
        self.cpu = cpu.CPU
        self.mem = memory.Memory
        self.cia1 = cia1.Cia1
        self.cia2 = cia2.Cia2

    def start(self):
        while True:
            if not self.cia1.emulate():
                break
            if not self.cia2.emulate():
                pass