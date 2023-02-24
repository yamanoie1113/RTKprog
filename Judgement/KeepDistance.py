import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')
from Judgement import Judge

from Sensors import PositionMgmt as PMgmt,TurnAngleSensor as TASensor

class KeepDistance(Judge.Judge):

    def judge():

        pass

    def set_param():

        pass