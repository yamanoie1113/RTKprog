import sys
import pathlib
import numpy as np
import math
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Sensors import MotorMgmt
from Walker import PID2

def calcRadius(start_pos:tuple, goal_pos:tuple, param:float=1, curvature_gain:float=0.4) -> (tuple, float):
    '''
    2点間の座標を円弧を描きながら走行する際の円の中心座標及びその半径を返す.
    　パラメータを半開区開(0,1]の範囲で設定する,このときパラメータが0に近づけば曲線は直線に近づき,1に近づけば半円に近づく.

    Parameters
    ----------
    start_pos : tuple
        スタート位置の座標
    goal_tpos : tuple
        ゴール位置の座標
    param : froat
        走行する円弧の設定パラメータ
    curvature_gain float
        パラメータの変化の度合いを調整するための定数
    
    Returns
    -------
    circle_central_pos : tuple
        円の中心座標
    radius_squared : froat
        円の半径の二乗
    '''

    if type(start_pos)!=tuple or type(goal_pos)!=tuple:
        raise TypeError('座標がタプルではありません.')

    # tupleをndarrayに変換
    start_vec = np.array(start_pos)
    goal_vec = np.array(goal_pos)

    # パラメータ調整
    if not (0<param and param<=1):
        raise ValueError('パラメータが不正な値です.')
    
    param = math.tan((math.pi*(param-1))/2) * curvature_gain

    # start-goal間の法線ベクトル
    n_vec = np.dot((goal_vec-start_vec), np.array([[0,-1],[1,0]]))

    # start-goal間の中点ベクトル
    middle_vec = (start_vec + goal_vec)/2

    # 円の中心ベクトル
    circle_center_vec = middle_vec + n_vec*param
    
    # 円の半径の二乗のスカラー
    radius_squared = ((start_vec-circle_center_vec)**2).sum()
    return tuple(circle_center_vec), radius_squared

