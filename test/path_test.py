import sys, os
ANSIBLE_WS_PATH_TEST = os.path.dirname(os.path.realpath(__file__))
ANSIBLE_WS_PATH_ROOT = os.path.dirname(ANSIBLE_WS_PATH_TEST)
ANSIBLE_WS_PATH_LIB = os.path.join(ANSIBLE_WS_PATH_ROOT, 'lib')
sys.path.append(ANSIBLE_WS_PATH_LIB)
