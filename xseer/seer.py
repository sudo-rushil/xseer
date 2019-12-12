import os
from astropy.io import fits
import numpy as np
from tensorflow.keras.models import load_model
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = [18, 8]

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
MODEL = load_model(os.path.join(DIR_PATH, 'xseer.h5'))

class Seer():
    def __init__(self, fits_file=None):
        '''
        Opens a FITS file and reads the spectra in the first HDU.
        '''
        assert isinstance(fits_file, str) and fits_file[-5:]=='.fits', "Input is not a valid FITS filename."
        self.file = fits_file
        specdata = fits.open(fits_file)[1].data
        self.loglam, self.flux = self.specdata['loglam'], self.specdata['flux']
        self.specdata.close()

    def denoise(self):
        '''
        Converts the spectra into a 4000-dimensional vector, where the loglam axis ranges from 3.5725 to 3.9725.
        All values that do not exist on the fringes are padded to zero. The loaded model is then used to denoise this vector
        '''
        idx = lambda x : (10000 * np.round(x-3.5725, 4)).astype(np.int32)
        vec = np.zeros(4000, dtype=np.float32)
        i, s = idx(self.loglam)[0], self.loglam.shape[0]
        vec[i:i+s] = self.flux

        output = MODEL(vec.reshape(1, -1, 1)).numpy()

        idxs = np.nonzero(vec)[0]
        lbound, ubound = idxs[0], idxs[-1] + 1
        self.denoised = output[0, lbound:ubound]

    def show(self):
        plt.plot(10**self.loglam, self.flux)
        if self.denoised:
            plt.plot(10**self.loglam, self.denoised)
        plt.grid(True)
        plt.show()

    def save(self, outfile=None):
        if not outfile:
            outfile = '_'.join(['xseer_spec', self.file])

        specdata = 
        self.flux = self.denoised



def test():
    a = np.random.uniform(size=1000)
    plt.plot(a)
    plt.show()