import pandas as pd

df = pd.read_csv("Dolche Vita Reviews.csv")

print(df.head())




#Replacing value like" 5 contributions" , "1 contribution", "19 contributions" etc,  with "Unknown" in location column
df['Location'] = df['Location'].fillna("Unknown").replace(regex=r'\d+ contributions?', value="Unknown")

df.to_csv('Dolche Vita Reviews.csv', index=False)

print(df['Location'].head())





# Convert the Date column to string and remove "Written " and bring in proper date format
df['Date'] = df['Date'].astype(str).str.replace("Written ", "", regex=False)


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')


if df['Date'].isnull().any():
    print("There are some dates that could not be converted:")
    print(df[df['Date'].isnull()])

df.to_csv('Dolche Vita Reviews.csv', index=False)
print(df['Date'].head())


# Extracting the numeric rating from the 'Rating' column and convert it to a numeric type coulmn
df['Rating'] = df['Rating'].str.extract(r'(\d+\.?\d*)').astype(float)

df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

df.to_csv('Dolche Vita Reviews.csv', index=False)

print(df['Rating'].head())


# Updated rating columns list with exact column names
rating_columns = ['Value Rating', 'Food Rating ', 'Service  Rating ', 'Atmosphere  Rating ']

# Clean and fill missing values in these columns
for col in rating_columns:
    # Remove text and convert to float
    df[col] = df[col].str.replace(" of 5 bubbles", "").astype(float)

# Fill missing values with the mean of each column
df[rating_columns] = df[rating_columns].apply(lambda x: x.fillna(x.mean()))

# Columns we want to modify
rating_columns = ['Value Rating', 'Food Rating ', 'Service  Rating ', 'Atmosphere  Rating ']

# Remove the decimal part by converting each value to integer
for col in rating_columns:
    df[col] = df[col].astype(float).astype(int)

# Display the first few rows to confirm the changes
df.head()

# Save the cleaned DataFrame to a new CSV 
df.to_csv('Cleaned_Dolche_Vita_Reviews.csv', index=False)







