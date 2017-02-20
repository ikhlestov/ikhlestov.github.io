# change display methods
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

# split some array in folds(numpy)
y_folds = np.array_split(y_digits, 3)

# shuffle the indices for test data
indexes = np.random.permutation(len(iris_X))

# select max value based on another array max value(numpy)
best_alpha = alphas[scores.index(max(scores))]

# reshape one array to another one shape
face_compressed.shape = face.shape

# Reshape numpy array with dynamically calculated second dimension
test_data = np.zeros((4, 3))
test_data.shape  # (4, 3)
reshaped = test_data.reshape((6, -1))
reshaped.shape  # (6, 2)

# Create list of 3 random items form 0 to 255
np.random.randint(0, high=256, size=(3, )).tolist()

# assign values to one line in array(notes for tensorflow)
M_t = np.arange(15).reshape(5, 3)
# array([[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11],
#        [12, 13, 14]])
indexes = np.array([0, 1, 0, 0, 0])
new_value = np.arange([101, 102, 103])
(M_t.T * (-1 * (indexes -1))).T + np.outer(indexes, new_value)
# array([[  0,   1,   2],
#        [103, 104, 105],
#        [  6,   7,   8],
#        [  9,  10,  11],
#        [ 12,  13,  14]])


