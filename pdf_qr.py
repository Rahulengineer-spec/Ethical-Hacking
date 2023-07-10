from PyPDF2 import PdfReader
import qrcode

def pdf_to_qrcode(pdf_path, output_path):
    # Read PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        
        # Generate QR codes for each page
        for page_number, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            
            # Create QR code
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(page_text)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")
            
            # Save QR code image
            qr_image.save(f"{output_path}_page{page_number+1}.png")
            
    print(f"QR codes saved successfully.")

# Example usage
pdf_path = 'example.pdf'  # Replace with your PDF file path
output_path = 'output'  # Replace with your desired output path (without file extension)
pdf_to_qrcode(pdf_path, output_path)
