import streamlit as st
import fitz  # PyMuPDF
from PyPDF2 import PdfReader, PdfWriter
import io

def run():
    st.set_page_config(page_title="Kelola Halaman PDF", layout="wide")
    st.title("📑 Kelola Halaman PDF dengan Preview (Hapus atau Pilih)")

    uploaded_file = st.file_uploader("Upload file PDF", type="pdf")

    if uploaded_file:
        # Baca file PDF dengan PyPDF2
        pdf_reader = PdfReader(uploaded_file)
        total_pages = len(pdf_reader.pages)

        # Reset pointer file untuk PyMuPDF
        uploaded_file.seek(0)
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        # Mode operasi
        mode = st.radio(
            "Pilih mode:",
            ["🗑️ Hapus halaman yang dipilih", "📌 Simpan hanya halaman yang dipilih"]
        )

        st.subheader("📖 Preview Halaman")
        col_count = 4  # jumlah kolom preview
        selected_pages = []

        for i in range(total_pages):
            if i % col_count == 0:
                cols = st.columns(col_count)

            pix = doc[i].get_pixmap(matrix=fitz.Matrix(0.5, 0.5))  # resize agar ringan
            img_bytes = pix.tobytes("png")

            with cols[i % col_count]:
                st.image(img_bytes, caption=f"Halaman {i+1}", use_container_width=True)
                if st.checkbox(f"Pilih {i+1}", key=f"chk_{i}"):
                    selected_pages.append(i)

        # Tombol proses
        if st.button("🚀 Proses PDF"):
            pdf_writer = PdfWriter()

            if mode == "🗑️ Hapus halaman yang dipilih":
                for i in range(total_pages):
                    if i not in selected_pages:
                        pdf_writer.add_page(pdf_reader.pages[i])
            else:  # Simpan hanya halaman yang dipilih
                for i in selected_pages:
                    pdf_writer.add_page(pdf_reader.pages[i])

            output = io.BytesIO()
            pdf_writer.write(output)
            output.seek(0)

            st.success("✅ PDF berhasil diproses!")
            st.download_button(
                label="💾 Download PDF Baru",
                data=output,
                file_name="pdf_hasil.pdf",
                mime="application/pdf"
            )
