import functools

# ==========================================
# (1) PHÂN TÍCH VÀ THIẾT KẾ
# ==========================================
"""
1. Cơ chế hoạt động của tham số key trong hàm sort():
   - Tham số key nhận vào một hàm hoặc lambda để áp dụng lên từng phần tử trong list, 
     tạo ra một 'khóa' đại diện để Python đem đi so sánh.
   - Khi trả về Tuple (-rating, price): Python sẽ xét rating trước, dấu trừ (-) giúp 
     đảo ngược thứ tự để xếp giảm dần. Nếu rating bằng nhau, nó xét tiếp sang price. 
     Do price mang dấu dương (+) nên sẽ xếp tăng dần.

2. Cơ chế cộng dồn accumulator của hàm reduce():
   - Hàm reduce() nhận vào một hàm 2 tham số (accumulator và current_value).
   - Ban đầu, nó lấy 2 phần tử đầu: phần tử thứ nhất làm biến tích lũy (accumulator), 
     phần tử thứ hai là giá trị hiện tại (current_value) rồi thực hiện phép cộng.
   - Kết quả trả về tiếp tục làm accumulator mới để cộng dồn với phần tử tiếp theo 
     cho đến khi hết danh sách.
"""

# Dữ liệu mẫu (có thêm sản phẩm lỗi để test bẫy)
product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5",
    "P04-Sạc Dự Phòng-300000",          
    "P05-Loa Máy Tính-400000VND-4.2"      
]

# Chức năng 1
def show_labels():
    print("\n--- DANH SÁCH TEM NHÃN ---")
    template = "Mã: {ma:<10} | Tên: {ten:<20} | Giá: {gia:,} VND | Rating: {sao}*"
    
    for product in product_list:
        try:
            parts = product.split('-')
            if len(parts) < 4:
                raise IndexError
                
            ma, ten, gia_raw, sao_raw = parts
            if not gia_raw.isdigit():
                raise ValueError
                
            gia = int(gia_raw)
            sao = float(sao_raw)
            
            info = {"ma": ma, "ten": ten, "gia": gia, "sao": sao}
            print(template.format_map(info))
            
        except IndexError:
            err_id = product.split('-')[0] if product else "Unknown"
            print(f"Bỏ qua sản phẩm [{err_id}] do sai cấu trúc dữ liệu.")
        except ValueError:
            err_id = product.split('-')[0] if product else "Unknown"
            print(f"Bỏ qua sản phẩm [{err_id}] do lỗi định dạng giá tiền.")

# Chức năng 2
def sort_products():
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    
    def get_sort_key(item):
        try:
            parts = item.split('-')
            if len(parts) < 4 or not parts[2].isdigit():
                return (-1.0, 999999999) 
            return (-float(parts[3]), int(parts[2]))
        except:
            return (-1.0, 999999999)

    product_list.sort(key=get_sort_key)
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    
    stt = 1
    for item in product_list:
        parts = item.split('-')
        if len(parts) == 4 and parts[2].isdigit():
            print(f"{stt}. {item}")
            stt += 1

# Chức năng 3
def calculate_total_stock():
    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    prices = []
    
    for item in product_list:
        try:
            parts = item.split('-')
            if len(parts) == 4 and parts[2].isdigit():
                prices.append(int(parts[2]))
        except:
            continue
            
    if prices:
        total = functools.reduce(lambda acc, curr: acc + curr, prices)
    else:
        total = 0
        
    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND.")

# Menu điều khiển
while True:
    print("\n============= E-COMMERCE ANALYTICS =============")
    print("1. Hiển thị tem nhãn sản phẩm (format_map & F-String)")
    print("2. Sắp xếp sản phẩm thông minh (sort key)")
    print("3. Tính tổng giá trị kho hàng (reduce)")
    print("4. Đóng hệ thống")
    print("================================================")
    
    try:
        choice = int(input("Chọn chức năng (1-4): "))
        
        if choice == 1:
            show_labels()
        elif choice == 2:
            sort_products()
        elif choice == 3:
            calculate_total_stock()
        elif choice == 4:
            print("Đã đóng hệ thống phân tích dữ liệu sản phẩm. Tạm biệt!")
            break
        else:
            print("Vui lòng chỉ chọn các số từ 1 đến 4!")
            
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")