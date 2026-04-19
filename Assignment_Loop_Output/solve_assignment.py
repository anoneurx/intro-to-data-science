import os
import csv

def solve_assignment():
    # 1. Create a list of 100 numbers (1 to 100)
    numbers = list(range(1, 101))
    
    # 2. Divide into 10 equal parts (each of size 10)
    parts = [numbers[i:i + 10] for i in range(0, 100, 10)]
    
    # 3. Generate 10 folders
    for i in range(10):
        folder_name = f"part_{i + 1}"
        os.makedirs(folder_name, exist_ok=True)
        
        # 4. Create 3 CSV files in each folder
        # Logic: Folder 1 gets parts 1, 2, 3; Folder 2 gets parts 2, 3, 4, etc.
        for j in range(3):
            # Use modulo 10 to wrap back to part 1 after reaching part 10
            chunk_idx = (i + j) % 10
            content = parts[chunk_idx]
            
            file_path = os.path.join(folder_name, f"file_{j + 1}.csv")
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["X", "X_squared"])
                for x in content:
                    writer.writerow([x, x * x])

    print("Success! 10 folders created, each containing 3 CSV files.")

if __name__ == "__main__":
    solve_assignment()
