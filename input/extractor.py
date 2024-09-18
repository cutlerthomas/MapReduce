import csv

# Specify the input CSV file and the output TXT file
csv_file = 'cars.csv'
txt_file = 'car_prices.txt'

# Open the CSV file and read the "Price ($)" column
with open(csv_file, mode='r') as infile:
    reader = csv.DictReader(infile)
    
    # Open the TXT file to write the "Price ($)" values
    with open(txt_file, mode='w') as outfile:
        # Loop through each row and write the "Price ($)" column to the TXT file
        for row in reader:
            price = row["Price ($)"]
            outfile.write(f"{price}\n")

print(f"Prices have been successfully written to {txt_file}")
