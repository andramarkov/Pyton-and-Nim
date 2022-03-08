import math
import random 
import times

randomize()
proc approxpi(nthrows: float): float =
  var inside = 0.0
  for i in 1..int64(nthrows):
    if hypot(rand(1.0), rand(1.0)) <= 1:
      inside += 1
  result = 4 * inside / nthrows

let time = cpuTime()
echo "pi: ",approxpi(100000000)," in: ", cpuTime() - time





#nim compile --run  --gc:refc --passC:"-flto" -d:release monte.nim
