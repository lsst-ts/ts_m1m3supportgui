def updateButton(button, text, action):
    button.setVisible(True)
    button.setText(text)
    button.clicked.disconnect()
    button.clicked.connect(action)

def doNothing():
    pass

def hideButton(button):
    button.setVisible(False)
    button.clicked.disconnect()
    button.clicked.connect(doNothing)

def updateSizePolicy(widget):
    policy = widget.sizePolicy()
    policy.setRetainSizeWhenHidden(True)
    widget.setSizePolicy(policy)

def setBoolLabel(label, trueText, falseText, value):
    text = falseText
    if value:
        text = trueText
    label.setText(text)

def setWarningLabel(label, value):
    setBoolLabel(label, "WARNING", "OK", value)

def setBoolLabelHighLow(label, value):
    setBoolLabel(label, "HIGH", "LOW", value)

def setBoolLabelOnOff(label, value):
    setBoolLabel(label, "ON", "OFF", value)

def setBoolLabelOpenClosed(label, value):
    setBoolLabel(label, "OPEN", "CLOSED", value)

def setBoolLabelYesNo(label, value):
    setBoolLabel(label, "YES", "NO", value)

def getGradientColor(lowest, highest, value):
    # Lowest = Blue
    # Highest = Red
    if value > highest:
        value = highest
    elif value < lowest:
        value = lowest
    range = highest - lowest
    percentage = 1.0
    if range != 0:
        percentage = (-(value - lowest) / range) + 1
    return pg.intColor(int(percentage * 179.0), 255)
