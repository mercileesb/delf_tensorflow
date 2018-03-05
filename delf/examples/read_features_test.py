from delf import feature_io

_DELF_FILE = "./features/ff46f993314efdbf.delf"

data_read = feature_io.ReadFromFile(_DELF_FILE)


print (data_read)

