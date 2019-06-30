import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logging.disable(logging.CRITICAL)

W, H, x, y  = (int(x) for x in input().split())

logging.info(L)

max_menseki = float(W) * float(H) / 2.0
if W / 2 == x and H / 2 == y:
    print("{:f}".format(max_menseki) + " " + str(1))
else:
    print("{:f}".format(max_menseki) + " " + str(0))

    
