import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import fitz  # PyMuPDF
import io

def run():
    def create_image_watermark(image_file):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)

        # load gambar
        img = ImageReader(image_file)

        # ukuran halaman A4
        page_width, page_height = A4

        # tentukan ukuran gambar watermark (misalnya 350x350 px)
        width, height = 400, 350

        # posisi tengah
        x = (page_width - width) / 2
        y = (page_height - height) / 2

        can.saveState()
        can.setFillAlpha(0.1)  # transparansi
        can.drawImage(img, x, y, width=width, height=height, mask='auto')
        can.restoreState()

        can.save()
        packet.seek(0)
        return PdfReader(packet)

    st.title("🖼️ PDF Image Watermark App")

    uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
    uploaded_img = st.file_uploader("Upload gambar watermark (PNG/JPG)", type=["png", "jpg", "jpeg"])

    if uploaded_pdf and uploaded_img:
        reader = PdfReader(uploaded_pdf)
        writer = PdfWriter()

        watermark_pdf = create_image_watermark(uploaded_img)
        watermark_page = watermark_pdf.pages[0]

        for page in reader.pages:
            page.merge_page(watermark_page)
            writer.add_page(page)

        output = io.BytesIO()
        writer.write(output)
        output.seek(0)

        # 🔹 Preview hasil dengan PyMuPDF (halaman pertama)
        doc = fitz.open(stream=output.getvalue(), filetype="pdf")
        page = doc[0]  # halaman pertama
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # zoom biar tajam
        img_bytes = pix.tobytes("png")

        st.image(img_bytes, caption="Preview Halaman Pertama dengan Watermark", use_container_width=True)

        # 🔹 Tombol download
        st.download_button(
            label="📥 Download PDF dengan Watermark Tengah",
            data=output,
            file_name="watermarked.pdf",
            mime="application/pdf"
        )
