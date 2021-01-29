class CPU {
    getCurrentOpcode()
    {
        let opcode = 0;
        return opcode;
    }

    reset()
    {
        SP = 0xFFFE;
        PC = 0x0100;
    }
}
