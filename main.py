import csv

def read_csv(file_path):
    # Read CSV file and return the header and data
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)
    return header, data

def process_data(header, data):
    # Process the data and return a list with additional information
    processed_data = [['State-Place', 'Year', 'Population', 'Peddisetty-Rank']]
    
    for row in data:
        state_place = f'{row[1]} - {row[0]}'
        year = int(row[2])
        population = int(row[3]) if row[3] else 0
        processed_data.append([state_place, year, population, 0])

    return processed_data

def calculate_rank(processed_data):
    # Sort the data based on year and population, and calculate the rank
    processed_data[1:] = sorted(processed_data[1:], key=lambda x: (x[1], x[2]), reverse=True)

    current_year = None
    rank = 0

    for row in processed_data[1:]:
        if row[1] != current_year:
            rank = 1
            current_year = row[1]
        else:
            rank += 1
        row[3] = rank

    return processed_data

def write_to_csv(data, output_file):
    # Write the processed data to a new CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def main():
    input_file = "C:\\Users\\tharunpeddisetty\\Largest_Cities_CSV(1).csv"
    output_file = "C:\\Users\\tharunpeddisetty\\Tharun_Peddisetty_Final_List.csv"

    header, data = read_csv(input_file)
    processed_data = process_data(header, data)
    final_data = calculate_rank(processed_data)
    write_to_csv(final_data, output_file)

if __name__ == "__main__":
    main()
