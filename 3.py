import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "SIGNAL COMPARATOR"

description = [
    "READ A VALUE FROM IN",
    "WRITE 1 TO OUT.G IF IN > 0",
    "WRITE 1 TO OUT.E IF IN == 0",
    "WRITE 1 TO OUT.L IF IN < 0",
    "WHEN A 1 IS NOT WRITTEN TO AN OUTPUT, WRITE A 0 INSTEAD",
]

layout = [
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_DAMAGED, TILE_DAMAGED, TILE_DAMAGED,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100
MIN = -2
MAX = 2

IN = [random.randint(MIN, MAX) for _ in range(NUM)]
OUT_G = [1 if i > 0 else 0 for i in IN]
OUT_E = [1 if i == 0 else 0 for i in IN]
OUT_L = [1 if i < 0 else 0 for i in IN]

streams = [
    [STREAM_INPUT, "IN", 0, IN],
    [STREAM_OUTPUT, "OUT.G", 1, OUT_G],
    [STREAM_OUTPUT, "OUT.E", 2, OUT_E],
    [STREAM_OUTPUT, "OUT.L", 3, OUT_L]
]

create("3.txt", name, description, streams, layout)
