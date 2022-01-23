import pandas as pd
import numpy as np

dump_file = open("/Users/agupta26/Personal/anjani/simulation/A2/dump/dump_4.file")
data = dump_file.read()

coordinates_list = []

frames = data.split("ITEM: TIMESTEP")
frames = frames[1:]
for frame in frames:
    coordinates = frame[frame.find("ITEM: ATOMS id type xu yu zu"):]
    lines = coordinates.split("\n")
    curr_df = pd.DataFrame(columns=["id", "type", "xu", "yu", "zu"])
    lines = lines[1:5]
    for line in lines:
        curr_atom_coordinates = line.split()
        curr_df.loc[len(curr_df)] = np.array(curr_atom_coordinates).astype(np.float64)
    coordinates_list = coordinates_list + [curr_df]

# coordinates_list --> contains a list of pandas dataframe.

for coordinate in coordinates_list:
    if coordinate.iloc[0]["xu"] > 5:
        print("akash")