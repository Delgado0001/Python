#lambda2.py DDG
def myfunc(n):
  return lambda a : a * n
  
  mydoubler = myfunc(2)
  mytripler = myfunc(3)
  dub = mydoubler(12)
  trip = mytripler(12)
  
  print("dub ",dub)
  print("trip",trip)
