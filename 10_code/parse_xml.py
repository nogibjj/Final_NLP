import pandas as pd
import xml.etree.ElementTree as ET
import os

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []

    # Iterate through each record in the XML
    for element in root:
        record_data = {}
        record_data['Record ID'] = element.attrib['ID']  # Get the ID attribute
        # Get the SMOKING status attribute
        smoking_status = element.find('SMOKING').attrib['STATUS']
        record_data['Smoking Status'] = smoking_status if smoking_status else None
        # Get the text content of the TEXT tag
        text_content = element.find('TEXT').text
        record_data['Text'] = text_content.strip() if text_content else None
        data.append(record_data)

    df = pd.DataFrame(data)
    return df

xml = '00_src/smokers_surrogate_test_all_groundtruth_version2.xml'
#df = parse_xml(xml)

# Extracting head, tail, and a sample
#head = df.head(5)
#tail = df.tail(5)
#sample = df.sample(5)

# Saving to CSV
#df.to_csv("01_intermediate-files/parsed_groundtruth_raw.csv", index=False)
#head.to_csv("01_intermediate-files/parsed_rows_head.csv", index=False)
#tail.to_csv("01_intermediate-files/parsed_rows_tail.csv", index=False)
#sample.to_csv("01_intermediate-files/parsed_rows_sample.csv", index=False)

##Number of rows in XML file: 398

##### TESTING PARSER 
# def count_smoking_status(xml_file_path, status_to_check):
#     tree = ET.parse(xml_file_path)
#     root = tree.getroot()
#     count = 0

#     for record in root.findall('.//RECORD'):
#         smoking_status = record.find('SMOKING').get('STATUS')
#         if smoking_status == status_to_check:
#             count += 1

#     return count

# counter = count_smoking_status(xml, "CURRENT SMOKER")
# print(counter)

##### CLUB SMOKER WITH PAST SMOKER
file_path = '01_intermediate-files/raw_parsed_xml.csv'
df = pd.read_csv(file_path)

# Step 2: Update 'smoker' values to 'past smoker' in the 'Smoking Status' column
df['Smoking Status'] = df['Smoking Status'].replace('SMOKER', 'PAST SMOKER')

# Step 3: Save the modified DataFrame back to a CSV file
df.to_csv('01_intermediate-files/raw_train_xml.csv', index=False)