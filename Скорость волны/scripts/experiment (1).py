import spidev
import time
import matplotlib.pyplot as plt
import waveFunctions as wave

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1600000


def getAdc():
    adcResponse = spi.xfer2([0, 0])
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1


try:

    data = []
    count = 0

    wave.waitForOpen()

    start = time.time()

    while (time.time() - start < 15):
        data.append(getAdc())
        count = count + 1

    wave.saveMeasures(data, count, 1, start, time.time())

    plt.plot(data)
    plt.show()


finally:
    spi.close()