import streamlit as st

# Import semua modul fitur (app.py kamu)
import app_kelola_halaman
import app_tambah_watermark
import app_gabung_pdf
import app_hapus_watermark

st.set_page_config(page_title="📑 PDF Tools", layout="wide")

# Sidebar dengan styling dan ikon besar
st.sidebar.title("📂 Menu Navigasi")
menu = st.sidebar.radio(
    "Pilih fitur:",
    ["🏠 Beranda", "🗑️ Kelola Halaman PDF", "💧 Tambah Watermark", "📚 Gabung PDF", "✂️ Hapus Watermark"],
    index=0,
    key="menu_radio"
)

# Header utama
st.markdown(
    """
    <h1 style='text-align: center; color: #4B8BBE; font-weight: bold;'>
        📑 PDF Tools
    </h1>
    <hr>
    """,
    unsafe_allow_html=True
)

if menu == "🏠 Beranda":
    st.subheader("Selamat Datang di PDF Tools 👋")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=150)
    with col2:
        st.markdown("""
        Gunakan menu di sebelah kiri untuk memilih fitur:
        - 🗑️ **Kelola halaman PDF**  
        - 💧 **Tambah watermark ke semua halaman**  
        - 📚 **Gabungkan beberapa file PDF**  
        - ✂️ **Hapus watermark PDF - CamScanner**  
        """)
elif menu == "🗑️ Kelola Halaman PDF":
    app_kelola_halaman.run()
elif menu == "💧 Tambah Watermark":
    app_tambah_watermark.run()
elif menu == "📚 Gabung PDF":
    app_gabung_pdf.run()
elif menu == "✂️ Hapus Watermark":
    app_hapus_watermark.run()

# Footer sederhana
st.markdown(
    """
    <hr>
    <p style='text-align: center; color: gray; font-size: 12px;'>
        © 2025 PDF Tools - Dibuat Oleh Sendhy Maula Ammarulloh
    </p>
    """,
    unsafe_allow_html=True
)
