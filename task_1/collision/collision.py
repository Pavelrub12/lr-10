def isCorrectRect(array):
    x1, y1 = array[0]
    x2, y2 = array[1]
    if x2 > x1 and y2 > y1:
        return True
    return False
