import pandas as pd
import re

# Function to extract text segments based on headers with more than one count
def extract_text_by_headers(text, headers):
    # Lowercase the text to ensure consistent matching
    text = text.lower()
    # Escape headers for regex, and sort headers by length in descending order to match longer headers first
    headers_pattern = '|'.join(sorted([re.escape(header) for header in headers], key=len, reverse=True))
    # Pattern to match headers and their corresponding text
    pattern = re.compile(fr"({headers_pattern})\s*:\s*(.*?)(?=\s*({headers_pattern})\s*:|\n{2,}|$)", re.DOTALL)

    # Find all matches and store them in a dictionary
    matches = pattern.findall(text)
    extracted_text = {}
    for match in matches:
        header, header_text = match[0].strip(), match[1].strip()
        extracted_text[header] = header_text

    # Combine all extracted text into a single string for matched headers
    matched_headers_text = ' '.join([f"{header}: {text}" for header, text in extracted_text.items()])

    # Unmatched text is what's left after removing matched text
    unmatched_text = pattern.sub('', text).strip()

    return matched_headers_text, unmatched_text

# Load the dataset with text and headers
df = pd.read_csv("01_intermediate-files/parsed_rows_with_headers_all.csv")

# Load the headers count dataset
headers_count_df = pd.read_csv("01_intermediate-files/headers_count.csv")

# Filter headers with a count greater than 1
headers_of_interest = headers_count_df[headers_count_df['Count'] > 1]['Header'].str.lower().tolist()

# Additionally, include headers that contain 'smok' or 'tobacco'
additional_headers = headers_count_df[headers_count_df['Header'].str.contains(r'smok|tobacco', case=False, regex=True)]['Header'].str.lower().unique().tolist()
headers_of_interest.extend(header for header in additional_headers if header not in headers_of_interest)

# Apply the text extraction function to each row in the DataFrame
df[['Matched Headers Text', 'Unmatched Text']] = df.apply(
    lambda row: extract_text_by_headers(row['Text'], headers_of_interest), axis=1, result_type='expand')

# Save the new DataFrame to a CSV file
df.to_csv("01_intermediate-files/extracted_text_with_separate_columns.csv", index=False)