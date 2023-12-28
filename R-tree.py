# Import required libraries
import rtree
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read data from a JSON file
with open('data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Set up properties for the R-tree (3D)
p = rtree.index.Property(dimension=3)
idx = rtree.index.Index(properties=p)

# Populate the R-tree with data
for i, entry in enumerate(json_data):
    # Extract relevant information from the JSON entry
    name = entry['name']
    awards = entry['awards']
    dblp_record = entry['dblp_record']
    education = entry.get('education', 'Null')
    letter = entry['letter']
    
    # Convert the letter to an index (A=1, B=2, ..., Z=26)
    letter_index = ord(letter.upper()) - 64

    # Define the bounding box for the R-tree
    bbox = (letter_index, awards, dblp_record, letter_index, awards, dblp_record)

    # Insert the entry into the R-tree
    idx.insert(i, bbox, obj=(name, awards, dblp_record, education))

# Define a query bounding box for the entire dataset
query_bbox = (0, 0, 0, len(json_data), len(json_data), len(json_data))

# Perform a spatial query on the R-tree
results = list(idx.intersection(query_bbox, objects=True))

# Create a new 3D subplot for visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each result point in the 3D space
for result in results:
    bbox = result.bbox
    x = (bbox[0] + bbox[3]) / 2
    y = (bbox[1] + bbox[4]) / 2
    z = (bbox[2] + bbox[5]) / 2
    ax.scatter(x, y, z)

# Set labels for axes
ax.set_xlabel('Letter Index')
ax.set_ylabel('Awards')
ax.set_zlabel('DBLP Record')

# Display the 3D plot
plt.show()
