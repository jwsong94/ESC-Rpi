import tkinter as tk
import bluetooth

ble_list = ["98:D3:31:F7:22:63", "98:D3:31:F5:2D:8E"];
#ble_list = ["98:D3:31:F5:2D:8E"];
ble_conn = []

def ble_connect():
    number=0;
    for ble in ble_list:
        print(ble);
        print(number);
        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM );
        sock.connect((ble, number+1));
        ble_conn.append(sock);
        number = number + 1;
    #for ble in ble_conn:
    #    print(ble);

def ble_disconnect():
    for sock in ble_conn:
        sock.close();

def send1():
    msg="Hello\n";
    sock=ble_conn[0];
    sock.send(msg);
    print(msg);

def send2():
    print("Send to Bluetooth2");

ble_connect();

window = tk.Tk();
frame = tk.Frame(window);
frame.pack();

button1 = tk.Button(frame,
                    text="BLE1",
                    command=send1);
button1.pack(side=tk.LEFT)
button2 = tk.Button(frame,
                    text="BLE2",
                    command=send2);
button2.pack(side=tk.LEFT)


window.mainloop();
ble_disconnect();
