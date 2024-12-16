import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "SELF-TEST DIAGNOSTIC"

description = [
    "READ A VALUE FROM IN.X AND WRITE THE VALUE TO OUT.X",
    "READ A VALUE FROM IN.A AND WRITE THE VALUE TO OUT.A",
]

layout = [
    TILE_COMPUTE, TILE_DAMAGED, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_DAMAGED, TILE_COMPUTE, TILE_DAMAGED,
    TILE_COMPUTE, TILE_DAMAGED, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100
MIN = 0
MAX = 99

IN_X = [random.randint(MIN, MAX) for _ in range(NUM)]
IN_A = [random.randint(MIN, MAX) for _ in range(NUM)]
OUT_X = [i for i in IN_X]
OUT_A = [i for i in IN_A]

streams = [
    [STREAM_INPUT, "IN.X", 0, IN_X],
    [STREAM_INPUT, "IN.A", 3, IN_A],
    [STREAM_OUTPUT, "OUT.X", 0, OUT_X],
    [STREAM_OUTPUT, "OUT.A", 3, OUT_A]
]

create("0.txt", name, description, streams, layout)
