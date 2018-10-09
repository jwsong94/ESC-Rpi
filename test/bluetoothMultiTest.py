

import bluetooth
#from bluetooth import *

ble_port1 = 1;
ble_port2 = 2;
ble_port3 = 3;
ble_port4 = 4;

# ESC_HR
esc_addr1 = "98:D3:31:F5:2D:8E";#"f4:5e:ab:b1:0c:06"; 
# ESC_SY
esc_addr2 = "98:D3:31:F5:2C:9F";#"f4:5e:ab:b0:8b:70";
# ESC_JW
esc_addr3 = "98:D3:31:F7:22:63";#"f4:5e:ab:b0:8c:a3";
# ESC_MH
#esc_addr4 = "98:D3:31:F6:27:70";
esc_addr4 = "F4:5E:AB:B1:0C:4A";

print("Bluetooth Test");

print("Connect To : " + esc_addr1);
sock1=bluetooth.BluetoothSocket( bluetooth.RFCOMM );
sock1.connect((esc_addr1, ble_port1));

print("Connect To : " + esc_addr2);
sock2=bluetooth.BluetoothSocket( bluetooth.RFCOMM );
sock2.connect((esc_addr2, ble_port1));

print("Connect To : " + esc_addr3);
sock3=bluetooth.BluetoothSocket( bluetooth.RFCOMM );
sock3.connect((esc_addr3, ble_port1));

print("Connect To : " + esc_addr4);
sock4=bluetooth.BluetoothSocket( bluetooth.RFCOMM );
sock4.connect((esc_addr4, ble_port1));

print("Connected");

#sock.settimeout(1.0);
#sock.send("Bluetooth Data Sending Start\r\n");

while True:
    data = input("Input(x is close) : ");
    if data=="x":
        break;
    sock1.send(data);
    sock2.send(data);
    sock3.send(data);
    sock4.send(data);

#data=sock.recv(1)
#print(data);

sock1.close();
sock2.close();
sock3.close();
sock4.close();
print("Disconnected");
print("Finish");
