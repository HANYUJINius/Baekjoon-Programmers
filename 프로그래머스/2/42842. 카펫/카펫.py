def solution(brown, yellow):
    allBlock = brown + yellow

    width = 3
    height = 1

    while True:
        height = allBlock // width
        remainder = allBlock % width

        if remainder == 0 and width >= height and yellow == (width-2) * (height-2):
            return [width, height]
        width += 1