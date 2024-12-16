import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "SEQUENCE GENERATOR"

description = [
    "SEQUENCE ARE ZERO-TERMINATED",
    "READ VALUES FROM IN.A AND IN.B",
    "WRITE THE LESSER VALUE TO OUT",
    "WRITE THE GREATER VALUE TO OUT",
    "WRITE 0 TO END THE SEQUENCE",
]

layout = [
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_DAMAGED, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100
MIN = 0
MAX = 99

IN_A = [random.randint(MIN, MAX) for _ in range(NUM)]
IN_B = [random.randint(MIN, MAX) for _ in range(NUM)]
OUT = []

for a, b in zip(IN_A, IN_B):
    if a < b:
        OUT.append(a)
        OUT.append(b)
        OUT.append(0)
    else:
        OUT.append(b)
        OUT.append(a)
        OUT.append(0)

streams = [
    [STREAM_INPUT, "IN.A", 1, IN_A],
    [STREAM_INPUT, "IN.B", 2, IN_B],
    [STREAM_OUTPUT, "OUT", 2, OUT]
]

create("5.txt", name, description, streams, layout)
