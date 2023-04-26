import pyqrcode
import png
from pyqrcode import QRCode
s="www.instagram.com"
url=pyqrcode.create(s)
url.png('instagramqr',scale=6)