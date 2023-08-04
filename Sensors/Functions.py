import  math

#関数を作成

#与えられた２点の中点を計算しx,yで返す
def calc_midpoint(sx,sy,gx,gy):
    midx = (sx+gx)/2
    midy = (sy+gy)/2

    return midx,midy


#扇形の弧の長さを求め、返す 引数：半径,角度
def calc_arc(radius,angle):
    arc = 2*math.pi * radius * (angle/360)
    return arc


#円周の計算 引数:直径
def calc_circ(diameter):
    circ = diameter * math.pi
    return circ



#曲線仮想ライントレース用の円を描く
def draw_circle():
    pass


