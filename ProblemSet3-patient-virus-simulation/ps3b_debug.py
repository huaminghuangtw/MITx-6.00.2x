# precompiled module: https://github.com/Richard-B-UK/MITx-6.00.2x-version-files-for-Python-3.5---3.9
from ps3b_precompiled_38 import *


if __name__ == '__main__':
    simulationWithoutDrug(100, 1000, 0.1, 0.05, 10)
    simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 10)
    # Why set {'guttagonol': False} as guttagonol-resistant? The viruses start off non-resistant; some acquire resistance through mutation.