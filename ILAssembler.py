from struct import * # Needed for arguments for argument based instructions

LookupInstructions = { # No argument instructions
	'add': [0x58],
	'add.ovf': [0xd6],
	'add.ovf.un': [0xd7],
	'and': [0x5f],
	'arglist': [0xfe, 0x00],
	'break': [0x01],
	'ceq': [0xfe, 0x01],
	'cgt': [0xfe, 0x02],
	'cgt.un': [0xfe, 0x03],
	'ckfinite': [0xc3],
	'clt': [0xfe, 0x04],
	'clt.un': [0xfe, 0x05],
	'conv.i': [0xD3],
	'conv.i1': [0x67],
	'conv.i2': [0x68],
	'conv.i4': [0x69],
	'conv.i8': [0x6A],
	'conv.ovf.i': [0xD4],
	'conv.ovf.i.un': [0x8A],
	'conv.ovf.i1': [0xB3],
	'conv.ovf.i1.un': [0x82],
	'conv.ovf.i2': [0xB5],
	'conv.ovf.i2.un': [0x83],
	'conv.ovf.i4': [0xB7],
	'conv.ovf.i4.un': [0x84],
	'conv.ovf.i8': [0xB9],
	'conv.ovf.i8.un': [0x85],
	'conv.ovf.u': [0xD5],
	'conv.ovf.u.un': [0x8B],
	'conv.ovf.u1': [0xB4],
	'conv.ovf.u1.un': [0x86],
	'conv.ovf.u2': [0xB6],
	'conv.ovf.u2.un': [0x87],
	'conv.ovf.u4': [0xB8],
	'conv.ovf.u4.un': [0x88],
	'conv.ovf.u8': [0xBA],
	'conv.ovf.u8.un': [0x89],
	'conv.r.un': [0x76],
	'conv.r4': [0x6B],
	'conv.r8': [0x6C],
	'conv.u': [0xE0],
	'conv.u1': [0xD2],
	'conv.u2': [0xD1],
	'conv.u4': [0x6D],
	'conv.u8': [0x6E],
	'cpblk': [0xFE, 0x17],
	'div': [0x5B],
	'div.un': [0x5C],
	'dup': [0x25],
	'endfault': [0xDC],
	'endfilter': [0xFE, 0x11],
	'endfinally': [0xDC],
	'initblk': [0xFE, 0x18],
	'ldarg.0': [0x02],
	'ldarg.1': [0x03],
	'ldarg.2': [0x04],
	'ldarg.3': [0x05],
	'ldc.i4.0': [0x16],
	'ldc.i4.1': [0x17],
	'ldc.i4.2': [0x18],
	'ldc.i4.3': [0x19],
	'ldc.i4.4': [0x1A],
	'ldc.i4.5': [0x1B],
	'ldc.i4.6': [0x1C],
	'ldc.i4.7': [0x1D],
	'ldc.i4.8': [0x1E],
	'ldc.i4.m1': [0x15],
	'ldc.i4.M1': [0x15],
	'ldelem.i': [0x97],
	'ldelem.i1': [0x90],
	'ldelem.i2': [0x92],
	'ldelem.i4': [0x94],
	'ldelem.i8': [0x96],
	'ldelem.r4': [0x98],
	'ldelem.r8': [0x99],
	'ldelem.ref': [0x9A],
	'ldelem.u1': [0x91],
	'ldelem.u2': [0x93],
	'ldelem.u4': [0x95],
	'ldelem.u8': [0x96],
	'ldind.i': [0x4D],
	'ldind.i1': [0x46],
	'ldind.i2': [0x48],
	'ldind.i4': [0x4A],
	'ldind.i8': [0x4C],
	'ldind.r4': [0x4E],
	'ldind.r8': [0x4F],
	'ldind.ref': [0x50],
	'ldind.u1': [0x47],
	'ldind.u2': [0x49],
	'ldind.u4': [0x4B],
	'ldind.u8': [0x4C],
	'ldlen': [0x8E],
	'ldloc.0': [0x06],
	'ldloc.1': [0x07],
	'ldloc.2': [0x08],
	'ldloc.3': [0x09],
	'ldnull': [0x14],
	'localloc': [0xFE, 0x0F],
	'mul': [0x5A],
	'mul.ovf': [0xD8],
	'mul.ovf.un': [0xD9],
	'neg': [0x65],
	'nop': [0x00],
	'not': [0x66],
	'or': [0x60],
	'pop': [0x26],
	'readonly.': [0xFE, 0x1E],
	'refanytype': [0xFE, 0x1D],
	'rem': [0x5D],
	'rem.un': [0x5E],
	'ret': [0x2A],
	'rethrow': [0xFE, 0x1A],
	'shl': [0x62],
	'shr': [0x63],
	'shr.un': [0x64],
	'stelem.i': [0x9B],
	'stelem.i1': [0x9C],
	'stelem.i2': [0x9D],
	'stelem.i4': [0x9E],
	'stelem.i8': [0x9F],
	'stelem.r4': [0xA0],
	'stelem.r8': [0xA1],
	'stelem.ref': [0xA2],
	'stind.i': [0xDF],
	'stind.i1': [0x52],
	'stind.i2': [0x53],
	'stind.i4': [0x54],
	'stind.i8': [0x55],
	'stind.r4': [0x56],
	'stind.r8': [0x57],
	'stind.ref': [0x51],
	'stloc.0': [0x0A],
	'stloc.1': [0x0B],
	'stloc.2': [0x0C],
	'stloc.3': [0x0D],
	'sub': [0x59],
	'sub.ovf': [0xDA],
	'sub.ovf.un': [0xDB],
	'tail.': [0xFE, 0x14],
	'throw': [0x7A],
	'unaligned. (alignment)': [0xFE, 0x12],
	'volatile.': [0xFE, 0x13],
	'xor': [0x61],
}

ArgInstruction = { # Instructions with arguments
	'beq': [ [0x3B], ['i'] ],
	'beq.s': [ [0x2E], ['b'] ],
	'bge': [ [0x3C], ['i'] ],
	'bge.s': [ [0x2F], ['b'] ],
	'bge.un': [ [0x41], ['i'] ],
	'bge.un.s': [ [0x34], ['b'] ],
	'bgt': [ [0x3D], ['i'] ],
	'bgt.s': [ [0x30], ['b'] ],
	'bgt.un': [ [0x42], ['i'] ],
	'bgt.un.s': [ [0x35], ['b'] ],
	'ble': [ [0x3E], ['i'] ],
	'ble.s': [ [0x31], ['b'] ],
	'ble.un': [ [0x43], ['i'] ],
	'ble.un.s': [ [0x36], ['b'] ],
	'blt': [ [0x3F], ['i'] ],
	'blt.s': [ [0x32], ['b'] ],
	'blt.un': [ [0x44], ['i'] ],
	'blt.un.s': [ [0x37], ['b'] ],
	'bne.un': [ [0x40], ['i'] ],
	'bne.un.s': [ [0x33], ['b'] ],
	'box': [ [0x8C], ['I'] ],
	'br': [ [0x38], ['i'] ],
	'br.s': [ [0x2B], ['b'] ],
	'brfalse': [ [0x39], ['i'] ],
	'brfalse.s': [ [0x2C], ['b'] ],
	'brinst': [ [0x3A], ['i'] ],
	'brinst.s': [ [0x2D], ['b'] ],
	'brnull': [ [0x39], ['i'] ],
	'brnull.s': [ [0x2C], ['b'] ],
	'brtrue': [ [0x3A], ['i'] ],
	'brtrue.s': [ [0x2D], ['b'] ],
	'brzero': [ [0x39], ['i'] ],
	'brzero.s': [ [0x2C], ['b'] ],
	'call': [ [0x28], ['I'] ],
	'calli': [ [0x29], ['I'] ],
	'callvirt': [ [0x6F], ['I'] ],
	'castclass': [ [0x74], ['I'] ],
	'constrained.': [ [0xFE, 0x16], ['I'] ],
	'cpobj': [ [0x70], ['I'] ],
	'initobj': [ [0xFE, 0x15], ['I'] ],
	'isinst': [ [0x75], ['I'] ],
	'jmp': [ [0x27], ['I'] ],
	'ldarg': [ [0xFE, 0x09], ['H'] ],
	'ldarg.s': [ [0x0E], ['B'] ],
	'ldarga': [ [0xFE, 0x0A], ['H'] ],
	'ldarga.s': [ [0x0F], ['B'] ],
	'ldc.i4': [ [0x20], ['i'] ],
	'ldc.i4.s': [ [0x1F], ['b'] ],
	'ldc.i8': [ [0x21], ['q'] ],
	'ldc.r4': [ [0x22], ['f'] ],
	'ldc.r8': [ [0x23], ['d'] ],
	'ldelem': [ [0xA3], ['I'] ],
	'ldelema': [ [0x8F], ['I'] ],
	'ldfld': [ [0x7B], ['I'] ],
	'ldflda': [ [0x7C], ['I'] ],
	'ldftn': [ [0xFE, 0x06], ['I'] ],
	'ldloc': [ [0xFE, 0x0C], ['H'] ],
	'ldloc.s': [ [0x11], ['B'] ],
	'ldloca': [ [0xFE, 0x0D], ['H'] ],
	'ldloca.s': [ [0x12], ['B'] ],
	'ldobj': [ [0x71], ['I'] ],
	'ldsfld': [ [0x7E], ['I'] ],
	'ldsflda': [ [0x7F], ['I'] ],
	'ldstr': [ [0x72], ['I'] ],
	'ldtoken': [ [0xD0], ['I'] ],
	'ldvirtftn': [ [0xFE, 0x07], ['I'] ],
	'leave': [ [0xDD], ['i'] ],
	'leave.s': [ [0xDE], ['b'] ],
	'mkrefany': [ [0xC6], ['I'] ],
	'newarr': [ [0x8D], ['I'] ],
	'newobj': [ [0x73], ['I'] ],
	'refanyval': [ [0xC2], ['I'] ],
	'sizeof': [ [0xFE, 0x1C], ['I'] ],
	'starg': [ [0xFE, 0x0B], ['H'] ],
	'starg.s': [ [0x10], ['B'] ],
	'stelem': [ [0xA4], ['I'] ],
	'stfld': [ [0x7D], ['I'] ],
	'stloc': [ [0xFE, 0x0E], ['H'] ],
	'stloc.s': [ [0x13], ['B'] ],
	'stobj': [ [0x81], ['I'] ],
	'stsfld': [ [0x80], ['I'] ],
	'switch': [ [0x45], ['I'] ], # Special case, args ignored
	'unbox': [ [0x79], ['I'] ],
	'unbox.any': [ [0xA5], ['I'] ],
}

def NumToArr(n, t): # Converts both hex and dec
	rN = 0
	if n[0:2] == '0x': # In hex
		rN = int(n, 16)
	else:
		rN = int(n)
	return bytearray(pack(t, rN)) # Return everything as ints instead of chars


def GetAssembleInstruction(instruction):
	instruction = instruction.lower() # Easier lookup
	if instruction in LookupInstructions: # Doesn't have arguments
		return LookupInstructions[instruction] # No parsing required
	else:
		ins = instruction.split(' ') # Split arguments based on spaces
		if len(ins) < 2:
			print 'UNKNOWN INSTRUCTION %s'%instruction
			return None
		else:
			if ins[0] in ArgInstruction:
				base = ArgInstruction[ins[0]][0][:]
				if len(ins) - 1 != len(ArgInstruction[ins[0]][1]) and ins[0] != 'switch': # Switch can have nth amount of args?
					print 'INVALID ARG LENGTH!'
					return None
				i = 1
				if ins[0] == 'switch': # Looks to have nth amount of args? could be wrong
					for a in ins:
						if a == 'switch': continue # First arg
						base += NumToArr( a.replace(',', '').strip(), 'I' )
					return base

				for arg in ArgInstruction[ins[0]][1]: # Every other arg based object seems to only have 1 arg but loop just in case
					base += NumToArr( ins[i], arg )
					i += 1
				return base
			else:
				print 'UNKNOWN INSTRUCTION %s'%ins[0]
				return None

def Assemble(IL, nicePrint=False):
	lines = IL.split('\n') # parse 1 line at a time
	out = ''
	for line in lines:
		line = line.strip() # Clean output
		if line == '':
			continue
		asm = GetAssembleInstruction(line) # Get byte code array
		for hx in asm:
			out += '%02X '%hx # Format nicely
		if nicePrint: # If it's nice print, print with comments and each instruction on a new line
			print out + '  ;   %s'%line
			out = ''
	if not nicePrint: # If we're not nice printing, print all on 1 line without comments
		print out

def main():
	strAssem = ''
	nicePrintToggle = False
	while True:
		curLine = raw_input('> ')
		if curLine == 'nice_print': # Toggle nice printing
			nicePrintToggle = not nicePrintToggle
			print 'Nice print is now %s'%nicePrintToggle
			continue
		if curLine.strip() != '': # Attempt single instruction assemble
			if GetAssembleInstruction(curLine) != None: # Valid instruction
				strAssem += curLine + '\n'
		if curLine == '': # No input, assemble
			Assemble(strAssem, nicePrintToggle)
			strAssem = '' # Reset input data

if __name__ == '__main__':
	main()
