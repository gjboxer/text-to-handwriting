import pywhatkit as pw
txt=input("Enter text for conversion to handwriting: ")
pw.text_to_handwriting(txt,"result.png",[0,0,138])
print("Conversion Done")