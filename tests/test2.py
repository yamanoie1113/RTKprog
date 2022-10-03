import pyproj

file_name = 'NMEA_sample.txt'

with open(file_name) as f:
    lines = f.readlines()
#print(lines)
#['Apple 150\n', 'Banana 200\n', 'Orange 100\n', 'Grape 500\n', 'Apple 200\n', 'Lemon 100\n', 'Apple 100\n', 'Peach 300\n', 'Mango 1000']


lines_strip = [line.strip() for line in lines ]
#print(lines_strip)
# ['Apple 150', 'Banana 200', 'Orange 100', 'Grape 500', 'Apple 200', 'Lemon 100', 'Apple 100', 'Peach 300', 'Mango 1000']

"""
list_Apple = [line_s for line_s in lines_strip if 'Apple' in line_s ]
print(list_Apple)
# ['Apple 150', 'Apple 
# 
# 
# 
# 200', 'Apple 100']

"""

while True:
    list_GGA = [line_s for line_s in lines_strip if '$GPGGA' in line_s ]
    cnt = 0
    tmp = list_GGA[1].split(',') 
    print(tmp[2])#緯度を抽出
    break
    while cnt > 2:
        pass
        #print(list_GGA)
    # ['150', '200', '100']


"""
ggacnt = 0
with open("NMEA_sample.txt") as temp_f:
    datafile = temp_f.readlines()
for line in datafile:
    if "$GPGGA," in line:
        ggacnt += 1
        if "," in line and ggacnt <2:
            print()
            """
        



"""
transformer = pyproj.Transformer.from_crs("epsg:4326", "epsg:3857", always_xy=True)
 
transformer.transform(135.5, 39.5)
# => (15083791.002488568, 4793547.459104806)
 
print(transformer.transform([135.5, 135.6, 135.7], [39.5, 39.6, 39.7]))
# => ([15083791.002488568, 15094922.951567894, 15106054.900647221],
#     [ 4793547.459104806,  4807984.493190501,  4822442.387442776])
"""