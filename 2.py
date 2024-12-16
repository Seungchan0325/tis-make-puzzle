import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "DIFFERENTIAL CONVERTER"

description = [
    "READ VALUES FROM IN.A AND IN.B",
    "WRITE IN.A - IN.B TO OUT.P",
    "WRITE IN.B - IN.A TO OUT.N"
]

layout = [
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_DAMAGED,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100
MIN = 0
MAX = 99

IN_A = [random.randint(MIN, MAX) for _ in range(NUM)]
IN_B = [random.randint(MIN, MAX) for _ in range(NUM)]
OUT_P = [a - b for a, b in zip(IN_A, IN_B)]
OUT_N = [b - a for a, b in zip(IN_A, IN_B)]

streams = [
    [STREAM_INPUT, "IN.A", 1, IN_A],
    [STREAM_INPUT, "IN.B", 2, IN_B],
    [STREAM_OUTPUT, "OUT.P", 1, OUT_P],
    [STREAM_OUTPUT, "OUT.N", 2, OUT_N]
]

create("2.txt", name, description, streams, layout)
