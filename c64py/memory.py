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
    kMemSize = 0x10000;
    # /* memory addresses  */
    kBaseAddrBasic  = 0xa000;
    kBaseAddrKernal = 0xe000;
    kBaseAddrStack  = 0x0100;
    kBaseAddrScreen = 0x0400;
    kBaseAddrChars  = 0xd000;
    kBaseAddrBitmap = 0x0000;
    kBaseAddrColorRAM = 0xd800;
    kAddrResetVector = 0xfffc;
    kAddrIRQVector = 0xfffe;
    kAddrNMIVector = 0xfffa;
    kAddrDataDirection = 0x0000;
    kAddrMemoryLayout  = 0x0001;
    kAddrColorRAM = 0xd800;
    # /* memory layout */
    kAddrZeroPage     = 0x0000;
    kAddrVicFirstPage = 0xd000;
    kAddrVicLastPage  = 0xd300;
    kAddrCIA1Page = 0xdc00;
    kAddrCIA2Page = 0xdd00;
    kAddrBasicFirstPage = 0xa000; 
    kAddrBasicLastPage  = 0xbf00;
    kAddrKernalFirstPage = 0xe000;
    kAddrKernalLastPage = 0xff00;
    # /* bank switching */
    kLORAM  = 1 << 0;
    kHIRAM  = 1 << 1;
    kCHAREN = 1 << 2;

    def __init__(self):
        self.banks = [None] * 7
        self.mem_ram = [None] * kMemSize
        self.mem_rom = [None] * kMemSize

    # /**
    # * @brief configure memory banks
    # *
    # * There are five latch bits that control the configuration allowing
    # * for a total of 32 different memory layouts, for now we only take
    # * in count three bits : HIRAM/LORAM/CHAREN
    # */
    def setup_memory_banks(v: int):
        hiram: bool = ( (v & kHIRAM) != 0 )
        loram: bool = ( (v & kLORAM) != 0 )

        load_rom("basic.901226-01.bin", kBaseAddrBasic)
        load_rom("characters.901225-01.bin", kBaseAddrChars)
        load_rom("kernal.901227-03.bin", kBaseAddrKernal)

    def write_byte(addr: int, v: int):
        pass

    def read_byte(addr: int):
        retval = 0
        page = addr & 0xff00

    def load_rom(f: str, baseaddr: int):
        pass

    def load_ram(f: str, baseaddr: int):
        pass

    def dump():
        pass
