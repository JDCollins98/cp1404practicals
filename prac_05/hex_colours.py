HEX_NAMES = {"burlywood": "#deb887", "chocolate": "#d2691e", "CornflowerBlue": "#6495ed",
             "DarkGreen": "#006400", "DarkKhaki": "#bdb76b", "DarkOrange": "#ff8c00",
             "DarkViolet": "#9400d3", "DimGray" : "#696969","firebrick" : "#b22222",
             "GhostWhite" : "#f8f8ff", "gray" : "#bebebe"}

name = "Init"
while name != "":
    name = input("Enter colour name: ")
    if name in HEX_NAMES:
        print(name, "is", HEX_NAMES[name])
    else:
        print("Invalid colour name")