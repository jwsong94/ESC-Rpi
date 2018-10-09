

import bluetooth

ble_port1 = 1;
ble_port2 = 2;
ble_port3 = 3;
ble_port4 = 4;

# ESC_HR
esc_addr1 = "f4:5e:ab:b1:0c:06"; 
# ESC_SY
esc_addr2 = "f4:5e:ab:b0:8b:70";
# ESC_JW
esc_addr3 = "f4:5e:ab:b0:8c:a3";
# ESC_MH
esc_addr4 = "f4:5e:ab:b1:0c:4a";

print("Bluetooth Test");

sock1=bluetooth.BluetoothSocket( bluetooth.RFCOMM );
sock1.connect((esc_addr3, port3));
print("Connected");

#sock.settimeout(1.0);
#sock.send("Bluetooth Data Sending Start\r\n");

#while True:
#    data = input("Input(x is close) : ");
#    if data=="x":
#        break;
#    sock.send(data);

#data=sock.recv(1)
#print(data);

sock1.close();
print("Disconnected");
print("Finish");
