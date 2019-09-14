import pandas as pd
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
data = pd.read_excel(dir_path + "/nama_produk.xlsx")
nama = data['nama produk'].tolist()
ganti = data['ganti'].tolist()

dictionary = dict(zip(nama, ganti))
dictionary

def fixNamaBarangAll(ls):
    ls = ls.split(",")
    for i, kt in enumerate(ls):
        ls[i] = ls[i].lstrip()
        kt    = kt.lstrip()
        try:
            ls[i] = dictionary[kt]
        except:
            pass
    return ",".join(ls)

def fixNamaBarang(ls):
    try:
        ls = dictionary[ls]
    except:
        pass
    return ls