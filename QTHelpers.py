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
