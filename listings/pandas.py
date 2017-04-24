import pandas as pd

# load the data
data = pd.read_csv("csv_name.csv")

# get first lines of data
print(data.head(5))

# get useful info regarding datased
print(data.describe())
print(train_set.info())

# change print options of pandas
pd.options.display.<tab>

# fill not existing variabels in column with median
data['Age'] = data["Age"].fillna(data["Age"].median())

# select all 'male' records from the "Sex" column
data.loc[data["Sex"] == "male", "Sex"]

# replace all values with 0
data.loc[data["Sex"] == "male", "Sex"] = 0
data.loc[bool_mask, "column_to_fetch"] = value

# get unique values from column
data["Embarked"].unique()

# select only required rows
data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]

# count values in data frame
# get how many "True" entries exist in data frame
tmp_res.value_counts()[True]

# another way to count data from list
titles = titanic["Name"].apply(get_title)
print(pandas.value_counts(titles))

# generate new column from previous one
titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]

# generate new column with .apply method
# The .apply method generates a new series
titanic["NameLength"] = titanic["Name"].apply(lambda x: len(x))

# filter dataframe based on series
df = df[df.filename.isin(df_clear.filename)]

# but sometimes more useful to apply method "by hands"
# we have nearly the same perfomance, but more verbose output
# previously you should install "tqdm"
result_array = []
for i in tqdm(xrange(0, len(data["column_name"]))):
    new_data = some_function( data["column_name"][i] )
    result_array.append(new_data)

# skip rows during data loading
test_set = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test',
                      skiprows = 1, header = None)

# add names for colums
column_labels = ['first', 'second', 'title']
test_set.columns = column_labels

# remove all rows contains '?' question mark
train_set.replace(' ?', np.nan).dropna()

# replace one value by another in column
test_nomissing['wage_class'] = test_nomissing.wage_class.replace({' <=50K.': ' <=50K', ' >50K.':' >50K'})

# concatenate two datasets vertically
combined_set = pd.concat([train_nomissing, test_nomissing], axis = 0)

# replace every sting value to the integer
# Loop through all columns in the dataframe
for feature in combined_set.columns:
    # Only apply for columns with categorical strings
    if combined_set[feature].dtype == 'object':
        # Replace strings with an integer
        combined_set[feature] = pd.Categorical(combined_set[feature]).codes

# create pandas data frame from data and save it
# assume that data - nested list of lists, when each nested list - values for one line
columns = ['word_1', 'word_2', 'target_similarity', 'calculated_similarity']
df = pd.DataFrame(data=data, columns=columns)
df = pd.DataFrame(data=csv_lines, columns=columns)
df.to_csv(save_file_name, index=False, header=True)

# create new dataframe if not exists or use existing one
# csv_columns = list of names for columns
# csv_data = dict with keys same as columns names
if os.path.exists(csv_f_name):
    main_csv = pd.read_csv(csv_f_name, index_col=0)
else:
    main_csv = pd.DataFrame(columns=csv_columns)
main_csv = main_csv.append(csv_data, ignore_index=True)
main_csv.to_csv(csv_f_name, index=True, header=True, na_rep='NaN')
