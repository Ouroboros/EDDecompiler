from ActionHelper import *
from Voice import *

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
        EMPTY_ACTION,                       # 11 17
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

    import SysCraft

    label('SysCraft_TeamRushInit')
    Return()

    label('SysCraft_TeamRushAction')
    Return()

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

    label('stub_craft')
    Return()


    label("SysCraft_ArtsAria")

    Call('clear_all_debuff')
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

    label("loc_65A")

    SetChrSubChip(0xFF, 0x4)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(50)
    Yield()
    Jump("loc_65A")

    label("loc_672")

    ResetTarget()

    #label("loc_673")

    #ForeachTarget("loc_6B2")
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 500, 0, 0, 0, 0, 500, 500, 500, 0x3)
    AS_A7(0xFF, 0x3, 0xFE, 0xFF38, 0x1F4, 0xFF38, 0xC8, 0x3E8, 0xC8, 0x0)
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(100)
    Yield()
    #NextTarget()
    #Jump("loc_673")

    label("loc_6B2")

    Sleep(100)
    Yield()
    Jump("loc_672")

    # SysCraft_NormalAttack end


    label("SysCraft_Stun")
    SetChrChip(0xFF, 5)
    SetChrSubChip(0xFF, 0)
    Sleep(100)
    Yield()
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
    # Jump('Craft_百烈击')
    # Return()

    attach_chip = 8
    critical_hit_eff = 1
    pre_critical_hit_eff = 2

    eff_list = [critical_hit_eff, pre_critical_hit_eff]

    AS_78(1)
    LoadChrChip(attach_chip, "chr/ch04672.itc", 0xFF)
    LoadEffect(critical_hit_eff, "battle/cr006402.eff")
    LoadEffect(pre_critical_hit_eff, "battle/cr006401.eff")
    AS_78(0)

    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(100, 20, 30)
    # BeginChrThread(0xFF, 1, "SysCraft_Move", 0x0)
    # AS_1E(0xFFFFFFFF)
    # EndChrThread(0xFF, 1)
    TurnDirection(0xFF, 0xFE, 0, 0, 0x0)
    AS_6D(0x200000)
    AS_89(0xFF)
    Yield()

    SetChrChip(CraftTarget.Self, attach_chip)
    SetChrSubChip(CraftTarget.Self, 0x0)
    Yield()

    PlayEffect(0xFF, 0xFF, pre_critical_hit_eff, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    Sleep(200)
    Yield()

    SoundEx(183, 0)
    BeginChrThread(CraftTarget.Self, 1, "shake_self", 0x0)
    Sleep(0xA)
    Yield()
    Sleep(0x1F4)
    Yield()
    Voice(0, 卡西乌斯_百烈击2, 卡西乌斯_攻击5, 卡西乌斯_攻击7, 0, 0xFE)

    for i in range(1, 7):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(0x32)
        Yield()

    Knockback(8)
    DamageAnime(CraftTarget.TargetChr, 1, 0x32)
    DamageCue(0xFE)
    SetCondition(CraftTarget.TargetChr, CraftConditionFlags.Stun, 50, 1)
    SoundEx(卡西乌斯_音效_百烈击_结尾, 0)
    PlayEffect(0xFF, 0xFF, critical_hit_eff, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 3)

    SetChrSubChip(CraftTarget.Self, 0x7)
    Sleep(0x32)
    Yield()

    SetChrSubChip(CraftTarget.Self, 0x8)
    Sleep(0x5DC)
    Yield()

    for i in range(9, 12):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(0x32)
        Yield()

    AS_14(0x2)

    for eff in eff_list:
        FreeEffect(eff)

    Return()

    # SysCraft_Counter end

    SaveToFile()

TryInvoke(main)
