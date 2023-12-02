import pandas as pd
import re
from collections import Counter

# Function to extract headers from a single text
def extract_headers(text):
    # Convert text to lowercase to increase match likelihood
    text = text.lower()
    # Regex to match any line ending with a colon that is not a date/time and does not start with a number
    pattern = re.compile(r"^(?!\d+/\d+/\d+.*)(?!.*\d:\d.*[AP]M)(.*\S.*?):.*$", re.MULTILINE | re.IGNORECASE)
    headers = Counter(re.findall(pattern, text))
    return headers

# Function to apply header extraction to the entire DataFrame
def apply_header_extraction_to_df(df, text_column):
    # Concatenate all text into one string
    combined_text = ' '.join(df[text_column].dropna())
    # Extract headers from the combined text
    all_headers = extract_headers(combined_text)
    return all_headers

# Read the CSV file into a DataFrame
df = pd.read_csv("01_intermediate-files/raw_parsed_xml.csv")

# Apply the header extraction to the entire DataFrame
all_headers = apply_header_extraction_to_df(df, 'Text')

# Convert the header counter to a DataFrame
headers_df = pd.DataFrame(all_headers.items(), columns=['Header', 'Count'])

# Save the DataFrame to CSV
headers_df.to_csv("01_intermediate-files/headers_count.csv", index=False)

# Inspect the result
print(headers_df)

