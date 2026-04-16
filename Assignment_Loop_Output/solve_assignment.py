import os
import shutil
import csv

def main():
    # Base directory for the output
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(base_dir, exist_ok=True)
    
    # Secure values 1 to 100
    values = list(range(1, 101))
    
    # 10 equal parts
    parts = [values[i:i + 10] for i in range(0, 100, 10)]
    
    # 2 different files already saved in other subfolders
    parent_dir = os.path.dirname(base_dir)
    source_files = [
        os.path.join(parent_dir, "Study_Materials/Python_AdvancedLoops_Patterns.ipynb"),
        os.path.join(parent_dir, "Study_Materials/Python_Basics_DataTypes_Variables.ipynb")
    ]
    
    for idx, part in enumerate(parts):
        folder_name = os.path.join(base_dir, f"part_{idx+1}")
        os.makedirs(folder_name, exist_ok=True)
        
        # Every subfolder has at least 3 sub files
        sub_files_content = {
            "file_chunk_1.csv": part,
            "file_chunk_2.csv": part,
            "file_chunk_3.csv": part
        }
        
        for file_name, content in sub_files_content.items():
            file_path = os.path.join(folder_name, file_name)
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["X", "X_squared"])
                for val in content:
                    writer.writerow([val, val**2])
                
        # Copy the 2 files, handling "no duplicate copy"
        for src_file in source_files:
            if os.path.exists(src_file):
                dest_file = os.path.join(folder_name, os.path.basename(src_file))
                # Only copy if the destination doesn't already exist (no duplicate copy)
                if not os.path.exists(dest_file):
                    shutil.copy(src_file, dest_file)
                    
    print(f"Assignment logic completed successfully! Output generated in '{base_dir}'.")

if __name__ == "__main__":
    main()
