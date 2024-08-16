import numpy as np
def nearest_neighbor(array_no_1, array_no_2, norm=2):
    
    nearest_pairs = []
    
    for point1 in array_no_1:
        distances = np.linalg.norm(array_no_2 - point1, ord=norm, axis=1)
        nearest_index = np.argmin(distances)
        nearest_pairs.append((point1, array_no_2[nearest_index]))
    
    return nearest_pairs

array_no_1 =np.array([[1, 2], [3, 4], [5, 6]])
array_no_2 = np.array([[1, 1], [4, 4], [7, 7]])

nearest_neighbors = nearest_neighbor(array_no_1, array_no_2, norm=2)

for pair in nearest_neighbors:
    print(f"Point {pair[0]} in array_no_1 is closest to point {pair[1]} in array_no_2.")