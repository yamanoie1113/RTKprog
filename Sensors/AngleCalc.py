import math

def CalcAng(goal_x,goal_y):
    start_x = 0.0
    start_y = 0.0



    x = (goal_x - start_x)
    y = (goal_y - start_y)

    r = math.atan2(y,x)

    if r < 0 :
        r = r + 2 * math.pi

    angle = math.floor(r * 360 / (2 * math.pi))

    print(angle)

def main():
    CalcAng(-10,-10)

if __name__ == '__main__':
    main()
