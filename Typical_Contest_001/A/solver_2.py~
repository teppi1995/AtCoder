import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
#logging.disable(logging.CRITICAL)

H, W = (int(x) for x in input().split())

fields = [list("#" * (W + 2))]
fields.extend([list("#" + input() + "#") for _ in range(H)])
fields.append(list("#" * (W + 2)))

logging.info(fields)

sl, sr = 0, 0
for i, line in enumerate(fields):
    if "s" in line:
        sl = i
        sr = line.index("s")

dlr = ((0, 1), (0, -1), (1, 0), (-1, 0))
stack = []
stack.append([sl, sr])

while stack:
    cl, cr = stack.pop()
    for dl, dr in dlr:
        nl = cl + dl
        nr = cr + dr
        logging.info([nl, nr])

        if fields[nl][nr] == "#":
            continue
        if fields[nl][nr] == "g":
            print("Yes")
            exit()
        stack.append([nl, nr])
        fields[nl][nr] = "#"

print("No")
