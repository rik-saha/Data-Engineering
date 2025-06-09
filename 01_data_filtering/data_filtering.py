import pandas as pd

# To ead the CSV file
df = pd.read_csv('students.csv')

# Function that returns the values filtered according to the column
# to be used multiple times to filter data
def filter_dataframe(dataframe, column_name, filter_value):
    return dataframe[dataframe[column_name] == filter_value]

# 1. Students from San francisco
sf_students = filter_dataframe(df, 'City', 'San Francisco')
print("Number of students from San Francisco:", len(sf_students))

# 2 Average age of Chicago Students
chicago_students = filter_dataframe(df, 'City', 'Chicago')
print("Average age of students of Chicago:", chicago_students['Age'].mean())

# 3. Students aged 30 or older
older_students = df[df['Age'] >= 30]
print("Number of students aged 30 or older:", len(older_students))