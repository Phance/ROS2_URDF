import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hance/nirb4600_40/nirb_4600_40_ws/install/nirb4600_40_urdf'
