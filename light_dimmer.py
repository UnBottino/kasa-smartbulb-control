import asyncio
import kasa

async def main():
    #await get_devices()
    smart_bulb = kasa.SmartBulb("Device IP")
    await light_dimmer(smart_bulb)

#Find IP of devices
async def get_devices():
    devices = await kasa.Discover.discover()

    for dev in devices.items():
        print(dev)

async def light_dimmer(smart_bulb):
    await smart_bulb.update()
    brightness = smart_bulb.brightness

    print(brightness)
    await asyncio.sleep(0.5)

    await smart_bulb.update()

    match brightness:
        case 25:
            await smart_bulb.set_brightness(50)
        case 50:
            await smart_bulb.set_brightness(25)
        case _:
            await smart_bulb.set_brightness(25)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())