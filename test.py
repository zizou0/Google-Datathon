import pandas as pd



# Read the CSV file
def create_county_mappings(df):
    # Option 1: Dictionary using FIPS as key
    county_dict = dict(zip(df['FIPS'], df['Classification']))
    
    # Option 2: DataFrame indexing using FIPS
    df.set_index('FIPS', inplace=True)
    
    return county_dict, df

def get_classification(county_id, county_dict):
    # Safely get classification with error handling
    return county_dict.get(county_id, "Not Found")

def main():
    # Read data
    pd.set_option('display.max_rows', None)  # Show all rows
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.width', None)  # Prevent wrapping
    df = pd.read_csv('counties.csv', dtype={'FIPS': str})
    
    # Create classifications first
    df['Classification'] = df['RUCC_2023'].apply(lambda x: 'Urban' if x <= 3 else 'Rural')
    df['FIPS'] = 'geoId/' + df['FIPS'].str.zfill(5)
    print(df)
    return
    # Create both mapping options
    county_dict, indexed_df = create_county_mappings(df.copy())
    
    # Example usage
    test_fips = '01001'  # Autauga County
    # Dictionary lookup
    print(f"Dictionary lookup: {test_fips} is {county_dict[test_fips]}")
    # DataFrame lookup
    print(f"DataFrame lookup: {test_fips} is {indexed_df.loc[test_fips, 'Classification']}")

if __name__ == "__main__":
    main()