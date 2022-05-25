sandbox.o: sandbox.asm
	nasm -f elf -g -F dwarf sandbox.asm

sandbox: sandbox.o
	ld -o sandbox sandbox.o -melf_i386
