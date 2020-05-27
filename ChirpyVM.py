# Chirpy v0.01
from sys import stdin,stdout

class ChirpyVM:
    def __init__(this,code,pc=0):
        this.code = list(code)
        this.pc = pc
        this.halted = False
        this.N = False
        this.A = this.B = this.ib = 0
    def step(this):
        op = this.ib&15
        this.ib >>= 4
        if op == 0: # no-op / next ib
            this.ib = this.code[this.pc]
            this.pc += 1
        elif op == 1: # lit
            this.A = this.code[this.pc]
            this.pc += 1
        elif op == 2: # inp
            this.A = ord(stdin.read(1)[0])&0xff
        elif op == 3: # out
            stdout.write(chr(this.A&0xff))
        elif op == 4: # fetch
            this.A = this.code[this.A]
        elif op == 5: # store
            this.code[this.A] = this.B
        elif op == 6: # swap
            this.A,this.B = this.B, this.A
        elif op == 7: # sub
            this.A = this.A-this.B
            this.N = this.A < 0
        elif op == 8: # jn d
            a = this.code[this.pc]
            this.pc += 1
            if this.N:
                this.pc = a
                this.ib = this.code[this.pc]
                this.pc += 1
        elif op == 15: # halt
            this.halted = True
        else:
            raise Exception("unknown opcode %r"%op)
    def __call__(this,cycles=1):
        while cycles > 0 and not this.halted:
            cycles-=1
            this.step()
        return cycles

            
