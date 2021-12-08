#1스테이지 맵 제작

import map


class Map1:
    ground = []

    # for i in range(50):
    #     ground.append(34 * i)
    # for i in range(52,67): #2칸 띄고
    #     ground.append(34 * i)
    # for i in range(70, 120): #3칸 띄고
    #     ground.append(34 * i)
    # for i in range(122, 162): #2칸 띄고
    #     ground.append(34 * i)
    for i in range(150):
        ground.append(34 * i)

    pipe = []


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
    block2_2 = [85, 85, 85 + 34, 85, 85 + 34, 85 + 34 *2, 85, 85 + 34, 85 + 34*2,85 + 34*3,   85, 85 + 34, 85 + 34*2,85 + 34*3,85,85 + 34,85 + 34*2,85,85 + 34,85]

    pipe1 = []
    # for i in range(2):
    #     pipe1.append((950, 102 + 34*i))
    # for i in range(3):
    #     pipe1.append((1050, 102 + 34*i))
    # for i in range(2):
    #     pipe1.append((1150, 102 + 34*i))
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

    randomboxI = []
    randomboxI.append(442)
    randomboxI.append(34 * 72)

    coin = []
    for i in range(340, 544, 68):
        coin.append(i)


    ## 몬스터
    goomba = [100, 750, 2500, 2600]
    m = [400]

    def update(self):
        pass