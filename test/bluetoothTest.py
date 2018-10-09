

import bluetooth

#bd_addr = "98:D3:31:F7:22:63";
bd_addr = "98:D3:31:F5:2C:9F";
#bd_addr = "98:D3:31:F5:2D:8E";
port = 1;

print("Bluetooth Test");

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print("Connected");

#sock.settimeout(1.0);
sock.send("Bluetooth Data Sending Start\r\n");

while True:
    data = input("Input(x is close) : ");
    if data=="x":
        break;
    sock.send(data);

#data=sock.recv(1)
#print(data);

sock.close();
print("Disconnected");
print("Finish");
