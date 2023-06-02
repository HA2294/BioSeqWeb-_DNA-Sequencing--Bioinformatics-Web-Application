# File: L07_01_sqrt.S
# Florida Tech, CSE3120
# Instructor: Marius Silaghi
.code32
.text
.globl main
.type  main, @function
.globl square_root_proc
.type  square_root_proc, @function
square_root_proc:
 ....
   ret
main:
 mov $4, %eax
 call square_root_proc
 mov %eax, %ebx # exit code
 mov $1, %eax # exit syscall
int $0x80
