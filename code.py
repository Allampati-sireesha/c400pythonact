import requests
import csv

def download_csv(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Successfully downloaded {filename}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def count_rows_in_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        total_rows = sum(1 for row in reader) - 1  # Subtract 1 for the header
    return total_rows

def find_unique_boroughs(filename):
    boroughs = set()
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            boroughs.add(row[1])  # Assuming 'Borough' is in the second column (index 1)
    return sorted(boroughs)

def count_records_for_borough(filename, borough_name):
    count = 0
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] == borough_name:
                count += 1
    return count

def save_facts(a, b, c, output_file):
    with open(output_file, 'w') as file:
        file.write(f"Fact A: {a}\n")
        file.write(f"Fact B: {b}\n")
        file.write(f"Fact C: {c}\n")
    print(f"Facts saved to {output_file}")

# Example usage
if __name__ == "__main__":
    csv_url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"  # Replace with your CSV link
    csv_file = "locations.csv"

    # Download the CSV file
    download_csv(csv_url, csv_file)

    # Count the rows in the downloaded CSV file
    total_rows = count_rows_in_csv(csv_file)
    print(f"Total number of rows: {total_rows}")

    # Find unique boroughs in ascending order
    unique_boroughs = find_unique_boroughs(csv_file)
    print("Unique Boroughs in Ascending Order:")
    for borough in unique_boroughs:
        print(borough)

    # Count records for Brooklyn borough
    brooklyn_count = count_records_for_borough(csv_file, "Brooklyn")
    print(f"Number of records for Brooklyn: {brooklyn_count}")

    # Define facts (you can change these values as needed)
    a = total_rows
    b = len(unique_boroughs)
    c = brooklyn_count

    # Save facts to the specified file
    output_file = "/root/taxi_zone_output.txt"
    save_facts(a, b, c, output_file)
