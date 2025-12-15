# 🎨 Color Graphing – Python Visualization

## 📌 Giới thiệu
Color Graphing là một dự án trực quan hóa dữ liệu bằng màu sắc và đồ thị.
Mục tiêu chính:
+ Hiển thị dữ liệu dưới dạng biểu đồ trực quan.
+ Sử dụng màu sắc để phân biệt, làm nổi bật các nhóm dữ liệu.
+ Hỗ trợ minh họa thuật toán, học tập và trình bày kết quả.

## 📁 Cấu trúc thư mục
```
Color_Graphing/
├── data/              # Chứa dữ liệu đầu vào (JSON, TXT, CSV, …)
│   ├── adj_matrix.txt
│   ├── edge_list.txt
│   ├── edges.txt
│   ├── graph_sample.txt
│   └── matrix.txt
├── src/               # Mã nguồn chính
│   ├── MinhHoa.py     # Script minh họa trực quan
│   ├── ToMauDoThi.py  # Thuật toán tô màu đồ thị
└── README.md          # Tài liệu mô tả dự án
```


## 🧠 Các chức năng chính
*Chức năng*
- Mô tả ngắn gọn
- Đọc dữ liệu đồ thị
- Hỗ trợ ma trận kề, danh sách cạnh
- Vẽ biểu đồ
- Biểu diễn đồ thị bằng matplotlib 
- Tô màu đồ thị
- Hiển thị trực quan quá trình tô màu hoặc duyệt đồ thị

## ✨ Ví dụ minh họa
Đồ thị có màu: mỗi đỉnh được tô màu khác nhau theo nhóm hoặc theo thuật toán.
Minh họa thuật toán: hiển thị quá trình tô màu.

## 📌 Ghi chú
- Đảm bảo dữ liệu đầu vào có định dạng đúng (ma trận số, danh sách cạnh).
- Có thể mở rộng thêm các thuật toán khác như BFS, DFS, tô màu tối ưu.
- Hỗ trợ tốt cho trình bày hoặc nghiên cứu thuật toán đồ thị.
