import sys,pathlib,csv
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir) + '/../')

from Judgement import DistanceJudge

class WalkingCircuit():

    #param_file = '/home/pi/Desktop/rtkprog_git/RTKprog/parameter/Circuit_Pos.prm'
    param_file = '/Users/takak/OneDrive/ドキュメント/GitHub/RTKplog2/parameter/Circuit_Pos.prm'

    def __init__(self) -> None:
        pass

    def get_target_pos(self):

        param=[]
        with open(self.param_file, mode='r') as f:
        # parameterファイルreaderの生成
            reader = csv.reader(f)
            #reader_header=next(f)

            for prm in reader:
                param.append([elem for elem in prm])
        #print("debbb",param)
        for i in range(len(param)):
            for j in range(len(param[i])):

                param[i][j] = float(param[i][j])
        #print(param)




def main():
    test = WalkingCircuit()
    test.get_target_pos()

if __name__ == '__main__':
    main()