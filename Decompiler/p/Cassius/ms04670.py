from BattleMonsterStatus import *

def main():
    Name               = "钢盔肾斗士"
    Description        = "结社八十八个『肾斗士』\\n的第一位，擅长使棍子的\\n剑圣。"
    ASFile             = "as04670.dat"
    Symbol             = "sy04670.itp"

    Resistance = CraftConditionFlags.Poison         | \
                 CraftConditionFlags.Frozen         | \
                 CraftConditionFlags.Landification  | \
                 CraftConditionFlags.Sleeping       | \
                 CraftConditionFlags.BanArts        | \
                 CraftConditionFlags.Darkness       | \
                 CraftConditionFlags.BanCraft       | \
                 CraftConditionFlags.Confusion      | \
                 CraftConditionFlags.Stun           | \
                 CraftConditionFlags.OnehitKill     | \
                 CraftConditionFlags.Burning        | \
                 CraftConditionFlags.Rage           | \
                 CraftConditionFlags.Vanish         | \
                 CraftConditionFlags.Reserve_2      | \
                 CraftConditionFlags.GreenPepper    | \
                 CraftConditionFlags.Dead           | \
                 CraftConditionFlags.Str            | \
                 CraftConditionFlags.Def            | \
                 CraftConditionFlags.Ats            | \
                 CraftConditionFlags.Adf            | \
                 CraftConditionFlags.Dex            | \
                 CraftConditionFlags.Agl            | \
                 CraftConditionFlags.Mov            | \
                 CraftConditionFlags.Spd

    Level              = 120
    MaximumHP          = 59000
    InitialHP          = 9000
    MaximumEP          = 9000
    InitialEP          = 9000
    MaximumCP          = 200
    InitialCP          = 0

    SPD                = 12
    MoveSPD            = 10
    MOV                = 6
    STR                = 3450
    DEF                = 3114
    ATS                = 2219
    ADF                = 2391
    DEX                = 150
    AGL                = 32
    RNG                = 1

    Unknown_2A         = 0x0
    EXP                = 1024
    Unknown_2E         = 0x0
    Unknown_30         = 0x0
    AIType             = 0x0
    Unknown_33         = 0x3E8
    Unknown_35         = 0x9
    Unknown_36         = 0xA280
    EnemyFlags         = 0x0000
    BattleFlags        = 0x0804

    Unknown_3C         = 0x1
    Unknown_3E         = 0x0
    Sex                = 9
    Unknown_41         = 0x1
    CharSize           = 0x190
    DefaultEffectX     = 0x0
    DefaultEffectZ     = 0
    DefaultEffectY     = 0x0
    Unknown_52         = 0x60
    Unknown_53         = 0x50
    Unknown_54         = 0xA0
    Unknown_55         = 0xB0
    #Resistance         = 0xF0008FFF
    AttributeRate      = [ 100, 100, 100, 100, 100, 100, 100 ]
    Sepith             = [ 255, 255, 255, 255, 255, 255, 255 ]
    DropItem           = [ 0x01FF, 0x0000 ]
    DropRate           = [ 100, 0 ]
    Equipment          = [ 0x0009, 0x0000, 0x0000, 0x0000, 0x0000 ]
    Orbment            = [ 0x0000, 0x0000, 0x0000, 0x0000 ]

    RunawayType        = 0
    RunawayRate        = 0
    RunawayParam1      = 0
    Reserve1           = 0

    Craft_03E8 = CreateCraft(
                    "",
                    "",
                    0x05, 0x12, 0x15,
                    CraftAttribute.NoAttribute,
                    CraftRange.Target,
                    CraftState.Physical, CraftState.QueryMonsterInfo,
                    0, 0,
                    0, 30,
                    0,
                    0,
                    60, 0,
                    0, 0,
               )

    百烈击 = CreateCraft(
                    "百烈击",
                    "百龙霸",
                    0x05, 0x12, 0,
                    CraftAttribute.NoAttribute,
                    CraftRange.Target,
                    CraftState.Physical, CraftState.NoneState,
                    3, 1,
                    0, 10,
                    0,
                    2,
                    120, 0,
                    0, 0,
               )

    钢盔回旋踢 = CreateCraft(
                    "钢盔回旋踢",
                    "",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.CircleOnSelf,
                    CraftState.Physical, CraftState.NoneState,
                    1, 1,
                    0, 0,
                    0,
                    10,
                    0, 0,
                    0, 0,
               )

    疾风轰雷闪 = CreateCraft(
                    "疾风轰雷闪",
                    "突贯攻击",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.LineOnLocationIncludeSelf,
                    CraftState.Physical, CraftState.InterruptAria,
                    1, 50,
                    0, 30,
                    0,
                    3,
                    60, 0,
                    0, 0,
               )

    大地轰雷锤 = CreateCraft(
                    "大地轰雷锤",
                    "以自身为避雷针，落下轰击整个战场的巨雷。",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.Arts, CraftState.BanCraft,
                    1, 50,
                    0, 30,
                    0,
                    100,
                    100, 0,
                    100, 3,
               )

    横扫千军 = CreateCraft(
                    "横扫千军",
                    "用横扫攻击将前方的敌人击退。",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.CircleOnSelf,
                    CraftState.Physical, CraftState.Stun,
                    1, 4,
                    0, 30,
                    0,
                    6,
                    100, 0,
                    100, 5,
               )

    圣技大十字 = CreateCraft(
                    "圣技·大十字",
                    "",
                    0x06, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.Physical, CraftState.NoneState,
                    1, 50,
                    0, 30,
                    100,
                    100,
                    400, 0,
                    0, 0,
               )

    摘面具 = CreateCraft(
                    "摘面具",
                    "改",
                    0x05, 0x42, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.Target,
                    CraftState.Physical, CraftState.NoneState,
                    1, 1,
                    0, 0,
                    0,
                    1,
                    0, 0,
                    0, 0,
               )

    暴雨疾风枪 = CreateCraft(
                    "暴雨疾风枪",
                    "以人类之身无法察觉的速度发出无数的枪把对手刺穿，一切防御\\n在这面前都显得苍白无力。此神技后来流传到某组织的No.3手上。",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.CircleOnLocationExclude,
                    CraftState.Physical, CraftState.QueryMonsterInfo,
                    50, 10,
                    0, 40,
                    0,
                    4,
                    50, 0,
                    0, 0,
               )

    零时迷子 = CreateCraft(
                    "零时迷子",
                    "",
                    0x05, 0x82, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.NoneState, CraftState.NoneState,
                    1, 0,
                    0, 0,
                    0,
                    0,
                    0, 0,
                    0, 0,
               )

    幻银方舟炮 = CreateCraft(
                    "幻银方舟炮",
                    "攻击：全体\\n召唤巨大的银色方舟，全炮台开火，将大地上的一切歼灭。",
                    0x4A, 0x12, 0x21,
                    CraftAttribute.Gen,
                    CraftRange.CircleOnLocationExclude,
                    CraftState.Arts, CraftState.NoneState,
                    1, 100,
                    0, 0,
                    0,
                    4,
                    380, 0,
                    0, 0,
               )


    CraftList = CreateCraftList([
                    Craft_03E8,
                    百烈击,
                    钢盔回旋踢,
                ])

    Attack = CreateAI(0x1, 0,   0x0, 0x1, 0x00, 0x05, Craft_03E8,         [0,     0,      1,      0])

    Craft_百烈击         = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x10, 百烈击,         [30,    1,      0,      0])
    Craft_钢盔回旋踢     = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x11, 钢盔回旋踢,      [30,    1,      0,      0])
    # Craft_暴雨疾风枪     = CreateAI(0x2,  30,   0x7,  0x1,  0x00, 0x15, 暴雨疾风枪,      [0,     0,      0,      0])
    # Craft_摘面具         = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x13, 摘面具,         [70,    255,    0,      0])
    # Craft_疾风轰雷闪     = CreateAI(0x2,  30,   0x7,  0x1,  0x00, 0x10, 疾风轰雷闪,      [0,     0,      1,      0])
    # Craft_横扫千军       = CreateAI(0x2,  30,   0x7,  0x1,  0x00, 0x12, 横扫千军,        [0,     0,      1,      0])
    # Craft_天地乖离       = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x18, 天地乖离,        [30,    1,      0,      0])
    # Craft_大地轰雷锤     = CreateAI(0x2,  30,   0x7,  0x1,  0x00, 0x11, 大地轰雷锤,      [0,     0,      1,      0])
    # Craft_零时迷子       = CreateAI(0xB,  100,  0x12, 0x1,  0x00, 0x14, 零时迷子,        [0,     0,      0,      0])
    # Craft_神速           = CreateAI(0x2,  30,   0x7,  0x1,  0x00, 0x19, 神速,            [0,     0,      1,      0])

    #Craft_幻银方舟炮       = CreateAI(0xB,  100,  0x12, 0x1,  6, 7, 幻银方舟炮,        [0,     0,      0,      0])

    # SCraft_圣技大十字    = CreateAI(0xA, 100, 0x0, 0x1, 0x00, 0x1A, 圣技大十字,         [100,   0,      0,      0])


    ArtsAIList          = []
    CraftAIList         = [Craft_钢盔回旋踢, Craft_百烈击]
    SCraftAIList        = []
    SupportCraftAIList  = []

    SaveToMS("ms04670.dat", locals())

TryInvoke(main)