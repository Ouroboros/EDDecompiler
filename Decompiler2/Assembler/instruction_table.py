from Common import *
from enum import IntEnum
from . import instruction

__all__ = (
    'OperandDescriptor',
    'InstructionDescriptor',
    'InstructionTable',
)

class OperandDescriptor(IntEnum):
    Empty,      \
    SInt8,      \
    SInt16,     \
    SInt32,     \
    SInt64,     \
    UInt8,      \
    UInt16,     \
    UInt32,     \
    UInt64,     \
    SHex8,      \
    SHex16,     \
    SHex32,     \
    SHex64,     \
    UHex8,      \
    UHex16,     \
    UHex32,     \
    UHex64,     \
    Float32,    \
    Float64,    \
    MBCS,       \
    Bytes,      \
    UserDefined = range(22)

    def __init__(self, *args):
        super(IntEnum, self).__init__()

        self.lower      = False     # type: bool
        self.encoding   = 'mbcs'    # type: str

    @property
    def size(self):
        return {
            self.SInt8      : 1,
            self.SInt16     : 2,
            self.SInt32     : 4,
            self.SInt64     : 8,

            self.UInt8      : 1,
            self.UInt16     : 2,
            self.UInt32     : 4,
            self.UInt64     : 8,

            self.SHex8      : 1,
            self.SHex16     : 2,
            self.SHex32     : 4,
            self.SHex64     : 8,

            self.UHex8      : 1,
            self.UHex16     : 2,
            self.UHex32     : 4,
            self.UHex64     : 8,

            self.Float32    : 4,
            self.Float64    : 8,

            self.MBCS       : None,
            self.Bytes      : None,
        }[self]

class InstructionDescriptor:
    def __init__(self, opcode: int, mnemonic: str, operands: List[OperandDescriptor], flags: 'instruction.Flags' = 0, handler: Callable = None):
        self.opcode     = opcode                    # type: int
        self.mnemonic   = mnemonic                  # type: str
        self.operands   = operands                  # type: List[OperandDescriptor]
        self.flags      = flags                     # type: instruction.Flags
        self.handler    = handler                   # type: Callable

    def __str__(self):
        return '%s @ 0x%02X %s' % (self.mnemonic, self.opcode, self.operands)

class InstructionTable:
    def __init__(self, decriptors: List[InstructionDescriptor]):
        self.decriptors = decriptors                # type: List[InstructionDescriptor]

    def readInstruction(self, fs: fileio.FileStream) -> 'instruction.Instruction':
        raise NotImplementedError

    def readOpCode(self, fs: fileio.FileStream) -> int:
        raise NotImplementedError

    def writeInstruction(self, fs: fileio.FileStream, inst: 'instruction.Instruction'):
        raise NotImplementedError

    def writeOpCode(self, fs: fileio.FileStream, inst: 'instruction.Instruction'):
        raise NotImplementedError
