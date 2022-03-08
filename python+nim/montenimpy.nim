import math
import random 
import nimpy

randomize()
proc approxpi(nthrows: float): float {.exportpy.} =
  var inside = 0.0
  for i in 1..int64(nthrows):
    if hypot(rand(1.0), rand(1.0)) <= 1:
      inside += 1
  result = 4 * inside / nthrows

