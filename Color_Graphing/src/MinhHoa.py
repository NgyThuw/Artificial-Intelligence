import turtle
import math
import sys

# Khởi tạo Turtle
screen = turtle.Screen()
screen.title("Minh họa Tô màu Đồ thị")
screen.bgcolor("white")
screen.setup(width=1000, height=700)

# Tạo turtle để vẽ
graph_turtle = turtle.Turtle()
graph_turtle.speed(0)
graph_turtle.hideturtle()

# Tạo turtle để hiển thị thông tin
info_turtle = turtle.Turtle()
info_turtle.hideturtle()
info_turtle.penup()
info_turtle.goto(0, -300)

# Màu sắc cho các đỉnh
colors = [
    "red", "blue", "green", "orange", "purple", 
    "cyan", "magenta", "yellow", "brown", "pink",
    "lime", "teal", "navy", "coral", "indigo"
]

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.adj_matrix = []
        self.coloring = {}
        self.num_vertices = 0
        
    def read_from_edge_list(self, filename):
        """Đọc đồ thị từ file dạng danh sách cạnh"""
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                
            # Đọc số đỉnh (dòng đầu tiên)
            self.num_vertices = int(lines[0].strip())
            
            # Tạo danh sách đỉnh
            self.vertices = [i+1 for i in range(self.num_vertices)]
            
            # Đọc danh sách cạnh
            self.edges = []
            for line in lines[1:]:
                if line.strip():
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        u, v = int(parts[0]), int(parts[1])
                        self.edges.append((u, v))
            
            # Tạo ma trận kề
            self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
            for u, v in self.edges:
                if 1 <= u <= self.num_vertices and 1 <= v <= self.num_vertices:
                    self.adj_matrix[u-1][v-1] = 1
                    self.adj_matrix[v-1][u-1] = 1
            
            print(f"Đã đọc đồ thị từ file {filename}")
            print(f"Số đỉnh: {self.num_vertices}")
            print(f"Số cạnh: {len(self.edges)}")
            print(f"Danh sách cạnh: {self.edges}")
            return True
            
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
            return False
    
    def read_from_adj_matrix(self, filename):
        """Đọc đồ thị từ file dạng ma trận kề"""
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                
            # Đọc ma trận kề
            self.adj_matrix = []
            for line in lines:
                if line.strip():
                    row = list(map(int, line.strip().split()))
                    self.adj_matrix.append(row)
            
            self.num_vertices = len(self.adj_matrix)
            self.vertices = [i+1 for i in range(self.num_vertices)]
            
            # Tạo danh sách cạnh từ ma trận kề
            self.edges = []
            for i in range(self.num_vertices):
                for j in range(i+1, self.num_vertices):
                    if self.adj_matrix[i][j] == 1:
                        self.edges.append((i+1, j+1))
            
            print(f"Đã đọc đồ thị từ file {filename}")
            print(f"Số đỉnh: {self.num_vertices}")
            print(f"Số cạnh: {len(self.edges)}")
            print(f"Ma trận kề:")
            for row in self.adj_matrix:
                print(row)
            return True
            
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
            return False
    
    def greedy_coloring(self):
        """Thuật toán tô màu tham lam cho đồ thị"""
        # Khởi tạo màu cho tất cả các đỉnh là -1 (chưa tô màu)
        colors_result = [-1] * self.num_vertices
        
        # Tô màu cho đỉnh đầu tiên
        colors_result[0] = 0
        
        # Mảng available để theo dõi các màu có sẵn
        available = [False] * self.num_vertices
        
        # Tô màu cho các đỉnh còn lại
        for u in range(1, self.num_vertices):
            # Đánh dấu tất cả các màu của đỉnh kề là không có sẵn
            for v in range(self.num_vertices):
                if self.adj_matrix[u][v] == 1 and colors_result[v] != -1:
                    available[colors_result[v]] = True
            
            # Tìm màu đầu tiên có sẵn
            color = 0
            while color < self.num_vertices:
                if not available[color]:
                    break
                color += 1
            
            # Gán màu cho đỉnh u
            colors_result[u] = color
            
            # Reset mảng available
            available = [False] * self.num_vertices
        
        # Lưu kết quả tô màu
        self.coloring = {}
        for i in range(self.num_vertices):
            self.coloring[i+1] = colors_result[i]
        
        # Đếm số màu sử dụng
        num_colors_used = max(colors_result) + 1
        
        return num_colors_used
    
    def draw_graph(self):
        """Vẽ đồ thị với các đỉnh được tô màu"""
        graph_turtle.clear()
        
        if self.num_vertices == 0:
            info_turtle.clear()
            info_turtle.write("Không có dữ liệu đồ thị để vẽ!", align="center", font=("Arial", 16, "normal"))
            return
        
        # Tính toán vị trí các đỉnh trên vòng tròn
        center_x, center_y = 0, 0
        radius = 200
        
        positions = []
        for i in range(self.num_vertices):
            angle = 2 * math.pi * i / self.num_vertices
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            positions.append((x, y))
        
        # Vẽ các cạnh
        graph_turtle.pensize(1)
        graph_turtle.pencolor("gray")
        
        for u, v in self.edges:
            if 1 <= u <= self.num_vertices and 1 <= v <= self.num_vertices:
                x1, y1 = positions[u-1]
                x2, y2 = positions[v-1]
                
                graph_turtle.penup()
                graph_turtle.goto(x1, y1)
                graph_turtle.pendown()
                graph_turtle.goto(x2, y2)
        
        # Vẽ các đỉnh với màu đã tô
        graph_turtle.pensize(2)
        for i in range(self.num_vertices):
            x, y = positions[i]
            vertex_num = i + 1
            color_idx = self.coloring.get(vertex_num, 0)
            
            # Vẽ đỉnh
            graph_turtle.penup()
            graph_turtle.goto(x, y - 20)
            graph_turtle.pendown()
            graph_turtle.fillcolor(colors[color_idx % len(colors)])
            graph_turtle.begin_fill()
            graph_turtle.circle(20)
            graph_turtle.end_fill()
            
            # Ghi số thứ tự đỉnh
            graph_turtle.penup()
            graph_turtle.goto(x, y - 10)
            graph_turtle.pencolor("black")
            graph_turtle.write(str(vertex_num), align="center", font=("Arial", 12, "bold"))
        
        # Hiển thị thông tin tô màu
        info_turtle.clear()
        color_info = f"Kết quả tô màu đồ thị (sử dụng {max(self.coloring.values())+1} màu):\n"
        for vertex, color_idx in self.coloring.items():
            color_name = colors[color_idx % len(colors)]
            color_info += f"  Đỉnh {vertex}: {color_name}\n"
        
        info_turtle.goto(0, -280)
        info_turtle.write(color_info, align="center", font=("Arial", 12, "normal"))


    """Tạo các file mẫu nếu chưa tồn tại"""
    
    # Tạo file danh sách cạnh mẫu
    edge_list_content = """6
1 2
1 3
1 4
2 3
2 5
3 4
3 6
4 6
5 6"""
    
    with open("edge_list.txt", "w") as f:
        f.write(edge_list_content)
    
    # Tạo file ma trận kề mẫu
    adj_matrix_content = """0 1 1 1 0 0
1 0 1 0 1 0
1 1 0 1 0 1
1 0 1 0 0 1
0 1 0 0 0 1
0 0 1 1 1 0"""
    
    with open("adj_matrix.txt", "w") as f:
        f.write(adj_matrix_content)
    
    print("Đã tạo file mẫu: edge_list.txt và adj_matrix.txt")

def main():
    # Khởi tạo đồ thị
    graph = Graph()
    
    # Hiển thị menu
    print("\n" + "="*50)
    print("MINH HỌA TÔ MÀU ĐỒ THỊ BẰNG TURTLE")
    print("="*50)
    print("1. Đọc đồ thị từ file danh sách cạnh (edges.txt)")
    print("2. Đọc đồ thị từ file ma trận kề (matrix.txt)")
    print("3. Thoát")
    print("="*50)
    
    choice = input("Chọn phương thức đọc dữ liệu (1-3): ").strip()
    
    if choice == "1":
        success = graph.read_from_edge_list("edges.txt")
        file_type = "Danh sách cạnh"
    elif choice == "2":
        success = graph.read_from_adj_matrix("matrix.txt")
        file_type = "Ma trận kề"
    elif choice == "3":
        print("Kết thúc chương trình.")
        turtle.bye()
        sys.exit(0)
    else:
        print("Lựa chọn không hợp lệ.")
    
    if success:
        # Thực hiện tô màu đồ thị
        num_colors = graph.greedy_coloring()
        print(f"\nĐã tô màu đồ thị với {num_colors} màu")
        
        # Vẽ đồ thị
        graph.draw_graph()
        
        # Hiển thị thông tin trên console
        print(f"\nFile đọc: {file_type}")
        print(f"Số đỉnh: {graph.num_vertices}")
        print(f"Số cạnh: {len(graph.edges)}")
        print(f"Kết quả tô màu:")
        for vertex, color_idx in graph.coloring.items():
            color_name = colors[color_idx % len(colors)]
            print(f"  Đỉnh {vertex}: {color_name}")
        
        # Thêm tiêu đề
        title_turtle = turtle.Turtle()
        title_turtle.hideturtle()
        title_turtle.penup()
        title_turtle.goto(0, 320)
        title_turtle.write(f"Minh họa Tô màu Đồ thị - Đọc từ {file_type}", 
                          align="center", font=("Arial", 16, "bold"))
        
        print("\nNhấn vào cửa sổ để thoát...")
        turtle.exitonclick()
    else:
        print("Không thể đọc dữ liệu đồ thị. Vui lòng kiểm tra file đầu vào.")
        turtle.bye()

if __name__ == "__main__":
    main()