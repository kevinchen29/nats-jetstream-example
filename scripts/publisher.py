import asyncio
import nats
import pytz
import decimal
import datetime as datetime2
from datetime import datetime
import json
class DateEncoder(json.JSONEncoder):
    """
    自定义类，解决报错：
    TypeError: Object of type "datetime" is not JSON serializable
    """

    def default(self, obj):
        if isinstance(obj, datetime2.datetime):
            return obj.astimezone(pytz.UTC).strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, datetime2.date):
            return obj.astimezone(pytz.UTC).strftime("%Y-%m-%d")
        elif isinstance(obj,decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


async def main():
    print("Connecting to nats")
    #nc = await nats.connect("nats://admintest:admintest@nats:4222")
    nc = await nats.connect("nats://veriid:123qwe@192.168.10.201:4222")
    js = nc.jetstream()

    await js.add_stream(name="ato", subjects=["ato"])

    i = 0
    while True:

        currentDateAndTime = datetime.now()
        input_data = {
        "data_version": "1.0.0",
        "payload":{
            "veriid_trans_id":"ATO_" ,
            "serial_number":  "TEST-1129",
            "diia_serial_number": "TEST_",
            "institute_id": "I999",
            "operator_id": "O001",
            "connector_id": "8909191002",
            "account": {
                "account": "kevin@gmail.com"            
                },
            "device": {
                "udid": "29",
                "hardware_device_type": "Desktop or Laptop",
                "os_name": "macOS",
                "os_version": "10.15"
                },
            "ip": {
                "ip_request": "29.117.43.1",
                "ip_latitude": "1.0127",
                "ip_longitude": "1.4609",
                "ip_is_proxy": "False",
                "ip_is_vpn": "False",
                "ip_is_tor": "False",
                "ip_cloud_server": "False"
            }
        }
    }
        
        ack = await js.publish("ato", json.dumps(input_data, cls=DateEncoder).encode())
        currentDateAndTime = datetime.now()
        print(f'{currentDateAndTime} Ack: stream={ack.stream}, sequence={ack.seq}')
            
        i += 1
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
