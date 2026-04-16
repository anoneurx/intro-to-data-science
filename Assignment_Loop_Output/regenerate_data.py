import os
import csv

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    main_output_folder = os.path.join(base_dir, "main")
    os.makedirs(main_output_folder, exist_ok=True)
    
    extracted_data = {}  # Dictionary naturally handles discarding duplicates
    
    # Iterate through all 10 partition folders
    for i in range(1, 11):
        folder_name = os.path.join(base_dir, f"part_{i}")
        if not os.path.exists(folder_name):
            continue
            
        # Check all CSV files in the folder
        for file in os.listdir(folder_name):
            if file.endswith(".csv"):
                file_path = os.path.join(folder_name, file)
                
                with open(file_path, "r") as f:
                    reader = csv.reader(f)
                    header = next(reader, None) # Skip header
                    
                    for row in reader:
                        if len(row) == 2:
                            try:
                                x_val = int(row[0])
                                x_sq = int(row[1])
                                # Inserting into dictionary prevents duplicate entries
                                extracted_data[x_val] = x_sq
                            except ValueError:
                                continue

    # Sort data by the value of X
    sorted_x = sorted(extracted_data.keys())
    
    complete_csv_path = os.path.join(main_output_folder, "complete_data.csv")
    with open(complete_csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["X", "X_squared"])
        for x in sorted_x:
            writer.writerow([x, extracted_data[x]])

    print(f"Data successfully regenerated. Extracted {len(sorted_x)} unique rows.")
    print(f"Output saved to: {complete_csv_path}")

if __name__ == "__main__":
    main()
