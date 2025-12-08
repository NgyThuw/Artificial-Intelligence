# 🧭 Travelling Salesman Problem (TSP) – Python Implementation
## 📌 Mô tả bài toán 
Bài toán người bán hàng (TSP) yêu cầu tìm chu trình ngắn nhất đi qua tất cả các thành phố đúng một lần và quay về điểm xuất phát. Đây là một bài toán tối ưu kinh điển trong AI và toán học.

## 📁 Cấu trúc thư mục
```
TSP/
├── data/               # Chứa các file JSON với ma trận chi phí
│   ├── matrix4.json
│   ├── matrix5.json
│   └── matrix6.json
├── src/                # Chứa mã nguồn chính
│   ├── heuristic.py    # Thuật toán Nearest Neighbor
│   ├── dynamic.py      # Thuật toán Held–Karp (quy hoạch động)
│   ├── utils.py        # Hàm đọc file JSON và tiện ích
│   └── main.py         # Chương trình chính: chạy và vẽ minh họa
└── README.md           # Tài liệu mô tả dự án
```
## 🧠 Các phương pháp sử dụng

| Phương pháp        | Mô tả ngắn gọn                           | Độ chính xác | Tốc độ    |
|--------------------|------------------------------------------|--------------|-----------|
| Nearest Neighbor   | Chọn thành phố gần nhất tiếp theo        | Gần đúng     | Rất nhanh |
| Held–Karp (DP)     | Quy hoạch động với bitmask               | Tối ưu       | Chậm hơn  |

## 📦 Yêu cầu thư viện
```
pip install matplotlib
```
## 📌 Ghi chú
Các file JSON cần đặt đúng trong thư mục data/.
Nếu gặp lỗi FileNotFoundError, kiểm tra lại đường dẫn hoặc dùng ../data/filename.json trong main.py.

## ✨ Ví dụ minh họa
### *Đi qua 4 thành phố*
Với dữ liệu matrix4.json, chương trình sẽ in ra route và chi phí của từng phương pháp.
Biểu đồ minh họa sẽ hiển thị các thành phố và tuyến đường bằng màu khác nhau:
Xanh: Nearest Neighbor
Đỏ: Held–Karp (tối ưu)

<img width="1280" height="612" alt="matrix4" src="https://github.com/user-attachments/assets/3116e107-b1bb-464a-993e-c16f209edac8" />

---

### *Đi qua 5 thành phố*
Tương tự với dữ liệu matrix5.json. 
Do không có chênh lệch nhiều giữa hai thuật toán nên tuyến đường màu xanh (Nearest Neighbor) trùng với tuyến đường màu đỏ (Held-Karp).
Chương trình sẽ ưu tiên hiển thị phương pháp quy hoạch động

<img width="1280" height="612" alt="matrix5" src="https://github.com/user-attachments/assets/2b100b39-5855-45f7-89ae-b3b316aa74d3" />

---

### *Đi qua 6 thành phố*
Với dữ liệu matrix6.json sẽ có sự chênh lệch giữa thuật toán nên ta sẽ thấy rõ hai tuyến đường khác nhau. 

<img width="600" height="600" alt="matrix6" src="https://github.com/user-attachments/assets/9b855992-376c-4365-9018-5da3ddd4c0d7" />
