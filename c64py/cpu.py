class CPU:
    def init(self):
        self._pc, self._sp: int
        self._cycles: int
        self._cf, self._zf, self._idf, self._dmf, self._bcf, self._of, self._nf: bool
        self._a, self._x, self._y: int

    def tick(self, v: int):
        self._cycles += v

    def pc(self):
        return self._pc

    def sp(self):
        return self._sp

    def a():
        pass

    def x():
        pass

    def y():
        pass

    def reset(self):
        self._cf = false
        self._zf = false
        self._cycles = 6

    def emulate(self):
        insn: int = self.fetch_op();
        retval: bool = true
        if insn == 0x0:
            brk()
        if insn == 0x1:
            ora(load_byte(addr_indx()), 6)


    def load_byte(addr: int):
        pass

    def push(v: int):
        pass

    def pop():
        pass

    def fetch_op(self):
        self._pc += 1
        return load_byte(self._pc)

    def fetch_opw():
        pass

    def addr_zero():
        addr = fetch_op();
        return addr

    def addr_zerox():
        addr = ( fetch_op() + x() ) & 0xff
        return addr

    def addr_zeroy():
        addr = ( fetch_op() + y() ) & 0xff
        return addr

    def addr_abs():
        addr = fetch_opw()
        return addr

    def addr_absy():
        pass

    def addr_absx():
        pass

    def addr_indx():
        pass

    def addr_indy():
        pass

    def sta(add: int, cycles: int):
        pass

    def stx(addr: int, cycles: int):
        pass

    def sty(addr: int, cycles: int):
        pass

    def txs():
        sp(x())
        tick(2)

    def tsx():
        x(sp())
        tick(2)

    def lda(v: int, cycles: int):
        a(v)
        tick(cycles)

    def ldx(v: int, cycles: int):
        pass

    def ldy(v: int, cycles: int):
        pass

    def txa():
        pass

    def tax():
        pass

    def tay():
        y(a())
        tick(2)

    def tya():
        a(y())
        tick(2)

    def pha():
        push(a())
        tick(3)

    def pla():
        a(pop())
        tick(4)

    def ora(v: int, cycles: int):
        a( a()|v )
        tick(cycles)

    def and(v: int, cycles: int):
        tick(cycles)

    def bit(addr: int, cycles: int):
        pass

    def rol(v: int):
        pass

    def rol_a():
        pass

    def rol_mem(addr: int, cycles:int):
        pass

    def ror(v: int):
        pass

    def ror_a():
        pass

    def ror_mem(addr: int, cycles: int):
        pass

    def lsr(v: int):
        pass

    def lsr_a():
        pass

    def lsr_mem(addr: int, cycles: int):
        pass

    def asl(v: int):
        pass

    def asl_a():
        pass

    def asl_mem(self, addr: int, cycles: int):
        tick(cycles)

    def eor(v: int, cycles: int):
        pass

    def inc(addr: int, cycles: int):
        pass

    def dec(addr: int, cycles: int):
        pass

    def inx():
        pass

    def iny():
        pass

    def dex():
        pass

    def dey():
        pass

    def adc(v: int, cycles: int):
        pass

    def sbc():
        pass

    def sei():
        pass

    def cli():
        pass

    def sec():
        pass

    def clc():
        pass

    def sed():
        pass

    def cld():
        pass

    def clv():
        pass

    def flags():
        v: int
        return v

    def flags(v: int):
        pass

    def php():
        pass

    def plp():
        pass

    def jsr():
        pass

    def jmp():
        pass

    def jmp_ind():
        pass

    def rts():
        pass

    def bne():
        pass

    def cmp():
        pass

    def cpx():
        pass

    def cpy():
        pass

    def beq():
        pass

    def bcs():
        pass

    def bcc():
        pass

    def bpl():
        pass

    def bmi():
        pass

    def bvc():
        pass

    def bvs():
        pass

    def nop():
        tick(2)

    def brk():
        push( ( ( pc() + 1 ) >> 8 ) & 0xff)
        push( ( ( pc() + 1 ) & 0xff) )
        push(flags())
        # TODO: finish
        pc()
        idf(true)
        bcf(true)
        tick(7)

    def rti():
        flags(pop())
        pc(pop() + (pop() << 8))
        tick(7)

    def irq():
        if not idf():
            push( ( ( pc() + 1 ) >> 8 ) & 0xff)
            push( ( ( pc() + 1 ) & 0xff) )
            push(flags())
            # TODO: finish
            pc()
            idf(true)
            tick(7)

    def nmi():
        push( ( ( pc() + 1 ) >> 8 ) & 0xff)
        push( ( ( pc() + 1 ) & 0xff) )
        push( ( flags() & 0xef) )
        # TODO: finish
        pc()
        tick(7)
