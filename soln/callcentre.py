# read the first line
  n , q = list(map(int, input().split()))

  # read the calls
  calls = [int(i) for i in input().split()]

  s_array , t_array = [], []
  # read and process each query
  for i in (range(0,q)):
     s , t = list(map(int, input().split()))
     s_array.append(s)
     t_array.append(t)

#print  the answer
sorting = {} #empty dictionary
#how many quaries between eacth s and t array
for i in range(0, q):
    sorting[i] = sum(calls[s_array[i] - 1:t_array[i]])

for k, v in sorting.items():
    print(v)
