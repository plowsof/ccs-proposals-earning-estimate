import frontmatter
import pprint
import os
import csv
import re
from datetime import datetime

# Function to read the price data from a CSV file and return a list of dictionaries
def read_price_data(csv_file):
    price_data = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert the 'snapped_at' to a datetime object for easier comparison
            row['snapped_at'] = datetime.strptime(row['snapped_at'], "%Y-%m-%d %H:%M:%S %Z")
            # Convert price, market_cap, and total_volume to float if they are not empty
            row['price'] = float(row['price']) if row['price'] else None
            row['market_cap'] = float(row['market_cap']) if row['market_cap'] else None
            row['total_volume'] = float(row['total_volume']) if row['total_volume'] else None
            price_data.append(row)
    return price_data

# Function to find the closest price data entry for a given date
def get_closest_price_data(price_data, target_date):
    closest = min(price_data, key=lambda x: abs(x['snapped_at'] - target_date))
    return closest

def parse_amount(amount_str):
    # Patterns to match different formats of the 'funds:' field
    patterns = [
        r'(\d+(\.\d+)?) XMR',                       # Pattern for "23 XMR"
        r'(\d+(\.\d+)?) Monero',                    # Pattern for "62.5 Monero"
        r'(\d+(\.\d+)?)% \((\d+(\.\d+)?) XMR\)',    # Pattern for "33% (62.5 XMR)"
        r'(\d+(\.\d+)?)% \((\d+(\.\d+)?) Monero\)', # Pattern for "33% (62.5 Monero)"
        r'(\d+(\.\d+)?)% \(XMR (\d+(\.\d+)?)\)',    # Pattern for "16.66% (XMR 6.3)"
        r'(\d+(\.\d+)?)% \(~XMR (\d+(\.\d+)?)\)',   # Pattern for "10% (~XMR 10.70)"
        r'All remaining \((\d+(\.\d+)?) XMR\)',     # Pattern for "All remaining (40.4 XMR)"
        r'^(\d+(\.\d+)?)$',                         # Pattern for "12.5"
        r'(\d+(\.\d+)?)( XMR)?',                    # Pattern for "33% (51)"
        r'(\d+(\.\d+)?)% \(XMR (\d+(\.\d+)?)\)',    # Pattern for "16.66% (XMR 6.3)"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, amount_str)
        if match:
            if match.group(1):
                return float(match.group(1))
            elif match.group(3):
                return float(match.group(3))
    
    # If no pattern matches, assume it's a Monero amount without any unit
    try:
        return float(amount_str)
    except ValueError:
        return 0.0

# Function to check if a date string is valid
def is_valid_date(date_str, date_format):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False

# Function to parse date with multiple possible formats
def parse_date(date_str):
    corrected_date_str = date_str.replace("Februrary", "February").replace("Janauary", "January")
    date_formats = [
        "%d %B %Y",      # e.g. "14 September 2022"
        "%B %d, %Y",     # e.g. "June 18, 2019"
        "%d/%m/%Y",      # e.g. "31/01/2019"
        "%d/%m/%y",      # e.g. "31/3/19"
        "%m/%d/%y",      # e.g. "6/12/19"
        "%m/%d/%Y",      # e.g. "06/12/2019"
        "%d %b %Y",      # e.g. "5 Jan 2022"
    ]
    for fmt in date_formats:
        try:
            if is_valid_date(corrected_date_str, fmt):
                return datetime.strptime(corrected_date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Date format for '{date_str}' is not recognized.")

# Function to collect completed milestones with associated price data
def collect_completed_milestones(directory=".", price_csv="price_data.csv"):
    price_data = read_price_data(price_csv)
    data_list = []
    author_yearly_summary = {}
    authors_with_zero_monero = set()
    funds_formats = set()

    for file in os.listdir(directory):
        if file.endswith(".md"):
            file_path = os.path.join(directory, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)

                author = str(post.get("author"))
                if not author:
                    raise ValueError("Invalid or missing author field")

                if author not in author_yearly_summary:
                    author_yearly_summary[author] = {}

                for x in post.get("payouts", []):
                    if x.get("date"):
                        if x.get("date") == 47:
                            tmp = x["amount"]
                            x["amount"] = x["date"]
                            x["date"] = tmp
                        funds_str = str(x.get("amount"))
                        print(funds_str)
                        if not funds_str:
                            raise ValueError("Invalid or missing funds field")

                        funds_formats.add(funds_str)

                        # Convert the 'done' date to a datetime object using multiple formats
                        try:
                            done_date = parse_date(str(x.get("date")))
                        except ValueError as e:
                            print(f"Error processing date in file {file}: {e}")
                            continue

                        closest_price_data = get_closest_price_data(price_data, done_date)
                        monero_amount = parse_amount(funds_str)
                        amount_in_usd = monero_amount * closest_price_data["price"]
                        year = done_date.year

                        # Append the data to the data list
                        data = {
                            "title": post.get("title"),
                            "payout_sent": x.get("date"),
                            "author": author,
                            "monero_amount": monero_amount,
                            "price_on_done_date": closest_price_data["price"],
                            "amount_in_usd": amount_in_usd
                        }
                        data_list.append(data)

                        # Aggregate data by year for the specific author
                        if year not in author_yearly_summary[author]:
                            author_yearly_summary[author][year] = {"total_monero": 0.0, "total_usd": 0.0}
                        author_yearly_summary[author][year]["total_monero"] += monero_amount
                        author_yearly_summary[author][year]["total_usd"] += amount_in_usd

                        # Check if the monero_amount is 0.0 and add the author to the set
                        if monero_amount == 0.0:
                            authors_with_zero_monero.add(author)

            except Exception as e:
                print(f"Error processing file {file}: {e}")

    pprint.pprint(data_list)
    print("\nAuthor Yearly Summary:")
    for author, yearly_summary in author_yearly_summary.items():
        print(f"\nAuthor: {author}")
        for year in sorted(yearly_summary.keys()):
            summary = yearly_summary[year]
            print(f"  {year}: {summary['total_monero']} Monero, ${summary['total_usd']:.2f} USD")

    print("\nUnique 'funds:' formats found:")
    pprint.pprint(funds_formats)

    print("\nAuthors with monero_amount 0.0:")
    pprint.pprint(authors_with_zero_monero)

# Call the function with the desired directory and CSV file
collect_completed_milestones(directory=".", price_csv="price_data.csv")
