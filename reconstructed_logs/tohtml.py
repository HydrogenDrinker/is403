import os
import glob
import subprocess

def convert_notebooks_to_html():
    # 1. Tìm tất cả các file có đuôi .ipynb trong thư mục hiện tại
    notebook_files = glob.glob("*.ipynb")
    
    if not notebook_files:
        print("Không tìm thấy file .ipynb nào trong thư mục này.")
        return

    print(f"Tìm thấy {len(notebook_files)} file notebook. Bắt đầu chuyển đổi...\n")

    for file_name in notebook_files:
        try:
            # 2. Tạo lệnh chuyển đổi
            # Sử dụng f-string để chèn tên file. Thêm dấu ngoặc kép "" để xử lý tên file có khoảng trắng
            cmd = f'jupyter nbconvert --to html "{file_name}"'
            
            # 3. Thực thi lệnh
            print(f"⏳ Đang xử lý: {file_name}...")
            subprocess.run(cmd, shell=True, check=True)
            
            print(f"✅ Thành công: {file_name} -> {file_name.replace('.ipynb', '.html')}")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Lỗi khi chuyển đổi file {file_name}: {e}")

    print("\n🎉 Đã hoàn tất quá trình chuyển đổi!")

if __name__ == "__main__":
    convert_notebooks_to_html()