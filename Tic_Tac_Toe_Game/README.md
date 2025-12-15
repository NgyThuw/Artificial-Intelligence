# So sánh Thuật toán Minimax và Alpha-Beta cho Cờ Caro

## 📊 Tổng quan So sánh: cho bàn cờ có kích thước là 3x3

#### *Thuật toán Minimax*
- Ưu điểm:
  - Đơn giản, dễ hiểu và dễ cài đặt
  - Luôn tìm được nước đi tối ưu (duyệt hết các nút)
  - Đảm bảo kết quả chính xác tuyệt đối

- Nhược điểm:
  - Hiệu suất chậm với độ sâu lớn
  - Phải duyệt tất cả các nút
  - Không thực tế cho các loại cờ có kích thước lớn (cờ vua, cờ vây)

#### *Thuật toán cắt tỉa Alpha-Beta* 
* Ưu điểm:
  - Nhanh hơn đáng kể so với Minimax
  - Cắt đi các nút dư thừa, chỉ xét các nút cần thiết
  - Vẫn đảm bảo kết quả tối ưu như Minimax

* Nhược điểm:
  - Phức tạp hơn trong quá trình cài đặt
  - Phụ thuộc vào thứ tự nước đi

## 🎯 Phạm vi Ứng dụng

- Minimax: Phù hợp với bàn cờ nhỏ có kích thước 3x3
- Alpha-Beta: Phù hợp với các bàn cờ có kích thước 5x5 trở lên

## 🔧 Chỉnh sửa Code cho Bàn Cờ Lớn

#### 1. Hàm GetWinner()
```python
def GetWinner(board, board_size=15, win_condition=5):
    # Kiểm tra tất cả hàng ngang
    for i in range(board_size):
        for j in range(board_size - win_condition + 1):
            if all(board[i][j+k] == board[i][j] != ' ' for k in range(win_condition)):
                return board[i][j]
    
    # Kiểm tra tất cả cột dọc
    for i in range(board_size - win_condition + 1):
        for j in range(board_size):
            if all(board[i+k][j] == board[i][j] != ' ' for k in range(win_condition)):
                return board[i][j]
    
    # Kiểm tra đường chéo chính
    for i in range(board_size - win_condition + 1):
        for j in range(board_size - win_condition + 1):
            if all(board[i+k][j+k] == board[i][j] != ' ' for k in range(win_condition)):
                return board[i][j]
    
    # Kiểm tra đường chéo phụ
    for i in range(board_size - win_condition + 1):
        for j in range(win_condition - 1, board_size):
            if all(board[i+k][j-k] == board[i][j] != ' ' for k in range(win_condition)):
                return board[i][j]
    
    return None
```

#### 2. Cấu trúc Dữ liệu Bàn Cờ
```python
def initialize_board(size=15):
    return [[' ' for _ in range(size)] for _ in range(size)]

def board_to_flat_index(i, j, size):
    return i * size + j + 1

def flat_index_to_board(index, size):
    return (index-1) // size, (index-1) % size
```

#### 3. Hàm GetAvailableCells()
```python
def GetAvailableCells(board):
    size = len(board)
    available = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == ' ':
                available.append(board_to_flat_index(i, j, size))
    return available
```

## 💡 Kết luận
Việc kết hợp **Cắt tỉa Alpha-Beta** với **Heuristic evaluation** và các kỹ thuật tối ưu hóa cho phép xử lý hiệu quả các bàn cờ lớn mà vẫn đảm bảo chất lượng nước đi tối ưu.
 Đơn giản trong cài đặt

