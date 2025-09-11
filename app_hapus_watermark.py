import streamlit as st
import fitz  # PyMuPDF
import io
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image

def run():
    st.set_page_config(page_title="Hapus Watermark / Crop PDF", page_icon="✂️", layout="wide")
    st.title("✂️ Hapus Watermark PDF - CamScanner (Overlay / Crop)")

    uploaded_file = st.file_uploader("Upload file PDF", type=["pdf"])

    if uploaded_file:
        file_bytes = uploaded_file.read()
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        total_pages = len(doc)

        st.info(f"PDF punya {total_pages} halaman.")

        # Preview halaman pertama
        page = doc[0]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        st.subheader("Preview Halaman Pertama (asli)")
        st.image(img, caption="Halaman 1 sebelum diproses", use_container_width=True)

        # Pilihan mode
        mode = st.radio("Pilih metode:", ["Overlay Putih", "Crop"])

        # Slider untuk atur tinggi bagian bawah
        cut_height = st.slider("Tinggi bagian bawah (pixel)", 0, img.height // 2, 80)

        if st.button("Proses PDF"):
            reader = PdfReader(io.BytesIO(file_bytes))
            writer = PdfWriter()

            if mode == "Overlay Putih":
                # Salin dokumen untuk edit
                doc_edit = fitz.open(stream=file_bytes, filetype="pdf")

                for i in range(len(doc_edit)):
                    width = float(doc_edit[i].rect.width)
                    height = float(doc_edit[i].rect.height)

                    # Konversi slider pixel -> point PDF
                    ratio = height / img.height
                    overlay_h_pt = cut_height * ratio

                    # Tambahkan overlay putih
                    rect = fitz.Rect(0, height - overlay_h_pt, width, height)
                    doc_edit[i].draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

                # Simpan hasil overlay
                output_pdf = io.BytesIO()
                doc_edit.save(output_pdf)
                output_pdf.seek(0)

                # Preview hasil overlay halaman pertama
                pix = doc_edit[0].get_pixmap(matrix=fitz.Matrix(2, 2))
                result_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                st.subheader("Preview Hasil (Overlay Putih)")
                st.image(result_img, caption="Halaman 1 sesudah overlay", use_container_width=True)

            elif mode == "Crop":
                for i, p in enumerate(reader.pages):
                    width = float(p.mediabox.width)
                    height = float(p.mediabox.height)

                    # Konversi slider pixel -> point PDF
                    ratio = height / img.height
                    bottom_cut = cut_height * ratio

                    # Set crop box
                    p.mediabox.lower_left = (0, bottom_cut)
                    p.mediabox.upper_right = (width, height)

                    writer.add_page(p)

                output_pdf = io.BytesIO()
                writer.write(output_pdf)
                output_pdf.seek(0)

                # Preview hasil crop halaman pertama
                doc_crop = fitz.open(stream=output_pdf.getvalue(), filetype="pdf")
                pix = doc_crop[0].get_pixmap(matrix=fitz.Matrix(2, 2))
                result_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                st.subheader("Preview Hasil (Crop)")
                st.image(result_img, caption="Halaman 1 sesudah crop", use_container_width=True)

            st.success("✅ PDF berhasil diproses!")
            st.download_button(
                label="📥 Download PDF",
                data=output_pdf,
                file_name="processed.pdf",
                mime="application/pdf"
            )

if __name__ == "__main__":
    run()
