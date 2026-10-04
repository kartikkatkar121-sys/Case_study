def adjacency_to_sparse(matrix):
    sparse = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value != 0:
                sparse.append((i, j, value))
    return sparse


if __name__ == "__main__":
    matrix = [
        [0,1,1,0,0],
        [1,0,0,1,0],
        [1,0,0,0,1],
        [0,1,0,0,0],
        [0,0,1,0,0]
    ]

    print("Sparse Matrix (row, column, value):")
    for item in adjacency_to_sparse(matrix):
        print(item)
