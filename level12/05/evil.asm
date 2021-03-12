;  Clicking button saves & builds using commands:
;    nasm -f elf -g -F stabs evil.asm
;    ld -o evil evil.o
section .data
Snippet: db "@E9>06G@Q:CN3C57I<)<)*"
SnipLen: equ $-Snippet
section .text
global _start
_start:
        mov ecx,Snippet ;set Snippet address to the ecx register
        mov edx,SnipLen ;set SnipLen to the edx register
        mov eax,6 ; set eax register to 6
DoMore: add byte [ecx], al ; move value in ecx to memory address af
        inc ecx; increment ecx register
        inc eax ; increment eax register
        dec edx ; decrease edx register
        jnz DoMore ; jump to DoMore if dec edx returns 0
        mov eax,4 ; move 4 to eax
        mov ebx,1 ; move 1 to ebx
        sub ecx,SnipLen ; subtract SnipLen address
        mov edx,SnipLen ; move address in edx to memory address Sniplen
        int 80H ; system call
        mov eax,1 ; set eax address to 1
        mov ebx,0 ; set ebx address to 0
        int 80H ; system call