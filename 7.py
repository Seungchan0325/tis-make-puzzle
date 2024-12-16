import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "SIGNAL EDGE DETECTOR"

description = [
    "READ A VALUE FROM IN",
    "COMPARE VALUE TO PREVIOUS VALUE",
    "WRITE 1 IF CHANGED BY 10 OR MORE",
    "IF NOT TRUE, WRITE 0 INSTEAD",
    "THE FIRST OUTPUT IS ALWAYS 0",
]

layout = [
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_DAMAGED, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100
MIN = -40
MAX = 40

IN = [0]
IN.extend([random.randint(MIN, MAX) for _ in range(NUM-1)])

OUT = [0]
for i in range(1, NUM):
    if abs(IN[i] - IN[i-1]) >= 10:
        OUT.append(1)
    else:
        OUT.append(0)

streams = [
    [STREAM_INPUT, "IN", 1, IN],
    [STREAM_OUTPUT, "OUT", 2, OUT]
]

create("7.txt", name, description, streams, layout)
