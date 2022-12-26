# Goodware

This is an executable that unpacks a base64 encoded shellcode. This shellcode performs AES-128 encryption of flag file using AES-NI instruction set.

The encryption algorithm is written entirely x86_64 assembly. It is a modified AES-128 encryption having 16 rounds and modified round constants (powers of 3 modulo 256 ). To demonstrate decryption, I stole an AES python script from github and modified it accordingly. Moreover, CBC is used as the block mode.

A portion of the key expansion algorithm had to be taken from Intel's official docs coz frankly AESKEYASSISTGEN made no sense at all. 
Fun blooper note: I intended it to be a full fledged malware that parses through every file in the directory, but parsing results of getdents64 syscall is a pain in the arse so maybe I'll make it a separate project in the future.