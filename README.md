# Data Transformation Project

This project fetches and cleans stock data from the Financial Modeling Prep API, transforming it for reporting purposes.

## Features

- Fetches data via API and loads into a pandas DataFrame.
- Transforms data: standardizes column names, handles missing values, encodes categorical data, and creates derived columns.
- Performs sorting, grouping, aggregation, and normalization.
- Saves the cleaned data to `cleaned_data.csv`.