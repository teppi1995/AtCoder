import numpy

N, D = (int(x) for x in input().split())
points = []
points.extend(list(int(x) for x in input().split()) for _ in range(N))

def cal_distance(point1, point2):
    return numpy.linalg.norm(numpy.array(point1) - numpy.array(point2))

if __name__ == "__main__":
    counter = 0
    for i in range(N):
        for j in range(i + 1, N):
            print(cal_distance(points[i], points[j]))
            if cal_distance(points[i], points[j]).is_integer():
                counter += 1

    print(counter)
