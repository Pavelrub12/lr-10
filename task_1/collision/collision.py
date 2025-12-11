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


def intersectionAreaRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise ValueError("Некорректный прямоугольник")
    
    if not isCorrectRect(rect2):
        raise ValueError("Некорректный прямоугольник")
    
    x1_1, y1_1 = rect1[0]
    x2_1, y2_1 = rect1[1]
    x1_2, y1_2 = rect2[0]
    x2_2, y2_2 = rect2[1]
    
    if x2_1 <= x1_2 or x2_2 <= x1_1:
        return 0.0
    
    if y2_1 <= y1_2 or y2_2 <= y1_1:
        return 0.0
    
    x_left = max(x1_1, x1_2)
    x_right = min(x2_1, x2_2)
    y_bottom = max(y1_1, y1_2)
    y_top = min(y2_1, y2_2)
    
    width = x_right - x_left
    height = y_top - y_bottom
    
    return float(width * height)

def intersectionAreaMultiRect(rectangles):
    for rect in rectangles:
        if not isCorrectRect(rect):
            raise ValueError("Некорректный прямоугольник")
    
    x_left = max(rect[0][0] for rect in rectangles)
    x_right = min(rect[1][0] for rect in rectangles)
    y_bottom = max(rect[0][1] for rect in rectangles)
    y_top = min(rect[1][1] for rect in rectangles)
    
    if x_right <= x_left or y_top <= y_bottom:
        return 0.0
    
    return (x_right - x_left) * (y_top - y_bottom)


