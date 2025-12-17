Giải thích các thư mục:
    LSTNet: chứa model chính
        data: chứa 4 bộ dữ liệu
        save: chứa kết quả huấn luyện của 64 mô hình LSTNet, được chia thành 4 biến thể là Full, no-ar, no-skip, no-cnn
            trong save có file history lưu lại quá trình và thay đổi chỉ số huấn luyện theo từng epoch
    
    Plots: chứa các ảnh Plots
    reconstructed_logs: do ban đầu nhóm chạy lệnh trong terminal nên phải reconstruct lại trong các file jupyter notebooks, được chia thành 4 notebook tương tự như cách chia thư mục save