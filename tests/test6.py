
import csv


class test6:
    
    def test(self):

        while True:
                print('<Corse select> 1:Normal_Course 2:REIWA_Course 3:Circuit_Course')
                course_select = input('>> ')
                    
                if course_select in ['1','2','3']:
                    print('OK',course_select)
                    break
                
                else:
                    print('Try agein')
                    
        param_file=('/home/pi/Desktop/rtkprog_git/RTKprog/parameter/Normal_Course.prm')
        param=[]
        with open(param_file, mode='r') as f:
            # parameterファイルreaderの生成
            reader = csv.reader(f)
            reader_header=next(f)
            # parameter readerからデータを取り出してループ
            for prm in reader:
            # strからfloatにキャストして追加
                param.append([elem for elem in prm])
                
        for i in range(len(param)):
            for j in range(len(param[i])-1):
                param[i][j] = float(param[i][j])
                
        #if param[0][4]=='straight':       
        print(param)



def main():
    test = test6()
    test.test()

if __name__ == '__main__':
    main()