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

xml = '00_src/smokers_surrogate_train_all_version2.xml'
df = parse_xml(xml)

# Extracting head, tail, and a sample
head = df.head(5)
tail = df.tail(5)
sample = df.sample(5)

# Saving to CSV
df.to_csv("01_intermediate-files/parsed_rows_raw.csv", index=False)
head.to_csv("01_intermediate-files/parsed_rows_head.csv", index=False)
tail.to_csv("01_intermediate-files/parsed_rows_tail.csv", index=False)
sample.to_csv("01_intermediate-files/parsed_rows_sample.csv", index=False)

##Number of rows in XML file: 398
