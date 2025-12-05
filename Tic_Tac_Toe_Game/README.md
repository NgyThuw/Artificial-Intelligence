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

## 🚀 Tối ưu hóa với Alpha-Beta + Heuristic

#### Giai đoạn 1: Alpha-Beta + Giới hạn Độ sâu

    def advanced_minimax(board, depth, alpha, beta, isMaximizing, max_depth=3):
    if depth >= max_depth:
        return evaluate_board_heuristic(board)
    
    winner = GetWinner(board)
    if winner is not None:
        return 10000 - depth if winner == "X" else -10000 + depth
    
    available = GetAvailableCells(board)
    if not available:
        return 0
    
    ordered_moves = order_moves_by_priority(board, available, isMaximizing)
    
    if isMaximizing:
        best_score = -math.inf
        for move in ordered_moves:
            i, j = flat_index_to_board(move, len(board))
            board[i][j] = "X"
            score = advanced_minimax(board, depth+1, alpha, beta, False, max_depth)
            board[i][j] = ' '
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        # Tương tự cho minimizing player


#### Giai đoạn 2: Thêm Heuristic Đánh giá

        def evaluate_board_heuristic(board):
            score = 0
            size = len(board)
            for i in range(size):
                for j in range(size):
                    if board[i][j] != ' ':
                        score += evaluate_position(board, i, j)
            return score

        def evaluate_position(board, i, j):
            player = board[i][j]
            multiplier = 1 if player == "X" else -1
            score = 0
            directions = [(0,1), (1,0), (1,1), (1,-1)]
    
            for dx, dy in directions:
                sequence_score = evaluate_sequence(board, i, j, dx, dy, player)
                score += sequence_score
    
            return score * multiplier

        def evaluate_sequence(board, i, j, dx, dy, player):
            # Logic đếm pattern
            if count == 5: return 100000    # Thắng
            if count == 4: 
                if open_ends == 2: return 10000   # 4 đầu mở
                if open_ends == 1: return 1000    # 4 một đầu mở
            if count == 3:
                if open_ends == 2: return 500     # 3 đầu mở
                if open_ends == 1: return 100     # 3 một đầu mở
            if count == 2:
                if open_ends == 2: return 50      # 2 đầu mở
            return 0

#### Giai đoạn 3: Sắp xếp Nước đi Thông minh

        def order_moves_by_priority(board, moves, isMaximizing):
            scored_moves = []
            size = len(board)
    
            for move in moves:
                i, j = flat_index_to_board(move, size)
                score = 0
        
                # Ưu tiên trung tâm
                center = size // 2
                distance_from_center = abs(i - center) + abs(j - center)
                score += (size - distance_from_center) * 10
        
                # Ưu tiên gần quân đã có
                score += count_adjacent_pieces(board, i, j) * 100
        
                # Ưu tiên tấn công/phòng thủ
                if isMaximizing:
                    score += evaluate_attack_potential(board, i, j, "X") * 1000
                else:
                    score += evaluate_attack_potential(board, i, j, "O") * 1000
        
                scored_moves.append((score, move))
    
            scored_moves.sort(reverse=True, key=lambda x: x[0])
            return [move for _, move in scored_moves]

#### Giai đoạn 4: Giới hạn Vùng Tìm kiếm
```python
def get_relevant_moves(board, last_move=None, radius=2):
    """Chỉ xét nước đi trong bán kính quanh các quân cờ hiện có"""
    size = len(board)
    if last_move is None:
        return [board_to_flat_index(size//2, size//2, size)]
    
    relevant_moves = set()
    occupied_positions = get_occupied_positions(board)
    
    for i, j in occupied_positions:
        for di in range(-radius, radius+1):
            for dj in range(-radius, radius+1):
                ni, nj = i + di, j + dj
                if 0 <= ni < size and 0 <= nj < size and board[ni][nj] == ' ':
                    relevant_moves.add(board_to_flat_index(ni, nj, size))
    
    return list(relevant_moves)
```

## 💡 Kết luận
Việc kết hợp **Cắt tỉa Alpha-Beta** với **Heuristic evaluation** và các kỹ thuật tối ưu hóa cho phép xử lý hiệu quả các bàn cờ lớn mà vẫn đảm bảo chất lượng nước đi tối ưu.
Hiệu suất giữa đọc danh sách cạnh và ma trận kề

Danh sách ma trận kề
- Tốn nhiều bộ nhớ do phải duyệt tất cả cạnh O(n2) nhưng kiểm tra cạnh với thời gian O(1) ->Tốt cho đồ thị dày
- Với đồ thị thưa thì lãng phí bộ nhớ
Danh sách cạnh
- Chỉ lưu cạnh thực sự tồn tại nên việc duyệt tất cả cạnh nhanh, dễ đọc và xử lý file
- Nhưng việc kiểm tra cạnh giữa u va v chậm, do phải lấy danh sách kề của một đỉnh nên cần phải duyệt toàn bộ

Khuyến nghị khi lựa chọn dạng file
Dùng danh sách cạnh khi
- Đồ thị thưa
- Bộ nhớ hạn chế
- Đồ thị lớn
- Không cần kiểm tra cạnh thường xuyên
Dùng ma trận kề khi
- Đồ thị rất dày
- Cần kiểm tra cạnh liên tục với O(1)
- Đồ thị nhỏ
- Đơn giản trong cài đặt
==================================================================
Thuật toán tô màu đồ thị

Ràng buộc: 2 đỉnh kề nhau không được tô cùng màu
Màu được sử dụng để tô : red, green, blue
Tô màu làm sao để sử dụng ít màu nhất có thể

#Hình ảnh đồ thị có 6 đỉnh
---Ma trận kề---
	A	B	C	D	E	F	BẬC
A	0	1	1	0	0	1	3
B	1	0	1	1	0	0	3
C	1	1	0	1	0	1	4
D	0	1	1	0	1	0	3
E	0	0	0	1	0	0	1
F	1	0	1	0	0	0	2

Bước 1: Chọn đỉnh có bậc lớn nhất để tô màu (lựa chọn đỉnh C)
Bước 2: Hạ bậc đỉnh 3 về 0 và các đỉnh liền kề nó xuống 1 bậc (hạ đỉnh 1,2,4,6)

#Hình ảnh đồ thị sau khi tô màu đỉnh 3

Bước 1: Chọn ngẫu nhiên một đỉnh bậc 2 ( do cùng bậc 2), chọn đỉnh 1 và tô màu khác với màu đỉnh 3 
(nếu chọn màu giống như màu đỉnh 3 thì sẽ vi phạm ràng buộc)
Bước 2: Hạ bậc đỉnh 1 về 0 và các đỉnh liền kề bị hạ bậc là 




