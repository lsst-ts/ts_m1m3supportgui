# Python GUI for M1M3 Support System

## Dependencies

Python 3.8
[PySide2 (QtCore, QtGui, QtCharts, QtWidgets)](https://pypi.org/project/PySide2)
[asyncqt](https://pypi.org/project/asyncqt)
[LSST ts_salobj](https://github.com/lsst-ts/ts_salobj)

## Prerequsities

```bash
make_idl_files.py MTM1M3 MTMount
```

## SALComm

Heart of the application is SALComm. The module links ts_salobj callbacks with
Qt Signals. Names of signals matches SAL events and telemetry topics. This
allows for simple integration of DDS/SAL and GUI widgets. Widgets in need to
receive SAL data accept SALComm as constructor parameter, and after setting up
the widget SALComm provided Qt Signals are connected to slots in the widget.

## Custom widgets

Qt Slots are decorated with @Slot and usually not documented, as the only
functions is to update widgets with data received from SAL/DDS. Please see
[PySide2 documentation](https://wiki.qt.io/Qt_for_Python_Signals_and_Slots) and
[SALComm](SALComm.py) for details how this works.
