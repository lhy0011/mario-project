#1스테이지 맵 제작

class Map1:
    ground = []

    for i in range(50):
        ground.append(34 * i)
    for i in range(52,67): #2칸 띄고
        ground.append(34 * i)
    for i in range(70, 120): #3칸 띄고
        ground.append(34 * i)
    for i in range(122, 162): #2칸 띄고
        ground.append(34 * i)

    pipe = []


    block = []
    # for i in range

    coin = []
    for i in range(340, 544, 68):
        coin.append(i)


    ## 몬스터
    goomba = [100, 750, 2500]
    m = [400]