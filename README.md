# Data Analysis: Glucose, Insulin, and BMI as predictor variables on the outcome variable (whether a patient is Diabetic or not)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/simrunsharma/bb556644aa675c59b2b208a5782f1802/diabetes.ipynb#scrollTo=bAN4CmBeC9Sm)

[![Install](https://github.com/nogibjj/mini_10_simrun/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/mini_10_simrun/actions/workflows/install.yml)[![Lint](https://github.com/nogibjj/mini_10_simrun/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/mini_10_simrun/actions/workflows/lint.yml)
[![Format](https://github.com/nogibjj/mini_10_simrun/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/mini_10_simrun/actions/workflows/format.yml)
[![Test](https://github.com/nogibjj/mini_10_simrun/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/mini_10_simrun/actions/workflows/test.yml)



## Data Source
This dataset contains information about female patients that are at least 21 years old and are of Pima Indian Heritage. From each patient the dataset gleans diagnostic measurements of BMI, Insulin, Pregnancies, Blood Pressure, Skin Thickness, Glucose, etc. This data was collected from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective is to determine if the patient has diabetes or not. The outcome variable tells with a (1-Diabetic) v. (0-Not Diabetic). I specifcally wanted to analyze Insulin, Glucose, and BMI as my predictor variables. I conduct a descriptive analysis/statistics of this dataset to deeper understand these variables relationship with Diabetes.
You can access the data from the following URL: [Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database?select=diabetes.csv).

## Code Overview

# PySpark Data Analysis Example

**Description:**

This code snippet demonstrates how to use PySpark to perform data analysis on a dataset stored in a CSV file named "diabetes.csv." The code covers various data manipulation and analysis operations, including loading data, data type conversion, and aggregation. It uses the PySpark library to work with big data in a distributed computing environment.

**Installation:**

Before running the code, make sure you have PySpark installed. You can use pip to install it:

```sh
!pip install pyspark
```
**Usage:**

1. Import the required libraries:

   ```python
   import pyspark
   import pandas as pd
   from pyspark.sql import SparkSession
   from pyspark.sql.types import IntegerType
   
2. Load the CSV data into a Spark DataFrame and display it:
```sh
spark = SparkSession.builder.appName("Practice").getOrCreate()
df = spark.read.option('header','true').csv('diabetes.csv')
df.show()
```
3.Perform data type conversion for specific columns:
```sh
df = df.withColumn("Glucose", df["Glucose"].cast(IntegerType()))
# Repeat for other columns as needed
```
4. Conduct various data analysis operations, such as grouping and aggregation:
```sh
df.groupBy("Age").sum("Glucose").show()
# Repeat for other analysis operations
```
5. To find counts and aggregate statistics:
```sh
df.groupBy("Outcome").count().show()
df.agg({"Glucose": "sum", "BMI": "sum", "Outcome": "sum", "BloodPressure": "sum", "SkinThickness": "sum"}).show()
```




### MakeFile and Workflows
I created four different workflows to show each step of my Makefile.

Install: runs the packages indicated in my requirements.txt

Lint: 
```sh
nbqa ruff src/*.ipynb
```
Format: 
```sh
nbqa black src/*.ipynb
```  
Test: 
```sh
python -m pytest --nbval src/*.ipynb
```

<img width="496" alt="image" src="https://github.com/nogibjj/mini_10_simrun/assets/141798228/0c1970b0-9011-4473-98d0-0bbe09cd5bdf">


## Results

<img width="607" alt="image" src="https://github.com/nogibjj/mini_10_simrun/assets/141798228/fcf10bc2-de15-4ea1-ace5-db427f473393">

**Aggregation and Grouping:**

In the provided code, you'll notice the use of two important PySpark functions—`agg` and `groupBy`. These functions play a crucial role in data analysis and aggregation operations.

1. **`groupBy` Function:**

   The `groupBy` function is used to group data in the DataFrame based on one or more columns. In the code, you can see examples like:
```sh
df.groupBy("Age").sum("Glucose").show()
```
<img width="300" alt="image" src="https://github.com/nogibjj/mini_10_simrun/assets/141798228/4d9df804-f200-41d5-b7a5-479b5d5a8fab">

2. agg Function:

The agg (short for "aggregate") function is used to perform aggregate operations on one or more columns of a DataFrame. In the code, you can see an example like:
```sh
df.agg({"Glucose": "sum", "BMI": "sum", "Outcome": "sum", "BloodPressure": "sum", "SkinThickness": "sum"}).show()
```
<img width="501" alt="image" src="https://github.com/nogibjj/mini_10_simrun/assets/141798228/0c371093-4655-4b32-a3ee-b218477c424b">

## Conclusion
This script serves as a valuable tool for investigating the interplay between crucial predictor variables—Glucose, Insulin, and BMI—and the diabetes status indicator within the context of the Pima Indian female patient dataset. By offering essential descriptive statistics and intuitive visualizations like count plots and bar plots, it allows for a deeper understanding of how these variables are linked to the likelihood of diabetes. These insights provide a solid foundation for conducting more advanced analyses and informed decision-making in the domain of diabetes research and prediction
