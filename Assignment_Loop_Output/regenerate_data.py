import os
import csv

def regenerate_data():
    all_data = {}  # Dictionary to store unique X and X_squared values
    
    # 1. Loop through folders part_1 to part_10
    for i in range(1, 11):
        folder = f"part_{i}"
        if os.path.exists(folder):
            # 2. Look at every file in the folder
            for filename in os.listdir(folder):
                if filename.endswith(".csv"):
                    path = os.path.join(folder, filename)
                    
                    # 3. Read the CSV and skip the header row
                    with open(path, "r") as f:
                        reader = csv.reader(f)
                        next(reader, None) # Skip "X, X_squared" header
                        
                        for row in reader:
                            if len(row) == 2:
                                # Save into dictionary to auto-remove duplicates
                                x, x_sq = int(row[0]), int(row[1])
                                all_data[x] = x_sq

    # 4. Create 'main' folder and save the final combined CSV
    os.makedirs("main", exist_ok=True)
    output_path = "main/complete_data.csv"
    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["X", "X_squared"])
        
        # Sort X values from 1 to 100 before writing
        for x in sorted(all_data.keys()):
            writer.writerow([x, all_data[x]])

    print(f"Success! Combined {len(all_data)} unique rows into {output_path}")

if __name__ == "__main__":
    regenerate_data()
