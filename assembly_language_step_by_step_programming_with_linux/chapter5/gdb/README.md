go build -o gdb_sandbox main.go

gdb gdb_sandbox

break main.go:7

n
