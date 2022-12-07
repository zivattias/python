relative_path = 'data/AAPL.csv'

price_sum = 0
price_count = 0

with open(relative_path, 'r') as fh:
    # Skip 1st line:
    fh.readline()   # No given attr or '1' = 1
    for line in fh:
        open_price: float = float(line.split(',')[2])
        price_count += 1
        price_sum += open_price

print(price_sum / price_count)


