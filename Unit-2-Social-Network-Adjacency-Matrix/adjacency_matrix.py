def create_adjacency_matrix(users, friendships):
    index = {user: i for i, user in enumerate(users)}
    matrix = [[0] * len(users) for _ in users]

    for u, v in friendships:
        i, j = index[u], index[v]
        matrix[i][j] = matrix[j][i] = 1
    return matrix


def display_matrix(users, matrix):
    print("    " + " ".join(f"{u:>4}" for u in users))
    for user, row in zip(users, matrix):
        print(f"{user:>4} " + " ".join(f"{x:>4}" for x in row))


if __name__ == "__main__":
    users = ["U1", "U2", "U3", "U4", "U5"]
    friendships = [("U1", "U2"), ("U1", "U3"), ("U2", "U4"), ("U3", "U5")]

    matrix = create_adjacency_matrix(users, friendships)
    print("Social Network Adjacency Matrix\n")
    display_matrix(users, matrix)
    print("\nU1 and U3 connected:", bool(matrix[0][2]))
    print("U2 and U5 connected:", bool(matrix[1][4]))
