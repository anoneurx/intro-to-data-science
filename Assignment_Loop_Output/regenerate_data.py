import os
import csv

def main():
    # 1. Find out where our current code lives on the computer
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. We make a folder named "main" to save our final result
    main_output_folder = os.path.join(base_dir, "main")
    os.makedirs(main_output_folder, exist_ok=True)
    
    # 3. We use a dictionary to save our data. 
    # A dictionary is like a real-life dictionary: it has a 'key' and a 'value'.
    # Because a dictionary can't have duplicate keys, this easily removes duplicates!
    extracted_data = {}  
    
    # 4. We know there are 10 folders (part_1 to part_10). Let's loop from 1 up to 10 (inclusive).
    for i in range(1, 11):
        # Create the folder name, e.g., "part_1", "part_2"
        folder_name = os.path.join(base_dir, f"part_{i}")
        
        # If the folder does not exist, just skip it and go to the next one
        if not os.path.exists(folder_name):
            continue
            
        # 5. Look at everything inside this folder
        files_in_folder = os.listdir(folder_name)
        
        for file in files_in_folder:
            # We only care about CSV files
            if file.endswith(".csv"):
                # Get the full path to this file
                file_path = os.path.join(folder_name, file)
                
                # 6. Open the CSV file to read it
                with open(file_path, "r") as f:
                    reader = csv.reader(f)
                    
                    # Skip the first row because it contains headers ("X", "X_squared")
                    header = next(reader, None) 
                    
                    # 7. Read line by line
                    for row in reader:
                        # Make sure the row has exactly 2 columns of data before trying to read it
                        if len(row) == 2:
                            try:
                                # First column is our X value, Second is our X squared value
                                x_val = int(row[0])
                                x_sq = int(row[1])
                                
                                # 8. Save it into our dictionary
                                # If we already have this x_val, it just overwrites it safely (no duplicates)
                                extracted_data[x_val] = x_sq
                            except ValueError:
                                # If there is an error converting the value to a number, just ignore it
                                continue

    # 9. Now we sort all the keys (the X values) from smallest to largest
    sorted_x = sorted(extracted_data.keys())
    
    # 10. Create the final "complete_data.csv" file to save our work
    complete_csv_path = os.path.join(main_output_folder, "complete_data.csv")
    
    with open(complete_csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        
        # Write the top header row
        writer.writerow(["X", "X_squared"])
        
        # Write each piece of data, one by one
        for x in sorted_x:
            writer.writerow([x, extracted_data[x]])

    # 11. Print a success message!
    print("Data successfully regenerated!")
    print(f"We extracted {len(sorted_x)} unique rows.")
    print(f"Output saved to: {complete_csv_path}")

if __name__ == "__main__":
    main()
