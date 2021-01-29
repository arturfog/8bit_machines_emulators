# /**
#  * @brief DRAM
#  *
#  * - @c $0000-$00FF  Page 0        Zeropage addressing
#  * - @c $0100-$01FF  Page 1        Enhanced Zeropage contains the stack
#  * - @c $0200-$02FF  Page 2        Operating System and BASIC pointers
#  * - @c $0300-$03FF  Page 3        Operating System and BASIC pointers
#  * - @c $0400-$07FF  Page 4-7      Screen Memory
#  * - @c $0800-$9FFF  Page 8-159    Free BASIC program storage area (38911 bytes)
#  * - @c $A000-$BFFF  Page 160-191  Free machine language program storage area (when switched-out with ROM)
#  * - @c $C000-$CFFF  Page 192-207  Free machine language program storage area
#  * - @c $D000-$D3FF  Page 208-211  
#  * - @c $D400-$D4FF  Page 212-215  
#  * - @c $D800-$DBFF  Page 216-219  
#  * - @c $DC00-$DCFF  Page 220  
#  * - @c $DD00-$DDFF  Page 221  
#  * - @c $DE00-$DFFF  Page 222-223  Reserved for interface extensions
#  * - @c $E000-$FFFF  Page 224-255  Free machine language program storage area (when switched-out with ROM)
#  */

class Memory:
    # /* constants */
    kMemSize = 0x10000
    # /* memory addresses  */
    kBaseAddrBasic  = 0xa000
    kBaseAddrKernal = 0xe000
    kBaseAddrStack  = 0x0100
    kBaseAddrScreen = 0x0400
    kBaseAddrChars  = 0xd000
    kBaseAddrBitmap = 0x0000
    kBaseAddrColorRAM = 0xd800
    kAddrResetVector = 0xfffc
    kAddrIRQVector = 0xfffe
    kAddrNMIVector = 0xfffa
    kAddrDataDirection = 0x0000
    kAddrMemoryLayout  = 0x0001
    kAddrColorRAM = 0xd800
    # /* memory layout */
    kAddrZeroPage     = 0x0000
    kAddrVicFirstPage = 0xd000
    kAddrVicLastPage  = 0xd300
    kAddrCIA1Page = 0xdc00
    kAddrCIA2Page = 0xdd00
    kAddrBasicFirstPage = 0xa000 
    kAddrBasicLastPage  = 0xbf00
    kAddrKernalFirstPage = 0xe000
    kAddrKernalLastPage = 0xff00
    # /* bank switching */
    kLORAM  = 1 << 0
    kHIRAM  = 1 << 1
    kCHAREN = 1 << 2
    #
    kROM = 0
    kRAM = 1
    kIO = 2
    #
    kBankBasic =  3
    kBankCharen = 5
    kBankKernal = 6

    def __init__(self):
        self.banks = [None] * 7
        self.mem_ram = [None] * Memory.kMemSize
        self.mem_rom = [None] * Memory.kMemSize

    # /**
    # * @brief configure memory banks
    # *
    # * There are five latch bits that control the configuration allowing
    # * for a total of 32 different memory layouts, for now we only take
    # * in count three bits : HIRAM/LORAM/CHAREN
    # */
    def setup_memory_banks(self, v: int):
        hiram: bool  = ( (v & kHIRAM)  != 0 )
        loram: bool  = ( (v & kLORAM)  != 0 )
        charen: bool = ( (v & kCHAREN) ! = 0)

        for i in range(0, len(banks)):
            self.banks[i] = Memory.kRAM
        # load ROMS
        load_rom("basic.901226-01.bin", Memory.kBaseAddrBasic)
        load_rom("characters.901225-01.bin", Memory.kBaseAddrChars)
        load_rom("kernal.901227-03.bin", Memory.kBaseAddrKernal)
        # kernal
        if hiram:
            self.banks[Memory.kBankKernal] = kRom
        # basic
        if loram and hiram:
            self.banks[Memory.kBankBasic] = kRom

        write_byte_no_io(Memory.kAddrMemoryLayout, v)

    def write_byte_no_io(self, addr: int, v: int):
        self.mem_ram[addr] = v

    def write_byte(addr: int, v: int):
        page: int = addr & 0xff00
        if page == Memory.kAddrZeroPage:
            if addr == Memory.kAddrMemoryLayout:
                setup_memory_banks(v)
            else:
                self.mem_ram[addr] = v
        # VIC-II DMA or Character ROM
        elif page >= Memory.kAddrVicFirstPage and page <= Memory.kAddrVicLastPage:
            if banks[Memory.kBankCharen] == Memory.kIO:
                pass
            else:
                self.mem_ram[addr] = v
        # CIA 1
        elif page == Memory.kAddrCIA1Page:
            if banks[Memory.kBankCharen] == Memory.kIO:
                pass
            else:
                self.mem_ram[addr] = v
        # CIA 2
        elif page == Memory.kAddrCIA2Page:
            if banks[Memory.kBankCharen] == Memory.kIO:
                pass
            else:
                self.mem_ram[addr] = v
        # default
        else:
            self.mem_ram[addr] = v

    def read_byte(addr: int):
        retval = 0
        page = addr & 0xff00

        if page >= Memory.kAddrVicFirstPage and page <= Memory.kAddrVicLastPage:
            if self.banks[Memory.kBankCharen] == Memory.kIO:
                pass
            elif self.banks[Memory.kBankCharen] == Memory.kROM:
                retval = self.mem_rom[addr]
            else:
                retval = self.mem_ram[addr]
        else:
            retval = self.mem_ram[addr] 
        return retval
        
    # @brief writes a byte without performing I/O (always to RAM)
    def read_byte_no_io(self, addr: int):
        return self.mem_ram[addr]

    def read_word(self, addr: int):
        return read_byte(addr) | (read_byte(addr + 1) << 8)

    def read_word_no_io(self, addr: int):
        return read_byte_no_io(addr) | (read_byte_no_io(addr + 1) << 8)

    def write_word(self, addr: int, v: int):
        write_byte(addr, v)
        write_byte(addr + 1, v >> 8)

    def write_word_no_io(self, addr: int, v: int):
        write_byte_no_io(addr, v)
        write_byte_no_io(addr + 1, v >> 8)

    # /**
    # * @brief read byte (from VIC's perspective)
    # *
    # * The VIC has only 14 address lines so it can only access 
    # * 16kB of memory at once, the two missing address bits are 
    # * provided by CIA2.
    # *
    # * The VIC always reads from RAM ignoring the memory configuration,
    # * there's one exception: the character generator ROM. Unless the 
    # * Ultimax mode is selected, VIC sees the character generator ROM 
    # * in the memory areas:
    # *
    # *  1000-1FFF
    # *  9000-9FFF
    # */
    def vic_read_byte(addr: int):
        v: int = None
        return v

    def load_rom(f: str, baseaddr: int):
        path = "./assets/roms/" + f
        with open(path) as rom:
            rom.seek(0, os.SEEK_END)
            size = rom.tell()
            # TODO
            self.mem_rom = list(rom.read(size))

    def load_ram(f: str, baseaddr: int):
        path = "./assets/" + f
        with open(path) as rom:
            rom.seek(0, os.SEEK_END)
            size = rom.tell()
            # TODO
            self.mem_ram = list(rom.read(size))

    def dump():
        for i in range(0, Memory.kMemSize):
            print(read_byte(i))
