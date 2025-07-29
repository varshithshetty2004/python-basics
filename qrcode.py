import qrcode
a = qrcode.QRCode()
text_mg = "hi students you are well disiplined "
a.add_data(text_mg)
a.make(fit = True)
varshith = a.make_image(fill_color="black",black_color="white")
varshith.save("varsh.png")
print("saved!")
