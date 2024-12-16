import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "INTERRUPT HANDLER"

description = [
    "READ FROM IN.1 THROUGH IN.4",
    "WRITE THE INPUT NUMBER WHEN THE VALUE GOES FROM 0 TO 1",
    "TWO INTERRUPTS WILL NEVER CHANGE IN THE SAME INPUT CYCLE",
]

layout = [
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_DAMAGED, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100

PRV_1 = 0
PRV_2 = 0
PRV_3 = 0
PRV_4 = 0

IN_1 = [0]
IN_2 = [0]
IN_3 = [0]
IN_4 = [0]

OUT = [0]

for _ in range(NUM):
    interrupt = random.choice([0, 1, 2, 3, 4])
    if interrupt == 0:
        OUT.append(0)
    elif interrupt == 1:
        if PRV_1 == 0: OUT.append(1)
        else: OUT.append(0)
        PRV_1 = 1 - PRV_1
    elif interrupt == 2:
        if PRV_2 == 0: OUT.append(2)
        else: OUT.append(0)
        PRV_2 = 1 - PRV_2
    elif interrupt == 3:
        if PRV_3 == 0: OUT.append(3)
        else: OUT.append(0)
        PRV_3 = 1 - PRV_3
    elif interrupt == 4:
        if PRV_4 == 0: OUT.append(4)
        else: OUT.append(0)
        PRV_4 = 1 - PRV_4
    IN_1.append(PRV_1)
    IN_2.append(PRV_2)
    IN_3.append(PRV_3)
    IN_4.append(PRV_4)

streams = [
    [STREAM_INPUT, "IN.1", 0, IN_1],
    [STREAM_INPUT, "IN.2", 1, IN_2],
    [STREAM_INPUT, "IN.3", 2, IN_3],
    [STREAM_INPUT, "IN.4", 3, IN_4],
    [STREAM_OUTPUT, "OUT", 2, OUT],
]

create("8.txt", name, description, streams, layout)
