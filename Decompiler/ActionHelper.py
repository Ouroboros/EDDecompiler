from BattleActionScript import *
#import random
import uuid

def GenerateUniqueLable():
    return uuid.uuid4().hex
    #return '%X' % int(random.random() * 100000000000)

def JumpToLabelIfHasTarget(label_name):
    Jc(0x16, 0x1, 0x0, label_name)

def Random_Execute(Probability, LabelName):
    Jc(0x14, 0x4, Probability, LabelName)

def ChrSetSize(chr, x, z, y):
    AS_8D(0x7, chr, x, z, y)

def ForeachTargetEx(func, reset = True):
    if reset:
        ResetTarget()

    foreach_begin   = GenerateUniqueLable()
    foreach_end     = GenerateUniqueLable()

    label(foreach_begin)

    ForeachTarget(foreach_end)

    func()

    NextTarget()
    Jump(foreach_begin)

    label(foreach_end)
