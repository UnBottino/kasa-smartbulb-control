import asyncio
import kasa

async def main():
    #await get_devices()
    smart_bulb = kasa.SmartBulb("Device IP")
    await light_switch(smart_bulb)

#Find IP of devices
async def get_devices():
    devices = await kasa.Discover.discover()

    for dev in devices.items():
        print(dev)

async def light_switch(smart_bulb):
    await smart_bulb.update()

    if smart_bulb.is_on:
        await smart_bulb.turn_off()
    else:
        await smart_bulb.turn_on()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())