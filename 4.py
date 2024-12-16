import random
from create_puzzle import create

TILE_COMPUTE = "TILE_COMPUTE"
TILE_DAMAGED = "TILE_DAMAGED"
TILE_MEMORY = "TILE_MEMORY"

STREAM_INPUT = "STREAM_INPUT"
STREAM_OUTPUT = "STREAM_OUTPUT"

name = "SIGNAL MULTIPLEXER"

description = [
    "READ VALUES FROM IN.A AND IN.B",
    "READ A VALUE FROM IN.S",
    "WRITE IN.A WHEN IN.S = -1",
    "WRITE IN.B WHEN IN.S = 1",
    "WHEN IN.A + IN.B WHEN IN.S = 0"
]

layout = [
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
    TILE_DAMAGED, TILE_COMPUTE, TILE_COMPUTE, TILE_COMPUTE,
]

NUM = 100
MIN = 0
MAX = 99

IN_A = [-random.randint(MIN, MAX) for _ in range(NUM)]
IN_B = [random.randint(MIN, MAX) for _ in range(NUM)]
IN_S = [random.choice([-1, 0, 1]) for _ in range(NUM)]
OUT = [a if s == -1 else b if s == 1 else a + b for a, b, s in zip(IN_A, IN_B, IN_S)]

streams = [
    [STREAM_INPUT, "IN.A", 1, IN_A],
    [STREAM_INPUT, "IN.S", 2, IN_S],
    [STREAM_INPUT, "IN.B", 3, IN_B],
    [STREAM_OUTPUT, "OUT", 2, OUT],
]

create("4.txt", name, description, streams, layout)
