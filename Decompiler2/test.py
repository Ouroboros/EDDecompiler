from ml import *
import Assembler

def main():
    OperandDescriptor = Assembler.OperandDescriptor

    desc = Assembler.InstructionDescriptor(0x05, 'Call', (OperandDescriptor.UInt8, OperandDescriptor.UInt8))
    desc.operands[0]

    print(desc)

    opr = Assembler.Operand()

    print(opr.descriptor.encoding)

    f = Assembler.Flags.StartBlock | Assembler.Flags.EndBlock
    print(f)

    inst = Assembler.Instruction()
    blk = Assembler.CodeBlock(None)
    tbl = Assembler.InstructionTable(None)

    blk.instructions[0]
    inst.branches[0]
    tbl.decriptors[0]

    print(f.isStartBlock)
    print(f.isEndBlock)

    console.pause('done')

if __name__ == '__main__':
    Try(main)
