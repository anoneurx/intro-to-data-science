import os
import shutil
import csv

def main():
    # 1. Find out where our current code lives on the computer
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(base_dir, exist_ok=True)
    
    # 2. Create a simple list of numbers from 1 to 100
    values = []
    for number in range(1, 101):
        values.append(number)
    
    # 3. Split the 100 numbers into 10 smaller parts (each containing exactly 10 numbers)
    parts = []
    for i in range(0, 100, 10):
        # Take a piece (slice) of 10 items from the main list
        small_part = values[i:i + 10]
        parts.append(small_part)
    
    # 4. Find the 2 study files we want to copy into the folders
    # 'parent_dir' is the main project folder "intro-to-data-science"
    parent_dir = os.path.dirname(base_dir)
    file_1 = os.path.join(parent_dir, "Study_Materials/Python_AdvancedLoops_Patterns.ipynb")
    file_2 = os.path.join(parent_dir, "Study_Materials/Python_Basics_DataTypes_Variables.ipynb")
    source_files = [file_1, file_2]
    
    # 5. Loop 10 times to build our 10 folders (part_1 up to part_10)
    for idx in range(10):
        # idx starts at 0 and goes to 9. We add 1 so our folders start at "part_1".
        folder_number = idx + 1
        folder_name = os.path.join(base_dir, f"part_{folder_number}")
        
        # Create the subfolder using os.makedirs
        os.makedirs(folder_name, exist_ok=True)
        
        # 6. We want 3 CSV files in each folder.
        # We use the remainder operator (%) so we repeat our 10 parts if we go out of bounds
        chunk_1 = parts[(idx) % 10]
        chunk_2 = parts[(idx + 1) % 10]
        chunk_3 = parts[(idx + 2) % 10]
        
        # Put these lists in a dictionary tied to their future file names
        sub_files_content = {
            "file_chunk_1.csv": chunk_1,
            "file_chunk_2.csv": chunk_2,
            "file_chunk_3.csv": chunk_3
        }
        
        # 7. Create these 3 CSV files one by one inside the newly created folder
        for file_name, content_list in sub_files_content.items():
            file_path = os.path.join(folder_name, file_name)
            
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                
                # Write the title/header row for the CSV
                writer.writerow(["X", "X_squared"])
                
                # Loop through the numbers, square them, and write them down
                for number in content_list:
                    squared_number = number * number
                    writer.writerow([number, squared_number])
                
        # 8. Copy the 2 Jupyter Notebook files into this new subfolder
        for src_file in source_files:
            # First, check if the original file exists
            if os.path.exists(src_file):
                # Figure out what the new file path should be
                new_file_name = os.path.basename(src_file)
                dest_file = os.path.join(folder_name, new_file_name)
                
                # Only copy it if it is NOT already copied there (no duplicate copies)
                if not os.path.exists(dest_file):
                    shutil.copy(src_file, dest_file)
                    
    print(f"Assignment logic completed! All 10 subfolders are ready inside: '{base_dir}'.")

if __name__ == "__main__":
    main()
