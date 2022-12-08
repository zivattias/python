import csv
from datetime import datetime

path = 'AAPL.csv'

# New file fieldnames: Year,  Avg Price, Min Price, Max Price, Avg Volume, Min Volume, Max Volume

def create_new_csv(new_file_name: str):

    # Variables initialization:
    avg_price, min_price, max_price = 0.0, float('inf'), float('-inf')
    avg_volume, min_volume, max_volume = 0.0, float('inf'), float('-inf')
    total_volume: int = 0
    total_price: float = 0
    previous_year: int = 0
    line_counter: int = 0

    # New file fieldnames:
    fieldnames = ["Year",  "Avg Price", "Min Price", "Max Price", "Avg Volume", "Min Volume", "Max Volume"]

    # Write 1st line of fieldnames to new file:
    with open(new_file_name, 'w') as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader()

    # Retrieve data from source file:
    with open(path, 'r') as source_file:
        csv_reader = csv.DictReader(source_file)

        for line in csv_reader:
            # Format 'Date' to datetime & retrieve year
            date = datetime.strptime(line['Date'], "%d-%m-%Y").date()
            current_year = date.year

            # If year is incremented:
            if 0 != previous_year != current_year:
                with open(new_file_name, 'a') as new_file:
                    # Before turning to next year, create a dict of current year's finalized data:
                    row_dict: dict[str, int | float] = {
                        fieldnames[0]: previous_year,
                        fieldnames[1]: total_price / line_counter,
                        fieldnames[2]: min_price,
                        fieldnames[3]: max_price,
                        fieldnames[4]: total_volume / line_counter,
                        fieldnames[5]: min_volume,
                        fieldnames[6]: max_volume
                    }
                    # Add current year's data to new file:
                    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                    csv_writer.writerow(row_dict)

                # Reset variables to be ready for next year data:
                avg_price, min_price, max_price = 0.0, float('inf'), float('-inf')
                avg_volume, min_volume, max_volume = 0.0, float('inf'), float('-inf')
                total_volume: float = 0
                total_price: float = 0
                previous_year: int = 0
                line_counter: int = 0

            # Evaluate year-related data:
            min_price = min(min_price, float(line['Low']))
            max_price = max(max_price, float(line['High']))
            min_volume = min(min_volume, int(line['Volume']))
            max_volume = max(max_volume, int(line['Volume']))
            total_volume += int(line['Volume'])
            total_price += float(line['Adjusted Close'])
            line_counter += 1
            previous_year = current_year

        # Handle the last year:
        with open(new_file_name, 'a') as new_file:
            # Before turning to next year, create a dict of current year's finalized data:
            row_dict: dict[str, int | float] = {
                fieldnames[0]: previous_year,
                fieldnames[1]: total_price / line_counter,
                fieldnames[2]: min_price,
                fieldnames[3]: max_price,
                fieldnames[4]: total_volume / line_counter,
                fieldnames[5]: min_volume,
                fieldnames[6]: max_volume
            }
            # Add current year's data to new file:
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writerow(row_dict)

if __name__ == '__main__':
    create_new_csv('new_AAPL.csv')





