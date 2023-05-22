import qrcode


def generate_contact_qr_code(name, phone, email):
    contact_details = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(contact_details)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img.save("contact_qr_code.png")


# Example usage
name = "Gnani Pasupula"
phone = "8096xxxxxx"
email = "gnanipasupula@gmail.com"

generate_contact_qr_code(name, phone, email)
