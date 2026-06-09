import itertools

# ==========================================
# (1) PHÂN TÍCH VÀ THIẾT KẾ
# ==========================================
"""
1. Phân biệt itertools.combinations và itertools.permutations:
   - combinations (Tổ hợp): Lấy ra các cặp phần tử mà KHÔNG quan tâm đến thứ tự. 
     Tức là (A, B) và (B, A) được coi là giống nhau và chỉ lấy 1 lần.
   - permutations (Chỉnh hợp): Lấy ra các cặp phần tử CÓ quan tâm đến thứ tự. 
     Tức là (A, B) và (B, A) được coi là 2 cặp khác nhau.
   - Vì giải đấu "vòng tròn một lượt" mỗi đội chỉ gặp nhau đúng 1 lần (Đội A đấu Đội B 
     cũng là Đội B đấu Đội A), nên bắt buộc phải dùng combinations.

2. Luồng thuật toán sinh mã ID và tự điền số 0:
   - Dùng hàm enumerate() để vừa duyệt qua các trận đấu vừa lấy ra số thứ tự (chỉ số index từ 0).
   - Để tự động biến số thứ tự thành dạng 2 chữ số (01, 02...), ta dùng định dạng F-String {:02d}. 
     Cú pháp này báo cho Python biết đây là số nguyên (d), độ dài tối thiểu là 2 ký tự (2), 
     và nếu thiếu ký tự thì lấp đầy bằng số 0 (0) ở phía trước.
"""

# ==========================================
# KHỞI TẠO DỮ LIỆU TOÀN CỤC
# ==========================================
teams_list = []
match_schedule = []

# ==========================================
# CÁC HÀM NGHIỆP VỤ
# ==========================================

# Chức năng 1: 
def input_teams():
    global teams_list
    print("\n--- NHẬP DANH SÁCH ---")
    raw_input = input("Nhập các đội (cách nhau bởi dấu phẩy): ")
    
    if not raw_input.strip():
        print("Danh sách nhập không được để trống!")
        return
        
    temp_list = [team.strip().upper() for team in raw_input.split(',')]
    
    teams_list = list(dict.fromkeys([t for t in temp_list if t != ""]))
    
    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")

def create_schedule():
    global match_schedule
    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    
    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        match_schedule = []  
        return

    pairs = list(itertools.combinations(teams_list, 2))
    match_schedule = [f"{team1} vs {team2}" for team1, team2 in pairs]
    
    for idx, match in enumerate(match_schedule, 1):
        print(f"{idx}. {match}")
        
    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")

# Chức năng 3:
def generate_match_ids():
    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")
    
    if not match_schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    for idx, match in enumerate(match_schedule, 1):
        team1, team2 = match.split(' vs ')
        
        team1_code = f"{team1[0:3]:X<3}"
        team2_code = f"{team2[0:3]:X<3}"
        
        match_id = f"M{idx:02d}-{team1_code}-{team2_code}"
        print(f"Trận {idx} ({match}) -> ID: {match_id}")

# ==========================================
# VÒNG LẶP ĐIỀU KHIỂN CHƯƠNG TRÌNH
# ==========================================
while True:
    print("\n============= ESPORTS MATCHMAKER =============")
    print("1. Nhập danh sách Đội tuyển")
    print("2. Tạo lịch thi đấu (Combinations)")
    print("3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)")
    print("4. Đóng hệ thống")
    print("==============================================")
    
    try:
        choice = int(input("Chọn chức năng (1-4): "))
        
        if choice == 1:
            input_teams()
        elif choice == 2:
            create_schedule()
        elif choice == 3:
            generate_match_ids()
        elif choice == 4:
            print("Đã đóng hệ thống bốc thăm giải đấu. Tạm biệt!")
            break
        else:
            print("Vui lòng chọn từ 1 đến 4!")
            
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ!")