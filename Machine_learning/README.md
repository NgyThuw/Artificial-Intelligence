# K Means & K Nearest Neighbor
### 📚 Tóm Tắt Thuật Toán K-Nearest Neighbors (KNN)
KNN là một thuật toán học máy đơn giản, thuộc nhóm học có giám sát (supervised learning), chủ yếu được sử dụng cho các bài toán phân loại (classification) 
và đôi khi là hồi quy (regression).

### 🎯 Mục đích
Phân loại một điểm dữ liệu mới dựa trên việc tìm ra K điểm dữ liệu gần nhất đã biết (hàng xóm) trong không gian đặc trưng.

### 🛠️ Cách thức hoạt động
- Chọn K: Xác định số lượng hàng xóm (K) sẽ được xem xét.
- Tính khoảng cách: Tính toán khoảng cách (thường là khoảng cách Euclid) giữa điểm dữ liệu mới và tất cả các điểm dữ liệu đã có trong tập huấn luyện.
- Tìm K láng giềng: Chọn ra K điểm dữ liệu có khoảng cách nhỏ nhất.
- Phân loại (Classification): Lấy ra nhãn của K láng giềng đó. Điểm dữ liệu mới được gán nhãn dựa trên phương pháp bầu chọn đa số (majority vote) từ K láng giềng.
- Hồi quy (Regression): Giá trị dự đoán là giá trị trung bình của K láng giềng.

### 📚 Tóm Tắt Thuật Toán K Means
K-Means là một thuật toán học máy không giám sát (unsupervised learning) được sử dụng để giải quyết bài toán gom cụm (clustering).

### 🎯 Mục đích
Phân chia tập dữ liệu thành K nhóm (cụm) riêng biệt, sao cho các điểm dữ liệu trong cùng một cụm càng giống nhau (khoảng cách gần) 
và các cụm khác nhau càng khác nhau (khoảng cách xa)

### 🛠️ Cách thức hoạt động
- Khởi tạo K: Xác định số lượng cụm (K) mong muốn.
- Chọn tâm cụm ngẫu nhiên: Chọn ngẫu nhiên $K$ điểm dữ liệu làm tâm cụm (centroid) ban đầu.
- Phân cụm (Assignment Step):Mỗi điểm dữ liệu được gán vào cụm có tâm cụm (centroid) gần nó nhất (dựa trên khoảng cách Euclid).
- Cập nhật tâm cụm (Update Step): Tâm cụm mới được tính bằng cách lấy giá trị trung bình của tất cả các điểm dữ liệu đã được gán vào cụm đó.
- Lặp lại: Lặp lại các bước 3 và 4 cho đến khi các tâm cụm không còn thay đổi đáng kể nữa (hội tụ) hoặc đạt đến số lần lặp tối đa.
