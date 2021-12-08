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

    block2 = []
    # block2.append(map.Block2())
    # for i in range()

    pipe1 = []
    # for i in range(2):
    #     pipe1.append((950, 102 + 34*i))
    # for i in range(3):
    #     pipe1.append((1050, 102 + 34*i))
    # for i in range(2):
    #     pipe1.append((1150, 102 + 34*i))
    pipe1.append(900)
    pipe1.append(1500)

    pipe2 = []
    pipe2.append(1200)




    randomboxC = []
    randomboxC.append(374)
    randomboxC.append(238)

    randomboxI = []
    randomboxI.append(442)

    coin = []
    for i in range(340, 544, 68):
        coin.append(i)


    ## 몬스터
    goomba = [100, 750, 2500]
    m = [400]

    def update(self):
        pass