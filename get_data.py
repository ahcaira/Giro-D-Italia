import pandas as pd


# Function to find the correct table by looking for "Stage" in the columns
def find_leadership_table(tables):
    for table in tables:
        # Check if the table has columns related to "Stage" or "General Classification"
        if any(col in table.columns for col in ["General classification", 'Team classification']):
            return table
    return None  # If not found


# URL of the Wikipedia page
for i in range(1920, 2025):
    url = f"https://en.wikipedia.org/wiki/{i}_Giro_d%27Italia"

    try:
        tables = pd.read_html(url)
        leadership_table = find_leadership_table(tables)

        # if i == 1950:
        #     for table in tables:
        #         print(table)

        if leadership_table is not None:
            print(leadership_table.head())
            leadership_table.to_csv(f"data/{i}.csv", index=False)
        else:
            print(f'Year {i}: Leadership table not found!')

    except Exception as e:
        print(f'Year {i} is missing! Error: {e}')