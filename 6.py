import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "SEQUENCE COUNTER"

description = [
    "SEQUENCE ARE ZERO-TERMINATED",
    "READ A SEQUENCE FROM IN",
    "WRITE THE SUM TO OUT.S",
    "WRITE THE LENGTH TO OUT.L",
]

layout = [
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_DAMAGED,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100
MIN = 0
MAX = 99

IN = []
OUT_S = []
OUT_L = []

for i in range(10):
    length = random.randint(1, 5)
    sequence = [random.randint(MIN, MAX) for _ in range(length)]
    IN.extend(sequence)
    IN.append(0)
    OUT_S.append(sum(sequence))
    OUT_L.append(length)

streams = [
    [STREAM_INPUT, "IN", 1, IN],
    [STREAM_OUTPUT, "OUT.S", 1, OUT_S],
    [STREAM_OUTPUT, "OUT.L", 2, OUT_L],
]

create("6.txt", name, description, streams, layout)
