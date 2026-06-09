# Khởi tạo danh sách toàn cục
raw_logs = []
processed_logs = []

def clean_data():
    """
    Chức năng 1: Nhập, làm sạch dữ liệu log thô và lưu vào biến toàn cục raw_logs.
    Sử dụng maketrans và translate để loại bỏ ký tự rác (!, @, #, $).
    """
    global raw_logs
    
    raw_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")
    mapping_table = str.maketrans("", "", "!@#$")
    cleaned_string = raw_input.translate(mapping_table)
    
    raw_logs = [log.strip() for log in cleaned_string.split(";") if log.strip()]
    
    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.\n")


def filter_critical_logs():
    """
    Chức năng 2: Lọc các log cảnh báo nguy hiểm bằng List Comprehension.
    Lưu vào biến toàn cục processed_logs.
    """
    global raw_logs, processed_logs
    

    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1\n")
        return
        

    processed_logs = [
        log for log in raw_logs 
        if "error" in log.lower() or "critical" in log.lower()
    ]
    
    print("--- LỌC CẢNH BÁO ---")
    if processed_logs:
        print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
        for log in processed_logs:
            print(f"- {log}")
    else:
        print("Không có log cảnh báo nào.")
    print()

def mask_ip_addresses():
    """
    Chức năng 3: Mã hóa địa chỉ IP trong các log nguy hiểm.
    Bắt buộc Return danh sách log đã mã hóa.
    """
    global raw_logs, processed_logs

    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1\n")
        return []
        
    if not processed_logs:
        print("Không có dữ liệu cảnh báo để mã hóa.\n")
        return []

    masked_logs = []
    
    for log in processed_logs:
        words = log.split()
        masked_words = []
        
        for word in words:
            parts = word.split(".")
            if len(parts) == 4 and all(part.isdigit() for part in parts):
                masked_ip = f"{parts[0]}.{parts[1]}.*.*"
                masked_words.append(masked_ip)
            else:
                masked_words.append(word)
                
        masked_logs.append(" ".join(masked_words))
        
    print("--- MÃ HÓA IP ---")
    print("Báo cáo log an toàn:")
    for i, log in enumerate(masked_logs, 1):
        print(f"{i}. {log}")
    print()
    
    return masked_logs

def main():
    """
    Hàm điều hướng giao diện dòng lệnh của hệ thống.
    Sử dụng match-case để điều hướng luồng
    """
    while True:
        print("============= SECURITY LOG ANALYZER =============")
        print("1. Nhập và làm sạch dữ liệu Log thô")
        print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
        print("3. Mã hóa địa chỉ IP (Masking)")
        print("4. Đóng hệ thống")
        print("=================================================")
        
        choice = input("Chọn chức năng (1-4): ")
        
        match choice:
            case '1':
                print("--- NẠP DỮ LIỆU LOG ---")
                clean_data()
            case '2':
                filter_critical_logs()
            case '3':
                mask_ip_addresses()
            case '4':
                print("Đã đóng hệ thống Security Log Analyzer.")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.\n")

if __name__ == "__main__":
    main()