from mosaico import widget, config

# Create title
text = widget.createText()
text.setText(config["name"])
text.setHexColor(config["color"])
text.moveTo(3,0)
text.setFont("9x18")

# Create items
items = []
for i in range(0, len(config["items"])):
    items.append(widget.createText())
    items[i].setFont("6x12")
    items[i].setText(config["items"][i])
    items[i].moveTo(4,12)    
    items[i].translateYBy((i*6)+2)

def loop():
    pass