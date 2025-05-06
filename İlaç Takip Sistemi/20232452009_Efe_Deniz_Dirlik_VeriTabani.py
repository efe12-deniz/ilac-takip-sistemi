# Ana döngü


import sqlite3 as sql

vtp = sql.connect("ilacStokTakip.sqlite")

imlec = vtp.cursor()

imlec.execute("""
    CREATE TABLE IF NOT EXISTS ilac_Stok_Bilgisi (
        ilaç_Adi TEXT,
        miktar İNT,
        üretim_Tarihi TEXT,
        son_Kullanma_Tarihi TEXT,
        alis_Fiyati İNT,
        satis_Fiyati İNT,
        firma_Adi TEXT
    )
""")
imlec.execute("""
    CREATE TABLE IF NOT EXISTS kullanici_Giris_Bilgisi (
        kullanici_Adi TEXT,
        sifre TEXT
    )
""")

vtp.commit()
vtp.close()