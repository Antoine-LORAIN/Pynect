import pefile
import os

def list_dll_functions(dll_path):
    pe = pefile.PE(dll_path)
    if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            if exp.name:
                print(exp.name.decode('utf-8'))
            else:
                print(f"ordinal{exp.ordinal}")
    else:
        print("No export directory found.")

dll_path = os.path.join(os.environ['SYSTEMROOT'], 'System32', 'Kinect10.dll')
list_dll_functions(dll_path)