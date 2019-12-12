# XSeer

Deep learning for fast, accurate denoising of astronomical spectra.

# Overview

Xseer uses a denoising autoencoder, a deep learning model, to reconstruct astonomical spectra. It is simple to use, has a clean interface, and is remarkably quick. Its syntax allows for easy integration with Python scripts or Jupyter Notebooks, while the underlying model is extremely powerful at recognizing and eliminating noise.

## Requirements

XSeer is designed for use with Python 3 only. It has the following requirements:

 - Tensorflow 2.x
 - Astropy
 - Numpy
 - Matplotlib

# Installation

To install Xseer, simply use PyPI via pip.

```sh
$ pip install xseer
```

Alternatively, you can clone this directory and install from source.

```sh
$ git clone https://github.com/sudo-rushil/xseer
$ cd xseer
$ python setup.py install
```

Verify your installation by running the following.

```sh
$ python -c "import xseer"
```

If no errors are thrown, you are good to go!

# Example

Say you have a FITS file named `spec-01.fits` in your working directory, and you want to denoise it. Xseer allows you to do this quickly and easily.

```Python
import xseer    # This loads the denoising model from tensorflow into the backend

spectra = xseer.Seer('spec-01.fits')    # This creates a Seer object, which allows the model to perform computations on the spectra

spectra.denoise()   # This applies the denoising model to the spectra, saving the denoised flux vector as an object attribute

spectra.show()  # This plots the original spectra (in blue) and the new, denoised spectra (in orange) for visual comparision
                # It can also be called before denoising, to just plot the original spectra

spectra.save()  # This saves the denoised spectra to a new file. You can specify a filename, but it defaults to saving the spectra
                # to 'xseer_spec_<filename>.fits'
```

# Documentation

Behind the scenes, Xseer uses a four-layer denoising autoencoder to generate denoised spectra. It pads all flux vectors to 4000 units long, with respect to the log-wavelength. It was trained on a set of 300,000 spectra from SDSS DR14. During training, flux vectors were augmented with stochastic gaussian noise before being passed through the autoencoder. The autoencoder is implemented in TensorFlow, with one downsampling layer and two upsampling layers. This model configuration makes the denoising process incredibly fast - denoising each spectra takes, on average 2.51 milliseconds.