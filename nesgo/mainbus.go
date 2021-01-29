package nesgo

const (
	PPUCTRL   = 0x2000
	PPUMASK   = 0x2001
	PPUSTATUS = 0x2002
	OAMADDR   = 0x2003
	OAMDATA   = 0x2004
	PPUSCROL  = 0x2005
	PPUADDR   = 0x2006
	PPUDATA   = 0x2007
	OAMDMA    = 0x4014
	JOY1      = 0x4016
	JOY2      = 0x4017
)

type MainBus struct {
	m_Ram    []Byte
	m_extRam []Byte
}

func read(mb *MainBus) {

}

func write(mb *MainBus) {

}
