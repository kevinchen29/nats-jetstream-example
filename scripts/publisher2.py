import asyncio
import nats
from datetime import datetime

async def main():
    print("Connecting to nats")
    #nc = await nats.connect("nats://admintest:admintest@nats:4222")
    nc = await nats.connect("nats://veriid:123qwe@192.168.10.201:4222")
    js = nc.jetstream()

    await js.add_stream(name="fd", subjects=["fd"])
    i = 0
    while True:

        currentDateAndTime = datetime.now()
        ack2 = await js.publish("fd", f'Hello fd! {i}_{currentDateAndTime}'.encode())
        currentDateAndTime = datetime.now()
        print(f'{currentDateAndTime} Ack2: stream={ack2.stream}, sequence={ack2.seq}')
            
        i += 1
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
