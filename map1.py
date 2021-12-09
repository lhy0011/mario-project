#1스테이지 맵 제작

import map


class Map1:
    ground = []
    for i in range(170):
        ground.append(34 * i)

    block = []
    for i in range(340,510,68):
        block.append(i)
    # 69 ~ 75
    block.append(34 * 70)
    block.append(34 * 71)
    block.append(34 * 73)
    block.append(34 * 74)

    block2_1 = []
    block2_1.append(34 * 90)
    block2_1.append(34 * 91)
    block2_1.append(34 * 91)
    block2_1.append(34 * 92)
    block2_1.append(34 * 92)
    block2_1.append(34 * 92)
    block2_1.append(34 * 93)
    block2_1.append(34 * 93)
    block2_1.append(34 * 93)
    block2_1.append(34 * 93)

    block2_1.append(34 * 96)
    block2_1.append(34 * 96)
    block2_1.append(34 * 96)
    block2_1.append(34 * 96)
    block2_1.append(34 * 97)
    block2_1.append(34 * 97)
    block2_1.append(34 * 97)
    block2_1.append(34 * 98)
    block2_1.append(34 * 98)
    block2_1.append(34 * 99)

    block2_1.append(34 * 140)
    block2_1.append(34 * 141)
    block2_1.append(34 * 141)
    block2_1.append(34 * 142)
    block2_1.append(34 * 142)
    block2_1.append(34 * 142)
    block2_1.append(34 * 143)
    block2_1.append(34 * 143)
    block2_1.append(34 * 143)
    block2_1.append(34 * 143)
    block2_1.append(34 * 144)
    block2_1.append(34 * 144)
    block2_1.append(34 * 144)
    block2_1.append(34 * 144)
    block2_1.append(34 * 144)
    block2_1.append(34 * 145)
    block2_1.append(34 * 145)
    block2_1.append(34 * 145)
    block2_1.append(34 * 145)
    block2_1.append(34 * 145)
    block2_1.append(34 * 145)
    block2_2 = [85, 85, 85 + 34, 85, 85 + 34, 85 + 34 *2, 85, 85 + 34, 85 + 34*2,85 + 34*3,
                85, 85 + 34, 85 + 34*2,85 + 34*3,85,85 + 34,85 + 34*2,85,85 + 34,85,
                85,   85 + 34, 85,   85 + 34, 85 + 34*2,   85, 85 + 34, 85 + 34*2, 85 + 34*3,   85, 85 + 34, 85 + 34*2, 85 + 34*3, 85+34*4,
                85, 85 + 34, 85 + 34*2, 85 + 34*3, 85+34*4, 85+34*5,   85, 85 + 34, 85 + 34*2, 85 + 34*3, 85+34*4, 85+34*5, 85+34*6]

    pipe1 = []
    pipe1.append(900)
    pipe1.append(1500)
    pipe1.append(2100)
    pipe1.append(2800)

    pipe2 = []
    pipe2.append(1200)


    randomboxC = []
    randomboxC.append(374)
    randomboxC.append(238)
    randomboxC.append(34 * 69)
    randomboxC.append(34 * 75)
    randomboxC.append(34 * 113)
    randomboxC.append(34 * 114)
    randomboxC.append(34 * 115)

    randomboxC2 = []
    randomboxC2.append(34*72)


    randomboxI = []
    randomboxI.append(442)
    randomboxI.append(34 * 72)

    coin = []
    for i in range(340, 544, 68):
        coin.append(i)


    ## 몬스터
    goomba = [100, 750, 1050, 1350, 2500, 2600, 34*115, 34*117, 34*119]
    m = [34*125]

    def update(self):
        pass