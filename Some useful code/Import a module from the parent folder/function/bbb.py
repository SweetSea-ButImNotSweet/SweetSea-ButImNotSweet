import os
import sys

# Lấy đường dẫn của file bbb.py (Get bbb.py's directory)
a = os.path.abspath(__file__)

# Lấy đường dẫn của thư mục function (là nơi chứa file bbb.py)
# (Get function's directory which is contain bbb.py)
b = os.path.dirname(a)

# Lấy đường dẫn nơi của thư mục cha, chính là thư mục nơi
# chứa thư mục function và common
# (Get parent's directory, which is contain function and common)
c = os.path.dirname(b)

# Chuyển thư mục Python đang nhắm sang thư mục cha
# Force Python to change working directory
sys.path.append(c)

from common.aaa import say_hi

say_hi()
