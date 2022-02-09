# -*- coding: utf-8 -*-
import os

from astropy.io import fits

from make_convolution_kernel import MakeConvolutionKernel

os.chdir('/Users/williams/Documents/phangs/convolution_kernels')

source_psf = fits.open('PSF_Corrected_IRAC_8.0_added_wing.fits.gz')[0]
target_psf = fits.open('PSF_Corrected_GALEX_FUV_added_wing.fits.gz')[0]

kernel = MakeConvolutionKernel(source_psf=source_psf,
                               # source_fwhm=2.82,
                               source_name='IRAC_8',
                               target_psf=target_psf,
                               # target_fwhm=4.48,
                               target_name='GALEX_FUV'
                               )
kernel.make_convolution_kernel()
kernel.write_out_kernel()

print('Complete')
