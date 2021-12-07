import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import imageio
from cycler import cycler

def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)

    background = photo[480:1030, 1130:1385, 0:3].swapaxes(0, 1)
    
    cut = photo[480:1030, 1170:1350, 0:3].swapaxes(0, 1)
    rgb = np.mean(cut, axis=(0))

    luma = 0.2989 * rgb[:,0] + 0.5866 * rgb[:,1] + 0.1144 * rgb[:,2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.minorticks_on()

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()
    
    plt.imshow(background, origin='lower')
    
    plt.savefig(plotName)

    return luma

def intensites_plot(k, b):
    luma_data = np.zeros((550, 5))

    readIntensity("white-mercury.png", "white-mercury-plot.png", "Ртутная лампа", "белый лист")
    luma_data[:, 0] = (readIntensity("white-tungsten.png", "white-tungsten-plot.png", "Лампа накаливания", "белый лист"))
    luma_data[:, 1] = (readIntensity("red-tungsten.png", "red-tungsten-plot.png", "Лампа накаливания", "красный лист"))
    luma_data[:, 2] = (readIntensity("green-tungsten.png", "green-tungsten-plot.png", "Лампа накаливания", "зеленый лист"))
    luma_data[:, 3] = (readIntensity("blue-tungsten.png", "blue-tungsten-plot.png", "Лампа накаливания", "синий лист"))
    luma_data[:, 4] = (readIntensity("yellow-tungsten.png", "yellow-tungsten-plot.png", "Лампа накаливания", "желтый лист"))

    plt.rc('axes', prop_cycle=(cycler('color', ['w', 'r', 'g', 'b', 'y'])))

    fig, ax = plt.subplots(figsize=(16, 10), dpi=100)

    ax.set_facecolor('lightgrey')
    plt.rcParams.update({'font.size': 18})
    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.title('Отраженная интенсивность лампы накаливания', fontsize=26)
    plt.xlabel('Длина волны, нм', fontsize=20)
    plt.ylabel('Яркость', fontsize=20)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
    ax.grid(which='major', color='black')
    ax.minorticks_on()
    ax.grid(which='minor', color='black', linestyle=':')

    x = np.arange(0, 550, 1)
    x = x * k + b

    plt.axis([340, 750, -5, 80])
    plt.plot(x, luma_data, label=['белый лист', 'красный лист', 'зеленый лист', 'синий лист', 'желтый лист'],
             linewidth=3)
    plt.legend()

    plt.savefig('!intensites.png')

    albedo_plot(luma_data)

def albedo_plot(luma_data):
    k = 0.5962
    b = 371.5

    plt.rc('axes', prop_cycle=(cycler('color', ['w', 'r', 'g', 'b', 'y'])))

    fig, ax = plt.subplots(figsize=(16, 10), dpi=100)

    ax.set_facecolor('lightgrey')
    plt.rcParams.update({'font.size': 18})
    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.title('Альбедо поверхностей', fontsize=26)
    plt.xlabel('Длина волны, нм', fontsize=20)
    plt.ylabel('Альбедо', fontsize=20)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
    ax.grid(which='major', color='black')
    ax.minorticks_on()
    ax.grid(which='minor', color='black', linestyle=':')

    x = np.arange(0, 550, 1)
    x = x * k + b
    y = np.zeros((550, 5))
    y[:,0] = 1
    for i in range(70):
        luma_data[i, 0] += 1
        luma_data[-i, 0] += 1
    for i in range(1,5):
        y[:,i] = luma_data[:,i]/(luma_data[:,0])

    plt.axis([340, 720, -0.05, 1.05])
    plt.plot(x, y, label=['белый лист', 'красный лист', 'зеленый лист', 'синий лист', 'желтый лист'], linewidth=3)
    plt.legend()

    plt.savefig('albedos.png')