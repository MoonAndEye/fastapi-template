import json


def convert_sp500():
    companies = []

    with open("data/sp500.txt", "r") as file:
        # Skip header
        next(file)

        for line in file:
            # Split by tab character since data is tab-delimited
            parts = line.strip().split("\t")

            # Ensure we have all columns
            if len(parts) >= 8:
                symbol = parts[0]
                security = parts[1]
                sector = parts[2]
                sub_industry = parts[3]
                headquarters = parts[4]
                date_added = parts[5]
                cik = parts[6]
                founded = parts[7]

            # Clean up founded year if it contains parentheses
            if "(" in founded:
                founded = founded.split("(")[1].replace(")", "")

            company = {
                "symbol": symbol,
                "security": security,
                "sector": sector,
                "subIndustry": sub_industry,
                "headquarters": headquarters,
                "dateAdded": date_added,
                "cik": cik,
                "founded": founded,
            }
            companies.append(company)

    # Write the JSON file
    with open("data/sp500.json", "w") as f:
        json.dump(companies, f, indent=4)


if __name__ == "__main__":
    convert_sp500()
