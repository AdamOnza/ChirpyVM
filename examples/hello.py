# print "hello, world.\n" using one massive word full-O-opcodes
from chirpyVM import ChirpyVM
vm = ChirpyVM([0xf3131313131313131313131313131, 72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 46,10])
vm(1000)
