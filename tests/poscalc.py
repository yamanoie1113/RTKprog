import csv

origin_x,origin_y = 70788.81836454148, -171739.42465955665
filename = '../parameter/Perfect_Circuit_Course_Pos.prm'

export = '../Sensors/diff.csv'


with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        pos = [row for row in reader]

with open(export,'w',newline="") as exf:
    writer = csv.writer(exf)

    for i in pos:
        #print(i)
        diff_x = float(i[0]) - origin_x
        diff_y = float(i[1]) - origin_y

        #print(dif_x,dif_y)

        writer.writerow([diff_x,diff_y])

diff_file = 'diff.csv'

with open(diff_file) as diff1:
    reader = csv.reader(diff1)
    for row in reader:
        pos_diff = [row for row in reader]

