import asyncio
import nats
from datetime import datetime
import time
async def main():
    print("Connecting to nats")
    #nc = await nats.connect("nats://admintest:admintest@nats:4222")
    nc = await nats.connect("nats://veriid:123qwe@192.168.10.201:4222")
    js = nc.jetstream()
    sub = await js.subscribe(subject="ato")

    while True:
        try:
            currentDateAndTime = datetime.now()
            msg = await asyncio.wait_for(sub.next_msg(), timeout=None)
            print(f"{currentDateAndTime}_Received a message on '{msg.subject}': {msg.data.decode()}")
            await msg.ack_sync()
        except asyncio.TimeoutError:
            time.sleep(0.01)


if __name__ == '__main__':
    asyncio.run(main())
