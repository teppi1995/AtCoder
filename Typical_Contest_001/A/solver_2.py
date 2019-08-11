import logging
import collections import deque


logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

H, W = (int(x) for x in input().split())

fields = [list("#" * (W + 2))]
fields.extend([list("#" + input() + "#") for _ in range(H)])
fields.append(list("#" * (W + 2)))

logging.info(fields)

sy, sx = 0, 0
for i, line in enumerate(fields):
    if "s" in line:
        sy = i
        sx = line.index("s")

dyx = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
###深さ優先探索###
# stack = []
# stack.append([sl, sr])

# while stack:
#     cl, cr = stack.pop()
#     for dl, dr in dlr:
#         nl = cl + dl
#         nr = cr + dr
#         logging.info([nl, nr])

#         if fields[nl][nr] == "#":
#             continue
#         if fields[nl][nr] == "g":
#             print("Yes")
#             exit()
#         stack.append([nl, nr])
#         fields[nl][nr] = "#"

###幅優先探索###

queue = deque([[sy, sx]])

while queue:
    cy, cx = queue.popleft()
    for dy, dx in dyx:
        ny = cy + dy
        nx = cx + dx
        logging.info([ny, nx])

        if fields[ny][nx] == "#":
            continue
        if fields[ny][nx] == "g":
            print("Yes")
            exit()

        queue.append([ny, nx])
        fields[ny][nx] = "#"
        

print("No")
