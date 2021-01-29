class Cia1:
    def __init__(self):
        self.timer_a_enabled: int = 0
        self.timer_a_irq_enabled: int = 0
        self.timer_a_irq_triggered: int = 0

        self.timer_b_enabled: int = 0
        self.timer_b_irq_enabled: int = 0
        self.timer_b_irq_triggered: int = 0

        self.timer_a_latch: int = 0
        self.timer_a_counter: int = 0

        self.timer_a_input_mode
        self.timer_b_input_mode

        self.timer_a_run_mode
        self.timer_b_run_mode

        self.timer_b_latch: int = 0
        self.timer_b_counter: int = 0
        
        self.pra: int = 0xff
        self.prb: int = 0xff

    def write_register(r: int, v: int):
        if r == 0x0:
            self.pra = v
        if r == 0x1:
            pass
        if r == 0x2:
            pass
        if r == 0x3:
            pass
        if r == 0x4:
            self.timer_a_latch &= 0x00ff

    def read_register(r: int):
        if r == 0x0:
            pass

    def reset_timer_a():
        pass

    def reset_timer_b():
        pass
    # /**
    #  * @brief retrieves vic base address
    #  *
    #  * PRA bits (0..1)
    #  *
    #  *  %00, 0: Bank 3: $C000-$FFFF, 49152-65535
    #  *  %01, 1: Bank 2: $8000-$BFFF, 32768-49151
    #  *  %10, 2: Bank 1: $4000-$7FFF, 16384-32767
    #  *  %11, 3: Bank 0: $0000-$3FFF, 0-16383 (standard)
    #  */
    def vic_base_address(self) -> int:
        return ( (~self.pra & 0x3) << 14 )

    def emulate() -> bool:
        return True