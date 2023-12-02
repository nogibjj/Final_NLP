import pandas as pd

# Read the CSV file into a DataFrame
df1 = pd.read_csv('01_intermediate-files/extracted_text_with_separate_columns.csv')

# Select the desired columns
df2 = df1[['Smoking Status', 'Matched Headers Text']]

# Rename the 'Matched Headers Text' column to 'Text' in df2
df2.rename(columns={'Matched Headers Text': 'Text'}, inplace=True)

# Save the new DataFrame to a CSV file with a proper filename and extension
df2.to_csv('01_intermediate-files/smokers_train_all_separated.csv', index=False)