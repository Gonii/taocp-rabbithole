eatsyscall.o: eatsyscall.asm
	nasm -f elf -g -F dwarf eatsyscall.asm

eatsyscall: eatsyscall.o
	ld -o eatsyscall eatsyscall.o -melf_i386
