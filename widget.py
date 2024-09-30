from mosaico import widget, config

# Create title
text = widget.createText()
text.setText(config["name"])
text.setHexColor(config["color"])
text.moveTo(2,0)
text.setFont("9x18")

# Create items
items = []
bullets = []
for i in range(0, len(config["items"])):
    # Create bullet
    bullets.append(widget.createRectangle())
    bullets[i].setSize(2,2)        
    bullets[i].moveTo(4,16)
    bullets[i].translateYBy((i*7) + 5)    
    bullets[i].setHexColor(config["color"])  
    
    # Create entry  
    items.append(widget.createText())
    items[i].setFont("4x6")
    items[i].setText(config["items"][i])
    items[i].moveTo(8,14)    
    items[i].translateYBy((i*7) + 5)

def loop():
    pass
