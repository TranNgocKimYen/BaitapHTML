import pandas as pd
import plotly.express as px

# Đọc dữ liệu từ file Excel
file_path = "D:/HK2_MLBA/dataset-416.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Loại bỏ các hàng không có thông tin quan trọng
df = df.dropna(subset=["Loại môn học", "Học Kỳ", "Tên học phần"])

# Chuyển đổi cột "Học Kỳ" sang kiểu số nguyên
df["Học Kỳ"] = df["Học Kỳ"].astype(int)

# Tạo cột tổng số tín chỉ từ tên học kỳ
df["Học Kỳ (TC)"] = "Học kỳ " + df["Học Kỳ"].astype(str) + " (" + df.groupby("Học Kỳ")["Mã HP"].transform("count").astype(str) + "TC)"

# Nhóm dữ liệu theo học kỳ, loại môn và tên môn học
grouped_data = df.groupby(["Học Kỳ (TC)", "Loại môn học", "Tên học phần"]).size().reset_index(name="Số lượng")

# Tạo biểu đồ Sunburst Chart
fig = px.sunburst(grouped_data, path=["Học Kỳ (TC)", "Loại môn học", "Tên học phần"], values="Số lượng",
                  title="Chương trình đào tạo ngành 416",
                  color="Loại môn học",
                  color_discrete_map={"Bắt buộc": "#FFA07A", "Tự chọn": "#20B2AA"})

# Lưu biểu đồ thành file HTML
fig.write_html("416_10k.html")

# # Hiển thị biểu đồ
# fig.show()
