import sys
import pathlib
import time
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from Judgement import ooooTimeJudge

tclass = ooooTimeJudge.TimeJudge()
res = tclass.judge(20)

print("jugde_result")
print(res)