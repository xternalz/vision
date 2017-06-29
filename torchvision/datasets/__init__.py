from .lsun import LSUN, LSUNClass
from .folder import ImageFolder
from .coco import CocoCaptions, CocoDetection
from .cifar import CIFAR10, CIFAR100, CIFAR10Z, CIFAR100Z
from .stl10 import STL10
from .mnist import MNIST
from .svhn import SVHN
from .phototour import PhotoTour

__all__ = ('LSUN', 'LSUNClass',
           'ImageFolder',
           'CocoCaptions', 'CocoDetection',
           'CIFAR10', 'CIFAR100',
           'CIFAR10Z', 'CIFAR100Z',
           'MNIST', 'STL10', 'SVHN', 'PhotoTour')
