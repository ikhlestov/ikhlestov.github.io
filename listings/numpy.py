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
