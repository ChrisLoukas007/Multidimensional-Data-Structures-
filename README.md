# 📌 R-tree and LSH Implementation in Python

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)  
[![Algorithm](https://img.shields.io/badge/Algorithm-Data%20Structures-green?style=for-the-badge&logo=codeforces)](https://en.wikipedia.org/wiki/R-tree)  
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)](https://jupyter.org/)  

🚀 **A Python-based implementation of R-trees and Locality-Sensitive Hashing (LSH) for efficient spatial and high-dimensional data indexing.**  

---

## **📚 Overview**
This repository contains an implementation of **R-tree** and **Locality-Sensitive Hashing (LSH)**, two widely used data structures for **spatial indexing and approximate nearest neighbor search**. This project was developed as part of **university coursework**, demonstrating key concepts in **high-dimensional data indexing and spatial search optimization**.

### **🔹 Why R-tree and LSH?**
- **R-tree** is widely used in **spatial databases** to optimize range queries and **nearest neighbor searches**.
- **LSH** is crucial for **dimensionality reduction** and **efficient approximate nearest neighbor search** in large datasets.

---

## **⚡ Features**
### **🔶 R-tree Implementation**
✔️ Efficient **spatial data indexing** using the **R-tree** structure.  
✔️ Supports **insertion, deletion, and searching** for spatial objects.  
✔️ Optimized for **2D and multidimensional data**.  

### **🔶 Locality-Sensitive Hashing (LSH) Implementation**
✔️ **Approximate nearest neighbor search** for **high-dimensional** data.  
✔️ Configurable **hash functions** and **hash tables** for a trade-off between **accuracy and speed**.  
✔️ Ideal for applications like **image retrieval, recommendation systems, and geospatial indexing**.  

---

## **📂 Project Structure**
```
/Multidimensional-Data-Structures
├── /data         # Sample datasets
├── R-tree.py     # R-tree implementation
├── LSH.py        # Locality-Sensitive Hashing implementation
├── datasetSiouta.csv  # Sample dataset (CSV format)
├── data.json     # Sample JSON data for testing
├── README.md     # Project documentation
└── .gitignore    # Ignore unnecessary files
```

---

## **📊 Example Usage**
### **R-tree Example**
```python
from R_tree import RTree

rtree = RTree()
rtree.insert(10, 20)
rtree.insert(15, 25)
result = rtree.search(10, 20)
print(result)
```

### **LSH Example**
```python
from LSH import LSH

lsh = LSH(num_hashes=5, num_tables=3)
lsh.insert("vector_1", [0.1, 0.5, 0.8])
nearest = lsh.query([0.15, 0.55, 0.75])
print("Nearest Neighbor:", nearest)
```

---

## **🛠 Installation & Setup**
To run the project, follow these steps:

1️⃣ **Clone the repository**
```bash
git clone https://github.com/ChrisLoukas007/Multidimensional-Data-Structures.git
cd Multidimensional-Data-Structures
```
2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```
3️⃣ **Run the scripts**
```bash
python R-tree.py
python LSH.py
```

---
