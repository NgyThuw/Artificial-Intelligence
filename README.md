# 🧠 AI-Problem-Solving-Algorithms

Dự án này là tập hợp các bài toán và thuật toán trí tuệ nhân tạo (Artificial Intelligence - AI) được giải quyết bằng Python. Trọng tâm là minh họa cách các thuật toán tìm kiếm và tối ưu hóa cổ điển được áp dụng trong các vấn đề cụ thể.

---


## 🎯 Cấu Trúc Dự Án

Repository được tổ chức thành các thư mục riêng biệt, mỗi thư mục đại diện cho một bài toán/thuật toán khác nhau:

### 1. 🎨 Color_Graphing (Tô Màu Đồ Thị)
* **Mô tả:** Triển khai thuật toán tìm kiếm để tô màu các đỉnh của đồ thị sao cho không có hai đỉnh kề nhau nào có cùng màu, sử dụng số lượng màu ít nhất có thể.
* **Các tệp chính:**
    * `/src/ToMauDoThi.py`: Mã nguồn chính thực thi thuật toán tô màu.
    * `/src/MinhHoa.py`: Mã nguồn mô phỏng thuật toán tô màu sử dụng thư viện turtle.
    * `/data/`: Chứa dữ liệu đầu vào (ví dụ: `edges.txt`, `matrix.txt`) dùng để mô tả cấu trúc đồ thị.
    * `/outputs/`: Chứa hình ảnh ma trận kết quả sau khi tô màu (`matrix4.png`, `matrix5.png`, v.v.).

### 2. ♟️ Tic_Tac_Toe_Game (Trò Chơi Cờ Caro)
* **Mô tả:** Xây dựng một tác nhân AI (Agent) chơi game Tic-Tac-Toe (Cờ Caro) bằng các thuật toán tìm kiếm và ra quyết định.
* **Các tệp chính:**
    * `Minimax.py`: Triển khai thuật toán **Minimax** cơ bản để tìm nước đi tối ưu.
    * `Alpha_Beta.py`: Triển khai thuật toán **Alpha-Beta Pruning** (cải tiến của Minimax) giúp cắt giảm nhánh tìm kiếm và tăng tốc độ quyết định của AI.

### 3. 🗺️ TSP (Travelling Salesperson Problem - Bài Toán Người Du Lịch)
* **Mô tả:** Giải quyết bài toán tìm kiếm đường đi ngắn nhất qua một tập hợp các thành phố, mỗi thành phố được ghé thăm đúng một lần và quay về thành phố xuất phát.
* **Các tệp chính:**
    * `heuristic.py`: Triển khai thuật toán **Nearest Neighbor** để tìm thành phố gần nhất.
    * `dynamic.py`: Triển khai thuật toán **Quy hoạch động** .
    * `utils.py`: Đọc file ma trận
    * `main.py`: Mã nguồn thực thi thuật toán và hiển thị mô hình minh họa so sánh giữa hai phương pháp cho bài toán TSP
---

