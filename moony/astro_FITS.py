# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits


############
# 성운 이미지 불러오기
image_data = fits.open("C:/Users/llaum/Desktop/hlsp_heritage_hst_acs-wfc_m51_f814w_v1_drz_sci.fits")
image_data.info()

data = image_data[0].data
header = image_data[0].header

image = np.array(data)

max_value = np.percentile(image,99.8)
min_value = np.percentile(image,15)     # 밝기조절

plt.figure(figsize=(8,6))
plt.imshow(image, cmap="gray", vmax= max_value, vmin= min_value, origin="lower")
plt.xlim(1050,7000)
plt.ylim(3000, 8000)
plt.show()
#############
# 성운 이미지를 광도곡선으로 나타내기
# image_data = fits.open("C:/Users/llaum/Desktop/hlsp_heritage_hst_acs-wfc_m51_f814w_v1_drz_sci.fits")
# data = image_data[0].data
# header = image_data[0].header
#
# specdata = fits.open('hlsp_heritage_hst_acs-wfc_m51_f814w_v1_drz_sci.fits')
# specdata.info()
#
# spectrum = specdata[1].data
# header = specdata[1].header
# print(header)
#
# flux = []
# loglam = []
#
# for i in range(len(spectrum)):
    # flux.append(spectrum[i][0])
    # loglam.append(spectrum[i][1])
    #
# flux = np.array(flux)
# lam = 10**np.array(loglam)
# plt.figure(figsize=(10,7))
# plt.plot(lam,flux,c='black')
# plt.title('Spectrum lines of NGC 5334', fontsize=20)
# plt.xlabel('Wavelength (Angstroms)', fontsize=15)
# plt.ylabel('Flux', fontsize=15)
# plt.axvspan(5520,5650,facecolor='r', alpha=0.5)
