
import numpy as np
import matplotlib.pyplot as plt
# Land -> 1 & Water -> 0
# inits random binary matrix 33x33
Mx = np.random.randint(0,2, (33,33))
y, x = len(Mx)-1, len(Mx[0])-1
# fills the land matrix with water 
# up to the boundaries 
# of the land exit from it
land = Mx.copy() 
land[1:y, 1:x] = 0
# coastal lands
shelf = Mx.copy() 
isles = shelf[1:y, 1:x]
# uses the structuring element to
# morphology dilation 
# of a coastal land
elem = np.array(
[[0,1,0],
 [1,0,1],
 [0,1,0]])
# morfology process
for _ in range(max(y,x)//2):
  for i in range(len(isles)):
    for j in range(len(isles[0])):
      if isles[i,j]:
        isl = land[i:i+3,j:j+3]*elem
        if isl.sum():
          # land grows
          land[i+1,j+1] = 1
          # water comes
          isles[i,j] = 0
# plots 
ax = []
fig = plt.figure(
dpi = 300, figsize = (6, 20))

def plot_(Mx, i, s):
  ax.append(
  fig.add_subplot(3, 1, i))
  ax[-1].matshow(Mx)
  plt.title(s, color='w')
  plt.axis('off')

plot_(Mx,    1, 'LAND & BAY')
plot_(shelf, 2, 'REMOVED ISLES')
plot_(land,  3, 'LAND & SHELF')

plt.savefig("plt.png",
facecolor='black')

