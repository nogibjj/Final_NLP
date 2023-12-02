import pandas as pd
import re
from collections import Counter

# Function to extract headers from a single text
def extract_headers(text):
    # Convert text to lowercase to ensure consistent matching
    text = text.lower()
    # Regex to match any line ending with a colon that is not a date/time and does not start with a number
    pattern = re.compile(r"^(?!\d+/\d+/\d+.*)(?!.*\d:\d.*[ap]m)(.*\S.*?):.*$", re.MULTILINE)
    headers = Counter(re.findall(pattern, text))
    return headers

# Function to serialize Counter object into a string
def serialize_counter(counter):
    return '; '.join([f"{header}: {count}" for header, count in counter.items()])

# Function to apply header extraction to a DataFrame column and serialize the results
def apply_header_extraction_to_df(df, text_column):
    # Apply the extract_headers function to each row in the text column
    # and then serialize the Counter object
    df['Headers'] = df[text_column].apply(lambda text: serialize_counter(extract_headers(text)) if pd.notnull(text) else '')
    return df

# Read the CSV file into a DataFrame
df = pd.read_csv("01_intermediate-files/raw_parsed_xml.csv")

# Apply the header extraction and serialization
df = apply_header_extraction_to_df(df, 'Text')

# Inspect the result
print(df.head())

# Save the updated DataFrame to CSV
df.to_csv("01_intermediate-files/parsed_rows_with_headers_all.csv", index=False)