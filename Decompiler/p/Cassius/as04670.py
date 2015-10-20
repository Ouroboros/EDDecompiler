from ActionHelper import *
from Voice import *
import SysCraft

def main():
    CreateBattleAction("as04670.dat", ((128, 176), (128, 176), (128, 176), (128, 176), (128, 176), (128, 176), (128, 176), (128, 176)))

    AddPreloadChip((
        "chr/ch04670.itc",         # 00 0
        "chr/ch04671.itc",         # 01 1
        "chr/ch04673.itc",         # 02 2
        "chr/ch04675.itc",         # 03 3
        "chr/ch20290.itc",         # 04 4
        "chr/ch20715.itc",         # 05 5
    ))

    CraftAction((
        "SysCraft_Init",                    # 00 0
        "SysCraft_Stand",                   # 01 1
        "SysCraft_Move",                    # 02 2
        "SysCraft_UnderAttack",             # 03 3
        "SysCraft_Dead",                    # 04 4
        "SysCraft_NormalAttack",            # 05 5
        "SysCraft_ArtsAria",                # 06 6
        "SysCraft_ArtsCast",                # 07 7
        "SysCraft_Win",                     # 08 8
        "SysCraft_EnterBattle",             # 09 9
        "SysCraft_UseItem",                 # 0A 10
        "SysCraft_Stun",                    # 0B 11
        "SysCraft_Unknown2",                # 0C 12
        'stub_craft',                       # 0D 13
        'stub_craft',                       # 0E 14
        "SysCraft_Counter",                 # 0F 15
        "Craft_百烈击",                      # 10 16
        "Craft_钢盔回旋踢",                  # 11 17
        EMPTY_ACTION,                       # 12 18
        EMPTY_ACTION,                       # 13 19
        EMPTY_ACTION,                       # 14 20
        EMPTY_ACTION,                       # 15 21
        EMPTY_ACTION,                       # 16 22
        EMPTY_ACTION,                       # 17 23
        EMPTY_ACTION,                       # 18 24
        EMPTY_ACTION,                       # 19 25
        EMPTY_ACTION,                       # 1A 26
        EMPTY_ACTION,                       # 1B 27
        EMPTY_ACTION,                       # 1C 28
        EMPTY_ACTION,                       # 1D 29

        'SysCraft_TeamRushInit',            # 1E 30
        'SysCraft_TeamRushAction',          # 1F 31
        EMPTY_ACTION,                       # 20 32
        EMPTY_ACTION,                       # 21 33
        EMPTY_ACTION,                       # 22 34
        EMPTY_ACTION,                       # 23 35
        EMPTY_ACTION,                       # 24 36
        EMPTY_ACTION,                       # 25 37
        EMPTY_ACTION,                       # 26 38

        EMPTY_ACTION,                       # 27 39
        EMPTY_ACTION,                       # 28 40
        EMPTY_ACTION,                       # 29 41
        EMPTY_ACTION,                       # 2A 42
        EMPTY_ACTION,                       # 2B 43
        EMPTY_ACTION,                       # 2C 44
        EMPTY_ACTION,                       # 2D 45
    ))

    label('Craft_麒麟功')

    AS_8D(0x4B, 0xFF, 0x10000, 0xFFFFFFFF, 0x0)
    AS_8D(0x4B, 0xFF, 0x800000, 0xFFFFFFFF, 0x0)
    DamageCue(0xFE)
    AS_A1(0xFF, 0x10000, 0x83, "")
    Return()

    label('Craft_百烈击')
    import 百烈击
    百烈击.main()
    Return()

    label('Craft_钢盔回旋踢')
    import 钢盔回旋踢
    钢盔回旋踢.main()
    Return()

    label('stub_craft')
    Return()

    label("SysCraft_ArtsAria")
    SysCraft.artsAria()
    Return()


    label("SysCraft_ArtsCast")

    SysCraft.artsCast()
    Return()


    label("SysCraft_Win")

    SysCraft.battleWin()
    Return()


    label("SysCraft_EnterBattle")

    SysCraft.enterBattle()
    Return()


    label("SysCraft_UseItem")

    SysCraft.useItem()
    Return()

    label("SysCraft_Init")
    SysCraft.init()
    Return()

    # SysCraft_Init end

    label('clear_all_debuff')

    not_clear = \
    [
        CraftConditionFlags.MaxGuard,
        CraftConditionFlags.HPRecovery,
        CraftConditionFlags.CPRecovery,
        CraftConditionFlags.Stealth,
        CraftConditionFlags.Dead,
        CraftConditionFlags.Vanish,
    ]

    flag = 1
    for i in range(32):
        if not flag in not_clear:
            AS_8D(0x4B, CraftTarget.Self, flag, -1, 0)
        flag <<= 1

    AS_8D(0x4B, CraftTarget.Self, CraftConditionFlags.Vanish, 0, 0)

    CallReturn()


    # label("SysCraft_Stand")
    SysCraft.stand()
    # SysCraft_Stand end


    # label("SysCraft_Move")
    SysCraft.move()
    # SysCraft_Move end


    label("SysCraft_UnderAttack")

    SysCraft.underAttack()
    Return()

    # SysCraft_UnderAttack end


    label("SysCraft_Dead")

    SysCraft.dead()
    Return()

    # SysCraft_Dead end


    label("SysCraft_NormalAttack")
    SysCraft.normalAttack()
    Return()

    # SysCraft_NormalAttack end

    label("SysCraft_Stun")
    SysCraft.stun()
    Return()

    # SysCraft_Stun end


    label("SysCraft_Unknown2")

    SetChrChip(0xFF, 0x0)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    Return()

    # SysCraft_Unknown2 end


    label("SysCraft_Counter")
    SysCraft.counter()
    Return()

    # SysCraft_Counter end


    label('SysCraft_TeamRushInit')
    Return()

    label('SysCraft_TeamRushAction')
    Return()

    SaveToFile()

TryInvoke(main)
