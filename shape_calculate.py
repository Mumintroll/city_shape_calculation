import shapefile

import os
import shapefile as shp
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.abspath(__file__))



sf = shp.Reader(dir_path + "/city_test/test_building.shp")

myshp = open(dir_path + "/city_test/test_building.shp", "rb")
mydbf = open(dir_path + "/city_test/test_building.dbf", "rb")
r = shapefile.Reader(shp=myshp, dbf=mydbf)



def calculate_square(records : shapefile.Reader, type_square="com") -> float :
    # return sum(lambda m: m[7], records)
    summ = 0
    attribute = 7
    if type_square == "com":
        attribute = 7
    elif type_square == "home":
        attribute = 8
    for record in records:
        summ += record[attribute]
    return summ

print(calculate_square(r.records(), "com"))
print(calculate_square(r.records(), "home"))

class GridCell:
    id = 0
    total_home = 0
    total_com = 0
    buildings = []

    def __init__(self, buildings):
        self.buildings = buildings

sf2 = shp.Reader(dir_path + "/grid/grid2.shp")

plt.figure()
# second_shapes = list((lambda w: w.points , sf2.shapes())[1])
# print(second_shapes)


for shape in sf.shapeRecords():
    # print(poly_intersection(PL1, PL2))
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.show()


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def poly_intersection(poly1, poly2):

    for i, p1_first_point in enumerate(poly1[:-1]):
        p1_second_point = poly1[i + 1]

        for j, p2_first_point in enumerate(poly2[:-1]):
            p2_second_point = poly2[j + 1]

            if line_intersection((p1_first_point, p1_second_point), (p2_first_point, p2_second_point)):
                return True

    return False

PL1 = ((-1, -1), (1, -1), (1, 2))
PL2 = ((0, 1), (2, 1))

print(poly_intersection(PL1, PL2))