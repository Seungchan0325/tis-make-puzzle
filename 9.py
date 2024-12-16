import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "SIGNAL PATTERN DETECTOR"

description = [
    "READ A VALUE FROM IN",
    "LOOK FOR THE PATTERN 0,0,0",
    "WRITE 1 WHEN PATTERN IS FOUND",
    "IF NOT TRUE, WRITE 0 INSTEAD",
]

layout = [
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_DAMAGED,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100
MIN = 0
MAX = 99

IN = [random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]) for _ in range(NUM)]
OUT = [0, 0]
for i in range(2, NUM):
    if IN[i-2:i+1] == [0, 0, 0]:
        OUT.append(1)
    else:
        OUT.append(0)

assert len(IN) == len(OUT)

streams = [
    [STREAM_INPUT, "IN", 1, IN],
    [STREAM_OUTPUT, "OUT", 2, OUT],
]

create("9.txt", name, description, streams, layout)
