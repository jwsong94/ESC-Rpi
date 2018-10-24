from bluepy import btle

# BLUNO MAC TABLE
# ESC_HR : F4:5E:AB:B1:0C:06
# ESC_SY : F4:5E:AB:B0:8B:70
# ESC_JW : F4:5E:AB:B0:8C:A3
# ESC_MH : F4:5E:AB:B1:0C:4A

class ESC_BLE:
    def __init__(self):
        print("ESC_BLE Init");
        self.ble_list = ['f4:5e:ab:b1:0c:06', 'f4:5e:ab:b0:8b:70', 'f4:5e:ab:b0:8c:a3', 'f4:5e:ab:b1:0c:4a'];
        self.dev_list = [];
        self.conn_list = [];
        self.cont_uuid = '0000dfb1-0000-1000-8000-00805f9b34fb';
        self.ble_scan();

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
        for i in (0, 1, 2, 3):
            if self.conn_list[i] != None:
                print(self.ble_list[i] + " : On");
            else:
                print(self.ble_list[i] + " : Off");

    def ble_broadcast(self, data):
        for conn_val in self.conn_list:
            print("send : " + data);
            if conn_val != None:
                conn_val.write(data.encode('utf-8'));


esc = ESC_BLE();

play = True;

while play:
    print("***************************");
    print("*      ESC Controller     *");
    print("***************************");
    print("*  1 : Status             *");
    print("*  2 : Go(Send 1)         *");
    print("*  3 : Reconnect          *");
    print("*  4 : Finish             *");
    print("***************************");
    i = input("* Commend : ");

    if i == '1':
        esc.ble_status();
        '''
        for i in (0, 1, 2, 3):
            if conn_list[i] != None:
                print(ble_list[i] + " : On");
            else:
                print(ble_list[i] + " : Off");
        '''
    elif i == '2':
        esc.ble_broadcast("1");
        '''
        for conn_val in conn_list:
            if conn_val != None:
                #ch = conn_val.getCharacteristics(uuid=cont_uuid)[0];
                #ch.write("1".encode('utf-8'));
                conn_val.write("1".encode('utf-8'));
        '''
    elif i == '3':
        esc.ble_scan();
        '''
        for conn_val in conn_list:
            if conn_val != None:
                #ch = conn_val.getCharacteristics(uuid=cont_uuid)[0];
                #ch.write("0".encode('utf-8'));
                conn_val.write("0".encode('utf-8'));
        '''
    elif i == '4':
        play = False;

'''
print ("Connecting...");
#dev = btle.Peripheral("F4:5E:AB:B1:0C:4A")
dev = btle.Peripheral("F4:5E:AB:B0:8B:70");

print ("Services...");
for svc in dev.services:
    print (str(svc));

print ("Characteristics...");
for ch in dev.getCharacteristics():
    print ("  0x"+ format(ch.getHandle(),'02X')  +"   "+str(ch.uuid) +" " + ch.propertiesToString());

ch = dev.getCharacteristics(uuid='0000dfb1-0000-1000-8000-00805f9b34fb')[0];
ch.write("1".encode('utf-8'))
'''
