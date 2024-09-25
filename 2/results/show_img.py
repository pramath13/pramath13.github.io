import matplotlib.pyplot as plt

im1 = plt.imread('./2/results/angry_woman.jpg')/255.
im2 = plt.imread('./2/results/woman-1.jpg')/255
# im3 = plt.imread('./2/results/tahoe_vert_blend.png')

fig = plt.figure() 
rows = 1
columns = 2
fig.add_subplot(rows, columns, 1, xticks=[], yticks=[])
plt.imshow(im1) 
fig.add_subplot(rows, columns, 2, xticks=[], yticks=[])
plt.imshow(im2) 

fig.add_subplot(rows, columns, 1)
plt.imshow(im1) 
fig.add_subplot(rows, columns, 2)
plt.imshow(im2) 
# fig.add_subplot(rows, columns, 3, xticks=[], yticks=[])
# plt.imshow(im3) 
fig.tight_layout()
plt.show()