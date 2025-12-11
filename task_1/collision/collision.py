def isCorrectRect(array):
    x1, y1 = array[0]
    x2, y2 = array[1]
    if x2 > x1 and y2 > y1:
        return True
    return False

class RectCorrectError(Exception):
    pass

def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некорректный")
    
    if not isCorrectRect(rect2):
        raise RectCorrectError("1й прямоугольник некорректный")
    
    x1_1, y1_1 = rect1[0]
    x2_1, y2_1 = rect1[1]
    x1_2, y1_2 = rect2[0]
    x2_2, y2_2 = rect2[1]
    
    if x2_1 <= x1_2 or x2_2 <= x1_1:
        return False
    
    if y2_1 <= y1_2 or y2_2 <= y1_1:
        return False
    
    return True


