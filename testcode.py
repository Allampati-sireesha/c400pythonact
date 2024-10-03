import requests
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)
file = open('taxi_zone_lookup.csv', 'wb')
file.write(response.content)
file.close()
file = open('taxi_zone_lookup.csv', 'r')
lines = file.readlines()
file.close()
header = lines[0].strip().split(",")
records = [line.strip().split(",") for line in lines[1:]]
total_records = len(records)
borough = set(i[1] for i in records)
unique = sorted(borough)
brooklyn_count = sum(1 if i[1] == '"Brooklyn"' else 0 for i in records)
output_records = [f"Total Records: {total_records}", f"Unique Boroughs: {', '.join(unique)}", f"Brooklyn Records: {brooklyn_count}"]
print(output_records)
output_file_path = '/root/taxi_zone_output.txt'
file_result = open(output_file_path, 'w')
for i in output_records:
    file_result.write(i + '\n')
file_result.close()
print("Saved to /root/taxi_zone_output.txt")
