
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quan ly diem sinh vien", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    "Ho_va_ten": [
        "Nguyen Van An", "Tran Thi Binh",
        "Le Van Cuong", "Pham Thi Dung",
        "Hoang Van Em", "Vo Thi Giang",
        "Dang Van Hung", "Bui Thi Lan",
        "Do Van Minh", "Ngo Thi Nga"
    ],
    "Chuyen_can": [9, 8, 10, 7, 8.5, 9, 6, 10, 7.5, 9],
    "Giua_ky": [8, 7.5, 9, 8, 7, 8.5, 6.5, 9, 8, 7.5],
    "Cuoi_ky": [8.5, 8, 9.5, 7.5, 8, 9, 7, 9.5, 8.5, 8]
}

df = pd.DataFrame(data)
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

st.subheader("Bảng điểm sinh viên")
bang = df.rename(columns={
    "Ho_va_ten": "Họ và tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})
st.dataframe(bang, use_container_width=True, hide_index=True)

st.subheader("Thống kê lớp")
a, b, c, d = st.columns(4)
a.metric("Điểm trung bình", f"{df['Tong_ket'].mean():.2f}")
b.metric("Điểm cao nhất", f"{df['Tong_ket'].max():.2f}")
c.metric("Điểm thấp nhất", f"{df['Tong_ket'].min():.2f}")
d.metric("Số sinh viên đạt", f"{(df['Tong_ket'] >= 5).sum()}/10")

st.subheader("Tra cứu sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Ho_va_ten"])
sv = df[df["Ho_va_ten"] == ten].iloc[0]
st.write("Chuyên cần:", sv["Chuyen_can"])
st.write("Giữa kỳ:", sv["Giua_ky"])
st.write("Cuối kỳ:", sv["Cuoi_ky"])
st.write("Tổng kết:", sv["Tong_ket"])
st.write("Xếp loại:", sv["Xep_loai"])

st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df["Ho_va_ten"], df["Tong_ket"])
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ và tên")
ax.set_xlim(0, 10)
ax.invert_yaxis()
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.divider()
st.caption("Người tạo: [Nguyễn Tiến Hưng] | MSSV: [038208023235]")
