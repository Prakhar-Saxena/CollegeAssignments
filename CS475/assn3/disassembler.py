#!/usr/bin/env python3

def returnOpcode(opCode):
    opCodeDict = {
        '0x0': "nop",
        '0x1': "ld",
        '0x2': "st",
        '0x3': "br",
        '0x4': "bsr",
        '0x5': "brz",
        '0x6': "bnz",
        '0x7': "brn",
        '0x8': "bnn",
    }
    return opCodeDict[opCode]


def returnSubOpcode(subOpCode):
    subOpCodeDict = {
        '0x0': "nop",
        '0x1': "ldi",
        '0x2': "sti",
        '0x3': "add",
        '0x4': "sub",
        '0x5': "and",
        '0x6': "or",
        '0x7': "xor",
        '0x8': "shl",
        '0x9': "sal",
        '0xa': "shr",
        '0xb': "sar",
        '0x10': "rts",
        '0x1f': "halt",
    }
    return subOpCodeDict[subOpCode]


def getRegName(reg_hex):
    regName = ''
    if len(reg_hex) != 0:
        regName = "r" + str(int(reg_hex, 16))
    return regName


def hextobin(h):
    return bin(int(h, 16))[2:].zfill(len(h) * 4)


def printHeaders():
    print("Address    Instructions")
    print("-" * 40)


def printInstruction(addrs, instruction, param1, param2, param3=''):
    print("{0:#0{1}x}".format(addrs, 6), "   ", "{:5}".format(instruction), "{:5}".format(param1),
          "{:5}".format(param2), "{:5}".format(param3))


def traceCodeExecution(instructions):
    printHeaders()
    for inst in instructions:
        if inst[1] == 'nop':
            inst[1] = 'data'
        printInstruction(inst[0], inst[1], inst[2], inst[3], inst[4])


def readBinaryFile(fileName):
    with open(fileName, "rb") as f:
        byteCode = f.readlines()
        return byteCode


def getWords(byteCode):
    pc = 0
    hexCodes = []
    words = []
    for line in byteCode:
        hexCodes.extend(line.split())
    while pc < len(hexCodes):
        words.append(hextobin(hexCodes[pc]) + hextobin(hexCodes[pc + 1]) + hextobin(hexCodes[pc + 2]))
        pc = pc + 3
    return words


if __name__ == '__main__':
    byteCode = readBinaryFile('binary.txt')
    words = getWords(byteCode)
    lc = 0
    instructions = []
    for word in words:
        binOpcode = word[0:4]
        opcode = hex(int(binOpcode, 2))
        if opcode == '0x0':
            rA = word[4:9]
            rB = word[9:14]
            rC = word[14:19]
            binSubOpcode = word[19:24]
            opcodeTxt = returnOpcode(opcode)
            subOpcode = hex(int(binSubOpcode, 2))
            subOpcodeTxt = returnSubOpcode(subOpcode)
            hex_rA = ''
            hex_rB = ''
            hex_rC = ''
            if subOpcodeTxt not in ['nop', 'rts', 'halt']:
                hex_rA = hex(int(rA, 2))
                hex_rB = hex(int(rB, 2))
                hex_rC = hex(int(rC, 2))
            instructions.append([lc, subOpcodeTxt, getRegName(hex_rA), getRegName(hex_rB), getRegName(hex_rC)])
        else:
            reg = word[4:9]
            address = word[9:24]
            opcodeTxt = returnOpcode(opcode)
            hexAddress = hex(int(address, 2))
            hex_reg = hex(int(reg, 2))
            instructions.append([lc, opcodeTxt, getRegName(hex_reg), hexAddress, ''])
        lc = lc + 1

    traceCodeExecution(instructions)
