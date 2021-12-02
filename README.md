ThreadPoolExecutor
timeout: 500ms

treads: 1
time > 15m
cpu ~1%
memory ~15mb
network ~100kb

threads: 100
time: 41180ms
cpu ~12%
memory ~50mb
network ~5mb

threads: 250
time: 18167ms
cpu ~20%
memory ~100mb
network ~8mb

threads: 500
time: 17352ms
cpu ~30%
memory ~150mb
network ~8mb

threads: 1000
time: 21403ms
cpu ~30%
memory ~150mb
network ~9mb

---------------------

ProcessPoolExecutor
intel 7020u 3 coins

time 113s process 1
cpu ~22% memory 7.5mb

time 82s process 2
cpu ~48% memory 2 * 7.5mb

time 31s process 4
cpu ~82% memory 4 * 7.5mb

time 32s process 8
cpu ~82% memory 8 * 7.5mb

time 73s process 16
cpu ~82 memory 16 * 7.5 mb