#!/usr/bin/env python3

# ESC
# Author : Hery Kim, Soyoung Ko, Jungwoo Song
# Contact Us : jwsong417@gmail.com

# FOR BLE
from bluepy import btle

# FOR GPIO
import RPi.GPIO as GPIO
from time import sleep

# FOR UI
from PyQt5 import QtCore, QtGui, QtWidgets

# FOR TIMTER
import threading

class ESC_BLE:
    def __init__(self):
        print("ESC_BLE Init");
        self.ble_list = ['f4:5e:ab:b1:0c:06', 'f4:5e:ab:b0:8b:70', 'f4:5e:ab:b0:8c:a3', 'f4:5e:ab:b1:0c:4a'];
        self.dev_list = [];
        self.conn_list = [];
        self.cont_uuid = '0000dfb1-0000-1000-8000-00805f9b34fb';
        #self.ble_scan();

    def ble_scan(self):
        self.dev_list = [];
        self.conn_list = [];
        scan = btle.Scanner();
        print("Scanning for 5 seconds");
        devs = scan.scan(5);

        for dev in devs:
            self.dev_list.append(dev.addr);

        for dev in self.dev_list:
            print(dev);

        for ble_mac in self.ble_list:
            try:
                print("Try To connect : " + ble_mac);
                if ble_mac in self.dev_list:
                    conn = btle.Peripheral(ble_mac);
                    #conn_list.append(conn);
                    ch = conn.getCharacteristics(uuid=self.cont_uuid)[0];
                    self.conn_list.append(ch);
                else:
                    self.conn_list.append(None);
            except btle.BTLEException as ex:
                self.conn_list.append(None);

    def ble_status(self):
        ble_stat = [0, 0, 0, 0];
        for i in (0, 1, 2, 3):
            if self.conn_list[i] != None:
                ble_stat[i] = 1;
        return ble_stat;

    def ble_broadcast(self, data):
        for conn_val in self.conn_list:
            print("send : " + data);
            if conn_val != None:
                conn_val.write(data.encode('utf-8'));

class ESC_GPIO:
    def __init__(self):
        print("ESC_GPIO Init");
        GPIO.setmode(GPIO.BCM);

        self.OSCIL_SENSOR = 5
        self.FLAME_SENSOR = 6
        self.SMOKE_SENSOR = 13
        self.ESC_LED = 19
        self.ESC_BUTTON = 26

        GPIO.setup(self.OSCIL_SENSOR, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.FLAME_SENSOR, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.SMOKE_SENSOR, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(self.ESC_BUTTON, GPIO.IN, GPIO.PUD_DOWN)

        GPIO.setup(self.ESC_LED, GPIO.OUT, initial=GPIO.LOW)

        self.oscil_stat = 1;
        self.flame_stat = 1;
        self.smoke_stat = 1;
        self.button_stat = 0;

    # Normal : 1 / Oscil : 0
    def check_oscillation(self) :
        self.oscil_stat = GPIO.input(self.OSCIL_SENSOR)

    # Normal : 1 / Flame : 0
    def check_flame(self) :
        self.flame_stat = GPIO.input(self.FLAME_SENSOR)

    # Normal : 1 / Smoke : 0
    def check_smoke(self) :
        self.smoke_stat = GPIO.input(self.SMOKE_SENSOR)

    def check_button(self) :
        self.button_stat = GPIO.input(self.ESC_BUTTON)

    def sensor_status(self) :
        sensor_stat = [1, 1, 1, 0];
        self.check_oscillation();
        self.check_flame();
        self.check_smoke();
        self.check_button();

        sensor_stat[0] = self.oscil_stat;
        sensor_stat[1] = self.flame_stat;
        sensor_stat[2] = self.smoke_stat;
        sensor_stat[3] = self.button_stat;

        return sensor_stat;

    def led_on(self) :
        GPIO.output(self.ESC_LED, GPIO.HIGH);

    def led_off(self) :
        GPIO.output(self.ESC_LED, GPIO.LOW);

class ESC_UI(object):
    def __init__(self):
        print("ESC_UI Init");
        self.esc_gpio = ESC_GPIO();
        self.esc_ble = ESC_BLE();

    def ble_refresh(self):
        self.esc_ble.ble_scan();
        ble_stat = self.esc_ble.ble_status();
        #print('Button Test');
        print(ble_stat);

        if ble_stat[0] == 1:
            self.BLE1S.setStyleSheet("background-color: green;")
        else:
            self.BLE1S.setStyleSheet("background-color: red;")
            
        if ble_stat[1] == 1:
            self.BLE2S.setStyleSheet("background-color: green;")
        else:
            self.BLE2S.setStyleSheet("background-color: red;")

        if ble_stat[2] == 1:
            self.BLE3S.setStyleSheet("background-color: green;")
        else:
            self.BLE3S.setStyleSheet("background-color: red;")

        if ble_stat[3] == 1:
            self.BLE4S.setStyleSheet("background-color: green;")
        else:
            self.BLE4S.setStyleSheet("background-color: red;")

        self.ble_go();
    
    def ble_go(self):
        self.esc_ble.ble_broadcast("1");

    def ble_stop(self):
        self.esc_ble.ble_broadcast("0");
        self.led_off();

    def sensor_timer(self):
        sensor_stat = self.esc_gpio.sensor_status();
        print(sensor_stat);
        
        if sensor_stat[0] == 1:
            self.VibS.setStyleSheet("background-color: green;")
        else:
            self.VibS.setStyleSheet("background-color: red;")
        
        if sensor_stat[1] == 1:
            self.FlameS.setStyleSheet("background-color: green;")
        else:
            self.FlameS.setStyleSheet("background-color: red;")

        if sensor_stat[2] == 1:
            self.GasS.setStyleSheet("background-color: green;")
        else:
            self.GasS.setStyleSheet("background-color: red;")

        if sensor_stat[0]*sensor_stat[1]*sensor_stat[2] == 0:
            print("Warning!!!!");
            if sensor_stat[3] == 1:
                self.led_on();
        
        threading.Timer(1, self.sensor_timer).start();

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)
        self.MView = QtWidgets.QGraphicsView(Frame)
        self.MView.setGeometry(QtCore.QRect(10, 10, 281, 281))
        self.MView.setObjectName("MView")
        self.SLabel = QtWidgets.QLabel(Frame)
        self.SLabel.setGeometry(QtCore.QRect(310, 170, 59, 16))
        self.SLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SLabel.setObjectName("SLabel")
        self.BButton = QtWidgets.QPushButton(Frame)
        self.BButton.setGeometry(QtCore.QRect(300, 10, 91, 31))
        self.BButton.setObjectName("BButton")
        self.BLabel = QtWidgets.QLabel(Frame)
        self.BLabel.setGeometry(QtCore.QRect(310, 40, 61, 16))
        self.BLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BLabel.setObjectName("BLabel")
        self.formLayoutWidget = QtWidgets.QWidget(Frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(300, 60, 91, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.BLETable = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.BLETable.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.BLETable.setFormAlignment(QtCore.Qt.AlignCenter)
        self.BLETable.setContentsMargins(0, 0, 0, 0)
        self.BLETable.setObjectName("BLETable")
        self.BLE1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.BLE1.setObjectName("BLE1")
        self.BLETable.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.BLE1)
        self.BLE1S = QtWidgets.QLabel(self.formLayoutWidget)
        self.BLE1S.setStyleSheet("background-color: red;")
        self.BLE1S.setFrameShadow(QtWidgets.QFrame.Plain)
        self.BLE1S.setObjectName("BLE1S")
        self.BLETable.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.BLE1S)
        self.BLE2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.BLE2.setObjectName("BLE2")
        self.BLETable.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.BLE2)
        self.BLE2S = QtWidgets.QLabel(self.formLayoutWidget)
        self.BLE2S.setStyleSheet("background-color: red;")
        self.BLE2S.setObjectName("BLE2S")
        self.BLETable.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.BLE2S)
        self.BLE3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.BLE3.setObjectName("BLE3")
        self.BLETable.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BLE3)
        self.BLE3S = QtWidgets.QLabel(self.formLayoutWidget)
        self.BLE3S.setStyleSheet("background-color: red;")
        self.BLE3S.setObjectName("BLE3S")
        self.BLETable.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.BLE3S)
        self.BLE4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.BLE4.setObjectName("BLE4")
        self.BLETable.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.BLE4)
        self.BLE4S = QtWidgets.QLabel(self.formLayoutWidget)
        self.BLE4S.setStyleSheet("background-color: red;")
        self.BLE4S.setObjectName("BLE4S")
        self.BLETable.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.BLE4S)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Frame)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(300, 190, 91, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Flame = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Flame.setObjectName("Flame")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Flame)
        self.FlameS = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FlameS.setStyleSheet("background-color: green;")
        self.FlameS.setObjectName("FlameS")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.FlameS)
        self.Gas = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Gas.setObjectName("Gas")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Gas)
        self.GasS = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.GasS.setStyleSheet("background-color: green;")
        self.GasS.setObjectName("GasS")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.GasS)
        self.Vib = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Vib.setObjectName("Vib")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Vib)
        self.VibS = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.VibS.setStyleSheet("background-color: green;")
        self.VibS.setObjectName("VibS")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.VibS)
        self.SButton = QtWidgets.QPushButton(Frame)
        self.SButton.setGeometry(QtCore.QRect(300, 260, 91, 32))
        self.SButton.setObjectName("SButton")

        self.BButton.clicked.connect(self.ble_refresh);
        self.SButton.clicked.connect(self.ble_stop);
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.SLabel.setText(_translate("Frame", "Sensors"))
        self.BButton.setText(_translate("Frame", "Refresh"))
        self.BLabel.setText(_translate("Frame", "BLE Conn"))
        self.BLE1.setText(_translate("Frame", "Patient1"))
        self.BLE1S.setText(_translate("Frame", " "))
        self.BLE2.setText(_translate("Frame", "Patient2"))
        self.BLE2S.setText(_translate("Frame", " "))
        self.BLE3.setText(_translate("Frame", "Patient3"))
        self.BLE3S.setText(_translate("Frame", " "))
        self.BLE4.setText(_translate("Frame", "Patient4"))
        self.BLE4S.setText(_translate("Frame", " "))
        self.Flame.setText(_translate("Frame", "Flame"))
        self.FlameS.setText(_translate("Frame", " "))
        self.Gas.setText(_translate("Frame", "Gas"))
        self.GasS.setText(_translate("Frame", " "))
        self.Vib.setText(_translate("Frame", "Vibra"))
        self.VibS.setText(_translate("Frame", " "))
        self.SButton.setText(_translate("Frame", "Stop"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = ESC_UI()
    ui.setupUi(Frame)
    Frame.show()
    ui.sensor_timer();
    sys.exit(app.exec_())
