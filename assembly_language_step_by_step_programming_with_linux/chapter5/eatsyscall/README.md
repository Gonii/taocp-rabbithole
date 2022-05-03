### build commands for running x86 assembly in x86_64

# -F stabs "breaks" breakpoints, dwarf works for some reason
nasm -f elf -g -F dwarf eatsyscall.asm
ld -o eatsyscall eatsyscall.o -melf_i386
