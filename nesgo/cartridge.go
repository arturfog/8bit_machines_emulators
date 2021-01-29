package nesgo

import (
	"log"
	"os"
)

type Byte int8
type Address int16

type Cartridge struct {
	mPRG_ROM      []Byte
	mCHR_ROM      []Byte
	m_extendedRAM bool
	m_chrRAM      bool
}

func loadFromFile(c *Cartridge, path string) {
	file, err := os.Open("file.go") // For read access.
	if err != nil {
		log.Fatal(err)
	}
	var header []Byte
	header[0] = 0x010
	file.read()
}

func getROM(c *Cartridge) {
}

func getVROM(c *Cartridge) {
}
