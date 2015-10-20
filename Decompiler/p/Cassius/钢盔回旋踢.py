from ActionHelper import *
from Voice import *

def main():
    attack_chip     = 7

    showup_eff      = 0
    turn_around_eff = 1
    kick_eff        = 2
    hit_eff        = 3

    eff_list = [
        showup_eff,
        turn_around_eff,
        kick_eff,
        hit_eff,
    ]

    with ResourceLock:
        LoadEffect(showup_eff,      "battle/cr007200.eff")
        LoadEffect(turn_around_eff, "battle/cr007100.eff")
        LoadEffect(kick_eff,        "battle/cr007400.eff")
        LoadEffect(hit_eff,         "battle/ms00000.eff")
        LoadChrChip(attack_chip,    "chr/ch04672.itc", 0xFF)

    # ResetLookingTargetData()
    # LookingTargetAdd(0xFF, "", 0x0)
    # LookingTarget(2000, 1000, 1200)
    TurnDirection(0xFF, 0xFE, 0, 0, 0x0)
    AS_89(0xFF)
    AS_83(0)

    PlayEffect(0xFF, 0xFF, turn_around_eff, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    SoundEx(卡西乌斯_音效_雷光击_旋转, 0)
    SoundEx(卡西乌斯_音效_雷光击_起跳, 0)
    SetChrChip(CraftTarget.Self, attack_chip)

    for i in range(4):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(30)
        Yield()

    HideChr(CraftTarget.Self, 300)

    for i in range(6):
        AS_04(CraftTarget.Self, 1, -45)
        Sleep(20)
        Yield()

    AS_60(CraftTarget.Self)

    Voice(0, 卡西乌斯_攻击7, 0, 0, 0, 0xFE)
    LockCamera(0xF8, 0, 0, 0, 2000)
    Sleep(1000)
    Yield()

    SoundEx(卡西乌斯_音效_雷光击_移动, 0)
    # eff 4

    Knockback(2)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTargetAdd(CraftTarget.Self, "", 0x0)
    LookingTarget(100, 20, 30)

    ResetTarget()

    label("回旋踢_next_target")

    ForeachTarget("回旋踢_next_target_end")

    PlayEffect(0xFF, 0xF9, kick_eff, 0x400, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    ChrMove(CraftTarget.Self, CraftTarget.TargetChr, 0, 0, 0, 50, 0)
    PlayEffect(0xFF, 0xF8, hit_eff, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    AS_8D(0x1F, CraftTarget.Self, 0xF0, 0x0, 0x0)
    DamageAnime(CraftTarget.TargetChr, 0, 50)
    DamageCue(CraftTarget.TargetChr)
    LockCamera(0xF8, 0, 0, 0, 100)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("回旋踢_next_target")

    label("回旋踢_next_target_end")

    # CancelEffect(CraftTarget.Self, 4)
    Sleep(500)
    Yield()

    ResetTarget()

    AS_5F(CraftTarget.Self, 0x0)
    HideChr(CraftTarget.Self, 0)
    ShowChr(CraftTarget.Self, 500)
    SetChrChip(CraftTarget.Self, attack_chip)
    SetChrSubChip(CraftTarget.Self, 6)
    Sleep(0)
    Yield()

    SetChrChip(CraftTarget.Self, 3)
    SetChrSubChip(CraftTarget.Self, 0)
    AS_0A(CraftTarget.Self, 1, 0, 0)
    ChrSetPos(CraftTarget.Self, 0xF0, 0, 0, 0)
    Yield()

    PlayEffect(0xFF, 0xFF, showup_eff, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    SoundEx(卡西乌斯_音效_雷光击_现身, 0)

    TurnDirection(CraftTarget.Self, CraftTarget.TargetChr, 0, 0, 0x0)
    ShowChr(CraftTarget.Self, 100)
    Sleep(800)
    Yield()

    for eff in eff_list:
        FreeEffect(eff)
