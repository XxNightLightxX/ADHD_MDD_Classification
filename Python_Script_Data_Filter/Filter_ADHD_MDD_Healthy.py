import pandas as pd
import os
import shutil

# load the Excel file into a pandas dataframe
df = pd.read_excel('TDBRAIN_participants_V2.xlsx')
df = df[["participants_ID", "formal_status"]]

search_label = "HEALTHY"

# use pandas to filter the dataframe based on the label
filtered_df = df[df["formal_status"] == search_label]

# get all the IDs that match the label
matching_ids = filtered_df["participants_ID"].tolist()

# print the IDs
print("Number of matching entries: ", len(matching_ids))
print("The IDs for label {} are: {}".format(search_label, matching_ids))


# specify the path and folders to keep
original_path = "D:\TDbrain\derivatives"
new_path = "D:\TDbrain\HEALTHY"
folders_to_move = matching_ids

# create the new path if it doesn't already exist
if not os.path.exists(new_path):
    os.makedirs(new_path)

# move the folders to the new path
for folder in folders_to_move:
    old_path = os.path.join(original_path, folder)
    new_folder_path = os.path.join(new_path, folder)
    try:
        if os.path.exists(old_path):
            shutil.move(old_path, new_folder_path)
            print(f"{folder} moved to {new_folder_path}")
        else:
            print(f"{folder} does not exist in the current working directory")
    except shutil.Error as e:
        print(f"Error: {e}")

