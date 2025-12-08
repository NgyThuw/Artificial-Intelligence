def read_adjacency_matrix_from_file(filename):
    """Đọc ma trận kề từ file txt"""
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Loại bỏ khoảng trắng và chuyển đổi thành ma trận số
    G = []
    for line in lines:
        line = line.strip()
        if line:
            # Chuyển đổi chuỗi số thành list integer
            row = [int(x) for x in line.split()]
            G.append(row)
    
    return G

def read_adjacency_list_from_file(filename):
    """Đọc danh sách kề từ file txt"""
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Xác định số đỉnh
    n = int(lines[0].strip())
    
    # Khởi tạo ma trận kề
    G = [[0] * n for _ in range(n)]
    
    # Đọc các cạnh
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line:
            u, v = map(int, line.split())
            G[u][v] = 1
            G[v][u] = 1  # Đồ thị vô hướng
    
    return G

def greedy_coloring(G, node_labels=None):
    """Thuật toán tô màu đồ thị greedy"""
    n = len(G)
    
    # Tạo nhãn đỉnh nếu không được cung cấp
    if node_labels is None:
        node_labels = [chr(65 + i) for i in range(n)]  # A, B, C, ...
    
    # Tạo dictionary ánh xạ đỉnh sang chỉ số
    t_ = {}
    for i in range(n):
        t_[node_labels[i]] = i
    
    # Tính bậc của các đỉnh
    degree = []
    for i in range(n):
        degree.append(sum(G[i]))
    
    # Khởi tạo màu có thể sử dụng cho mỗi đỉnh
    colors = ["Blue", "Red", "Green"]
    colorDict = {}
    for i in range(n):
        colorDict[node_labels[i]] = colors.copy()
    
    # Sắp xếp các đỉnh theo bậc giảm dần
    sorted_indices = sorted(range(n), key=lambda i: degree[i], reverse=True)
    sortedNode = [node_labels[i] for i in sorted_indices]
    
    # Tô màu các đỉnh
    solution = {}
    for node in sortedNode:
        if colorDict[node]:  # Nếu còn màu có thể sử dụng
            chosen_color = colorDict[node][0]
            solution[node] = chosen_color
            
            # Xóa màu đã chọn khỏi các đỉnh kề
            node_idx = t_[node]
            for j in range(n):
                if G[node_idx][j] == 1 and chosen_color in colorDict[node_labels[j]]:
                    colorDict[node_labels[j]].remove(chosen_color)
    
    return solution, colorDict

def print_solution(solution):
    """In kết quả tô màu"""
    print("Kết quả tô màu đồ thị:")
    for node, color in sorted(solution.items()):
        print(f"Đỉnh {node} = {color}")

def main():
    print("Chọn chế độ nhập dữ liệu:")
    print("1. Nhập ma trận kề từ file")
    print("2. Nhập danh sách cạnh từ file")
    print("3. Sử dụng ma trận mặc định")
    
    choice = input("Nhập lựa chọn (1/2/3): ")
    
    if choice == '1':
        filename = input("Nhập tên file chứa ma trận kề: ")
        try:
            G = read_adjacency_matrix_from_file(filename)
            print(f"Đã đọc ma trận kề {len(G)}x{len(G)} từ file")
        except FileNotFoundError:
            print(f"File {filename} không tồn tại. Sử dụng ma trận mặc định.")
            # Ma trận kề mặc định
            G = [
                [0, 1, 0, 1, 0, 0],
                [1, 0, 1, 1, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 0, 0]
            ]
    
    elif choice == '2':
        filename = input("Nhập tên file chứa danh sách cạnh: ")
        try:
            G = read_adjacency_list_from_file(filename)
            print(f"Đã đọc đồ thị có {len(G)} đỉnh từ file")
        except FileNotFoundError:
            print(f"File {filename} không tồn tại. Sử dụng ma trận mặc định.")
            G = [
                [0, 1, 0, 1, 0, 0],
                [1, 0, 1, 1, 1, 0],
                [0, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1],
                [0, 1, 1, 1, 0, 0],
                [0, 0, 0, 1, 0, 0]
            ]
    
    else:
        # Ma trận kề mặc định
        G = [
            [0, 1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 1],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0]
        ]
        print("Sử dụng ma trận mặc định:")
    
    # Nhãn các đỉnh
    n = len(G)
    node_labels = [chr(65 + i) for i in range(n)]  # A, B, C, ...
    
    # In ma trận kề
    print("\nMa trận kề:")
    print("  " + " ".join(node_labels))
    for i in range(n):
        print(f"{node_labels[i]} " + " ".join(str(x) for x in G[i]))
    
    # Thực hiện thuật toán tô màu
    solution, colorDict = greedy_coloring(G, node_labels)
    
    # In kết quả
    print("\n" + "="*40)
    print_solution(solution)
    
    # Số màu sử dụng
    colors_used = set(solution.values())
    print(f"\nTổng số màu sử dụng: {len(colors_used)}")
    print(f"Các màu đã sử dụng: {', '.join(colors_used)}")
    
    return solution, G, node_labels

if __name__ == "__main__":
    solution, G, node_labels = main()