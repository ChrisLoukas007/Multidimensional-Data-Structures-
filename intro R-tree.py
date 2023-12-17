from rtree import index
from datasketch import MinHash, MinHashLSH
import csv
import matplotlib.pyplot as plt

# Define rtree_index in the global scope
rtree_index = None

def visualize_rtree(index, data):
    for i, entry in enumerate(data):
        _, _, _, dblp_record = entry
        result_ids = list(index.intersection((i, i, dblp_record, i, i, dblp_record)))

        for result_id in result_ids:
            try:
                plot_bounding_box(index, result_id)
            except Exception as e:
                print(f"Error visualizing bounding box for entry {result_id}: {e}")

    plt.title('R-tree Visualization')
    plt.xlabel('Dimension 1')
    plt.ylabel('Dimension 2')
    plt.show()

def plot_bounding_box(index, result_id):
    # Use iter_search to find the bounding boxes associated with the result IDs
    for item in index.iter_search(result_id):
        bounding_box = item.bbox
        min_x, min_y, min_z, max_x, max_y, max_z = bounding_box
        plt.plot([min_x, min_x, max_x, max_x, min_x], [min_y, max_y, max_y, min_y, min_y], 'b-')

def create_rtree(data):
    p = index.Property()
    p.dimension = 3  # 3 dimensions for Surname, #Awards, and #DBLP_Record
    idx = index.Index(properties=p)

    for i, entry in enumerate(data):
        surname, awards, _, dblp_record = entry
        bounding_box = (i, i, awards, awards, dblp_record, dblp_record)
        bounding_box = tuple(min(bounding_box[i], bounding_box[i + 1]) for i in range(0, len(bounding_box), 2))
        idx.insert(i, bounding_box)

    return idx

def import_dataset_from_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header row
        csv_reader = csv.reader(file)
        for values in csv_reader:
            try:
                surname = values[0].strip()
                awards = int(values[1].strip())
                education = values[2].strip()
                dblp_record = int(values[3].strip(')'))  # Remove trailing ')' and trim spaces
                data.append((surname, awards, education, dblp_record))
            except ValueError as e:
                print(f"Error parsing entry: {values}")
                print(f"Error message: {e}")

    return data

def create_minhash(text):
    minhash = MinHash()
    for word in text.split():
        minhash.update(word.encode('utf-8'))
    return minhash

def main():
    global rtree_index  # Declare rtree_index as global
    # Import dataset from CSV
    dataset_path = 'datasetSiouta.csv'  # Adjust the filename
    data = import_dataset_from_csv(dataset_path)

    # Create R-tree index
    rtree_index = create_rtree(data)

    # Example: Using LSH for Similarity Queries on Surname field
    threshold = 0.5  # Adjust as needed
    lsh = MinHashLSH(threshold=threshold, num_perm=128)

    # Insert MinHash signatures for each surname into LSH
    for i, entry in enumerate(data):
        surname, _, _, _ = entry
        minhash = create_minhash(surname)
        lsh.insert(i, minhash)

    # Example similarity query
    query_text = "Johnson"  # Replace with your query
    query_minhash = create_minhash(query_text)
    result_ids = lsh.query(query_minhash)

    # Display the result
    print(f"Similar entries to '{query_text}' with threshold {threshold}:")
    for result_id in result_ids:
        print(data[result_id])

    # Visualize the R-tree after running the queries
    visualize_rtree(rtree_index, data)

if __name__ == "__main__":
    main()
