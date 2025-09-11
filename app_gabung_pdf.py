import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import io
import fitz  # PyMuPDF

def pdf_page_to_image(page):
    """Render halaman PDF menjadi image (via PyMuPDF)"""
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # resolusi 2x
    img_bytes = pix.tobytes("png")
    return ImageReader(io.BytesIO(img_bytes)), pix.width, pix.height

def convert_pdf_to_a4(reader):
    """Konversi semua halaman PDF ke ukuran A4"""
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    a4_width, a4_height = A4

    # Simpan reader ke file temporary untuk dipakai PyMuPDF
    temp_buf = io.BytesIO()
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.write(temp_buf)
    temp_buf.seek(0)

    doc = fitz.open(stream=temp_buf, filetype="pdf")

    for page in doc:
        img, w, h = pdf_page_to_image(page)

        # Hitung scale agar fit ke A4
        scale = min(a4_width / w, a4_height / h)
        new_w, new_h = w * scale, h * scale

        # Posisi tengah
        x = (a4_width - new_w) / 2
        y = (a4_height - new_h) / 2

        c.drawImage(img, x, y, new_w, new_h)
        c.showPage()

    c.save()
    buffer.seek(0)
    return PdfReader(buffer)

def run():
    st.set_page_config(page_title="Gabungkan PDF Seragam A4", layout="wide")

    st.title("📚 Gabungkan PDF → Seragam A4")

    uploaded_files = st.file_uploader(
        "Pilih file PDF (boleh lebih dari satu)",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:
        file_names = [f.name for f in uploaded_files]
        order = st.multiselect("Atur urutan PDF", file_names, default=file_names)

        if st.button("Gabungkan PDF"):
            writer = PdfWriter()

            for name in order:
                file = next(f for f in uploaded_files if f.name == name)
                reader = PdfReader(file)

                # Konversi ke A4
                a4_reader = convert_pdf_to_a4(reader)
                for page in a4_reader.pages:
                    writer.add_page(page)

            output_pdf = io.BytesIO()
            writer.write(output_pdf)
            writer.close()

            st.success("✅ PDF berhasil digabung dan diseragamkan ke A4!")
            st.download_button(
                label="💾 Unduh PDF Gabungan (A4)",
                data=output_pdf.getvalue(),
                file_name="gabungan_A4.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    run()
