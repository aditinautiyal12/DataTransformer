import requests
import pandas as pd

def fetch_weather_data():

    url = f"https://financialmodelingprep.com/api/v3/stock/list?apikey=sAwXE7JiCPGDKvTnwZ7j6eqqeuHfAs6R"
    
    
    # HTTP GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        #print("Raw response:", data)
        
        # Convert the response to a DataFrame (adjust based on the structure)
        df = pd.json_normalize(data)
        
        # print("here is my df")
        # print(df.head(10))
        return df
    
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        print(response.text)


def transform_df(df):
    # Standardize Column Names
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    print("After standardizing column names:")
    print(df)
    print()

    # Convert Data Types
    df['price'] = df['price'].astype(float)
    print("After converting 'price' to float:")
    print(df)
    print()

    # Handle Missing Data
    df.fillna({'price': 0}, inplace=True)
    print("After handling missing data:")
    print(df)
    print()

    # Categorical Encoding
    df['exchange'] = df['exchange'].astype('category').cat.codes
    df['type'] = df['type'].astype('category').cat.codes
    print("After categorical encoding:")
    print(df)
    print()

    # Create Derived Columns
    df['high_price'] = df['price'] > 50
    print("After creating derived columns:")
    print(df)
    print()

    # Sort Data
    df_sorted = df.sort_values(by='price', ascending=False)
    print("After sorting by 'price':")
    print(df_sorted)
    print()

    # Group and Aggregate
    df_grouped = df.groupby('exchange').agg({'price': 'mean'})
    print("After grouping and aggregating by 'exchange':")
    print(df_grouped)
    print()

    # Format Data for Reporting
    df['price'] = df['price'].round(2)
    print("After rounding 'price' to two decimal places:")
    print(df)
    print()

    # Remove Duplicates
    df.drop_duplicates(inplace=True)
    print("After removing duplicates:")
    print(df)
    print()

    # Descriptive Statistics
    print("Descriptive statistics:")
    print(df.describe())
    print()

    # Data Normalization
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df[['price']] = scaler.fit_transform(df[['price']])
    print("After normalizing 'price':")
    print(df)
    print()

    return df


def main():
    
    # Call the function to fetch weather data
    df = fetch_weather_data()
    print("Raw DataFrame\n")
    print(df.head(10))
    transformed_df = transform_df(df)
    print("Transformed DataFrame\n")
    print(transformed_df.head(10))
    df.to_csv('cleaned_data.csv', index=False)

if __name__ == "__main__":
    main()
