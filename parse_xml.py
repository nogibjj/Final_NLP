import pandas as pd
import xml.etree.ElementTree as ET
import os

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []

    # Iterate through each record in the XML
    for i, element in enumerate(root):
        if i >= 5:  # Only process the first 5 records
            break
        record_data = {}
        record_data['Record ID'] = element.attrib['ID']  # Get the ID attribute
        # Get the SMOKING status attribute
        smoking_status = element.find('SMOKING').attrib['STATUS']
        record_data['Smoking Status'] = smoking_status if smoking_status else None
        # Get the text content of the TEXT tag
        text_content = element.find('TEXT').text
        record_data['Text'] = text_content.strip() if text_content else None
        data.append(record_data)

    return pd.DataFrame(data)

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the file path
file_path = os.path.join(script_dir, '00_src/smokers_surrogate_train_all_version2.xml')

df = parse_xml(file_path)
print(df)

# Specify the output CSV file path
output_csv_path = '/Users/robintitus/Desktop/nlp_final/NLP_Medical-SmokerCategorization/01_intermediate-src/df_parsed_5rows.csv'

# Save the DataFrame to a CSV file
df.to_csv(output_csv_path, index=False)
