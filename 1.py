import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "SIGNAL AMPLIFIER"

description = [
    "READ A VALUE FROM IN.A",
    "DOUBLE THE VALUE",
    "WRITE THE VALUE TO OUT.A"
]

layout = [
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_DAMAGED,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_DAMAGED, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100
MIN = 0
MAX = 99

IN_A = [random.randint(MIN, MAX) for _ in range(NUM)]
OUT_A = [2 * i for i in IN_A]

streams = [
    [STREAM_INPUT, "IN.A", 1, IN_A],
    [STREAM_OUTPUT, "OUT.A", 2, OUT_A]
]

create("1.txt", name, description, streams, layout)
