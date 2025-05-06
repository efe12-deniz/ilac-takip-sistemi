
import sqlite3 as sql

from idlelib.configdialog import font_sample_text
from tkinter import *
from tkinter import messagebox, ttk






def pencere_ortala(pencere, genislik, yukseklik):
    ekran_genislik = pencere.winfo_screenwidth()
    ekran_yukseklik = pencere.winfo_screenheight()
    x = (ekran_genislik - genislik) // 2
    y = (ekran_yukseklik - yukseklik) // 2
    pencere.geometry(f"{genislik}x{yukseklik}+{x}+{y}")


giris = Tk()
giris.title("İlaç Takip Sistemi - Giriş")
pencere_ortala(giris, 400, 200)
giris.maxsize(400,200)
giris.minsize(400,200)



def anasayfaGecis():
    # Ana Sayfa
    anasayfa = Toplevel()
    anasayfa.title("Anasayfa")
    anasayfa.state("zoomed")
    anasayfa.configure(bg="lightblue")
    # Alt pencereleri takip için bir liste
    alt_pencereler = []

    def alt_pencere_kapat():
        """Ana sayfa kapatıldığında tüm alt pencereleri kapat."""
        for pencere in alt_pencereler:
            try:
                pencere.destroy()
            except:
                pass
        anasayfa.destroy()

    # Ana pencereyi kapatırken alt pencereleri de kapatmak için
    anasayfa.protocol("WM_DELETE_WINDOW", alt_pencere_kapat)


    def eklesayfaGecis():
        eklesayfa = Toplevel()
        eklesayfa.title("İlaç Ekleme")
        eklesayfa.geometry("500x720+3+270")
        eklesayfa.attributes("-topmost", 1)
        alt_pencereler.append(eklesayfa)  # Alt pencereyi listeye ekleyin

        uyarıLabel = Label(eklesayfa, text="! Bilgileri Dikkatli ve Doğru Giriniz !", font=("Arial", 16))
        uyarıLabel.grid(row=0, column=0, columnspan=2, pady=40)


        adLabel = Label(eklesayfa, text="İlaç Adı : ", font=("Arial", 12))
        adLabel.grid(row=1, column=0, padx=10, pady=20, sticky="w")
        adEntry = Entry(eklesayfa, width=40)
        adEntry.grid(row=1, column=1, padx=10, pady=20)

        miktarLabel = Label(eklesayfa, text="Adet : ", font=("Arial", 12))
        miktarLabel.grid(row=2, column=0, padx=10, pady=20, sticky="w")
        miktarEntry = Entry(eklesayfa, width=40)
        miktarEntry.grid(row=2, column=1, padx=10, pady=20)

        ütLabel = Label(eklesayfa, text="Üretim Tarihi : ", font=("Arial", 12))
        ütLabel.grid(row=3, column=0, padx=10, pady=20, sticky="w")
        ütEntry = Entry(eklesayfa, width=40)
        ütEntry.grid(row=3, column=1, padx=10, pady=20)

        sktLabel = Label(eklesayfa, text="Son Kullanım Tarihi : ", font=("Arial", 12))
        sktLabel.grid(row=4, column=0, padx=10, pady=20, sticky="w")
        sktEntry = Entry(eklesayfa, width=40)
        sktEntry.grid(row=4, column=1, padx=10, pady=20)

        alisfiyatLabel = Label(eklesayfa, text="Alış Fiyatı : ", font=("Arial", 12))
        alisfiyatLabel.grid(row=5, column=0, padx=10, pady=20, sticky="w")
        alisfiyatEntry = Entry(eklesayfa, width=40)
        alisfiyatEntry.grid(row=5, column=1, padx=10, pady=20)

        fiyatLabel = Label(eklesayfa, text="Satış Fiyatı : ", font=("Arial", 12))
        fiyatLabel.grid(row=6, column=0, padx=10, pady=20, sticky="w")
        fiyatEntry = Entry(eklesayfa, width=40)
        fiyatEntry.grid(row=6, column=1, padx=10, pady=20)

        firmaLabel = Label(eklesayfa, text="Firma Adı : ", font=("Arial", 12))
        firmaLabel.grid(row=7, column=0, padx=10, pady=20, sticky="w")
        firmaEntry = Entry(eklesayfa, width=40)
        firmaEntry.grid(row=7, column=1, padx=10, pady=20)




        # Kayıt Etme İşlevi
        def veritabanina_kaydet():
            ilac_adi = adEntry.get()
            miktar = miktarEntry.get()
            uretim_tarihi = ütEntry.get()
            son_kullanma_tarihi = sktEntry.get()
            alis_fiyati = alisfiyatEntry.get()
            satis_fiyati = fiyatEntry.get()
            firma_adi = firmaEntry.get()


            if not (
                    ilac_adi and miktar and uretim_tarihi and son_kullanma_tarihi and alis_fiyati and satis_fiyati and firma_adi):
                messagebox.showerror("Hata", "Tüm alanları doldurunuz!")
                return

            try:
                # Veri tabanı bağlantısı
                vtp = sql.connect("ilacStokTakip.sqlite")
                imlec = vtp.cursor()
                imlec.execute("""
                    INSERT INTO ilac_Stok_Bilgisi (ilaç_Adi, miktar, üretim_Tarihi, son_Kullanma_Tarihi, alis_Fiyati, satis_Fiyati, firma_Adi)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (ilac_adi, miktar, uretim_tarihi, son_kullanma_tarihi, alis_fiyati, satis_fiyati, firma_adi))
                vtp.commit()
                vtp.close()
                messagebox.showinfo("Başarılı", "İlaç başarıyla kaydedildi!")
            except Exception as e:
                messagebox.showerror("Hata", f"Bir hata oluştu: {e}")


        kaydetButon = Button(eklesayfa, text="Ekle", font=("Arial", 12), bg="gray", fg="white", width=10, height=2, command=veritabanina_kaydet)
        kaydetButon.grid(row=8, column=1, pady=10, sticky="e")

    ekleButon = Button(anasayfa, text="İlaç Ekle", font=("Arial", 12), bg="gray", fg="white", width=20, height=5, command=eklesayfaGecis)
    ekleButon.grid(row=0, column=0, padx=10, pady=10)

    def silsayfaGecis():
        silsayfa = Toplevel()
        silsayfa.title("İlaç Satış")
        silsayfa.geometry("550x462+510+30")
        silsayfa.attributes("-topmost", 1)
        alt_pencereler.append(silsayfa)  # Alt pencereyi listeye ekleyin

        adLabel = Label(silsayfa, text="İlaç Adı : ", font=("Arial", 12))
        adLabel.grid(row=1, column=0, padx=10, pady=20, sticky="w")
        adEntry = Entry(silsayfa, width=40)
        adEntry.grid(row=1, column=1, padx=10, pady=20)

        miktarLabel = Label(silsayfa, text="Adet : ", font=("Arial", 12))
        miktarLabel.grid(row=2, column=0, padx=10, pady=20, sticky="w")
        miktarEntry = Entry(silsayfa, width=40)
        miktarEntry.grid(row=2, column=1, padx=10, pady=20)

        # Veritabanından Silme İşlevi
        def veritabanindan_sil():
            ilac_adi = adEntry.get()
            miktar = miktarEntry.get()


            if not ilac_adi or not miktar:
                messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz!")
                return

            try:
                miktar = int(miktar)
                # Veri tabanı bağlantısı
                vtp = sql.connect("ilacStokTakip.sqlite")
                imlec = vtp.cursor()

                # Son kullanım tarihi en yakın olan kaydı bul
                imlec.execute("""
                    SELECT son_Kullanma_Tarihi, miktar, üretim_Tarihi FROM ilac_Stok_Bilgisi
                    WHERE ilaç_Adi = ?
                    ORDER BY son_Kullanma_Tarihi ASC LIMIT 1
                """, (ilac_adi,))
                kayit = imlec.fetchone()

                if kayit is None:
                    messagebox.showerror("Hata", "Bu isimde bir ilaç bulunamadı!")
                elif kayit[1] < miktar:
                    messagebox.showerror("Hata", "Stokta yeterli miktar bulunmamaktadır!")
                else:
                    # Güncelleme veya silme işlemi
                    yeni_miktar = kayit[1] - miktar
                    son_kullanma_tarihi = kayit[0]
                    uretim_tarihi = kayit[2]

                    if yeni_miktar == 0:
                        imlec.execute("""
                            DELETE FROM ilac_Stok_Bilgisi 
                            WHERE ilaç_Adi = ? AND son_Kullanma_Tarihi = ? AND üretim_Tarihi = ?
                        """, (ilac_adi, son_kullanma_tarihi, uretim_tarihi))
                    else:
                        imlec.execute("""
                            UPDATE ilac_Stok_Bilgisi
                            SET miktar = ?
                            WHERE ilaç_Adi = ? AND son_Kullanma_Tarihi = ? AND üretim_Tarihi = ?
                        """, (yeni_miktar, ilac_adi, son_kullanma_tarihi, uretim_tarihi))

                    vtp.commit()
                    messagebox.showinfo("Başarılı", "Satış işlemi başarıyla gerçekleşti!")

                vtp.close()

            except ValueError:
                messagebox.showerror("Hata", "Adet bilgisi sayısal bir değer olmalıdır!")
            except Exception as e:
                messagebox.showerror("Hata", f"Bir hata oluştu: {e}")


        silButon = Button(silsayfa, text="Sat", font=("Arial", 12), bg="gray", fg="white", width=10, height=2,command=veritabanindan_sil)
        silButon.grid(row=3, column=1, pady=10, sticky="e")

    silButon = Button(anasayfa, text="Satış", font=("Arial", 12), bg="gray", fg="white", width=20, height=5, command=silsayfaGecis)
    silButon.grid(row=0, column=1, padx=10, pady=10)

    def guncellesayfaGecis():
        guncellesayfa = Toplevel()
        guncellesayfa.title("İlaç Satış Güncelleme")
        guncellesayfa.geometry("550x462+510+528")
        guncellesayfa.attributes("-topmost", 1)
        alt_pencereler.append(guncellesayfa)  # Alt pencereyi listeye ekleyin

        # İlaç Adı
        adLabel = Label(guncellesayfa, text="İlaç Adı : ", font=("Arial", 12))
        adLabel.grid(row=0, column=0, padx=10, pady=20, sticky="w")
        adEntry = Entry(guncellesayfa, width=40)
        adEntry.grid(row=0, column=1, padx=10, pady=20)

        # Yeni Alış Fiyatı
        alisfiyatLabel = Label(guncellesayfa, text="Yeni Alış Fiyatı : ", font=("Arial", 12))
        alisfiyatLabel.grid(row=1, column=0, padx=10, pady=20, sticky="w")
        alisfiyatEntry = Entry(guncellesayfa, width=40)
        alisfiyatEntry.grid(row=1, column=1, padx=10, pady=20)

        # Yeni Satış Fiyatı
        fiyatLabel = Label(guncellesayfa, text="Yeni Satış Fiyatı : ", font=("Arial", 12))
        fiyatLabel.grid(row=2, column=0, padx=10, pady=20, sticky="w")
        fiyatEntry = Entry(guncellesayfa, width=40)
        fiyatEntry.grid(row=2, column=1, padx=10, pady=20)

        # Fiyatları Güncelleme İşlevi
        def fiyatlari_guncelle():
            ilac_adi = adEntry.get()
            yeni_alis_fiyati = alisfiyatEntry.get()
            yeni_satis_fiyati = fiyatEntry.get()


            if not (ilac_adi and yeni_alis_fiyati and yeni_satis_fiyati):
                messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz!")
                return

            try:
                yeni_alis_fiyati = float(yeni_alis_fiyati)
                yeni_satis_fiyati = float(yeni_satis_fiyati)

                # Veri tabanı bağlantısı
                vtp = sql.connect("ilacStokTakip.sqlite")
                imlec = vtp.cursor()

                # İlaç adı ile eşleşen tüm kayıtları güncelle
                imlec.execute("""
                    UPDATE ilac_Stok_Bilgisi
                    SET alis_Fiyati = ?, satis_Fiyati = ?
                    WHERE ilaç_Adi = ?
                """, (yeni_alis_fiyati, yeni_satis_fiyati, ilac_adi))

                vtp.commit()
                etkilenen_satirlar = imlec.rowcount  # Güncellenen satır sayısı
                vtp.close()

                if etkilenen_satirlar > 0:
                    messagebox.showinfo("Başarılı", f"{etkilenen_satirlar} kayıt başarıyla güncellendi!")
                else:
                    messagebox.showwarning("Uyarı", "Bu isimde bir ilaç bulunamadı!")

                guncellesayfa.destroy()

            except ValueError:
                messagebox.showerror("Hata", "Fiyat bilgileri sayısal bir değer olmalıdır!")
            except Exception as e:
                messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

        # Güncelle Butonu
        kaydetButon = Button(guncellesayfa, text="Güncelle", font=("Arial", 12), bg="gray", fg="white", width=10,
                             height=2,
                             command=fiyatlari_guncelle)
        kaydetButon.grid(row=3, column=1, pady=20, sticky="e")

    guncellerButon = Button(anasayfa, text="Fiyat Güncelleme", font=("Arial", 12), bg="gray", fg="white", width=20, height=5, command=guncellesayfaGecis)
    guncellerButon.grid(row=1, column=0, padx=10, pady=10)

    def listelesayfaGecis():
        listelesayfa = Toplevel()
        listelesayfa.title("Kayıt Listeleme")
        listelesayfa.geometry("838x959+1068+30")
        listelesayfa.attributes("-topmost", 1)
        alt_pencereler.append(listelesayfa)  # Alt pencereyi listeye ekleyin

        # Treeview Widget'ı için stil ayarları
        style = ttk.Style(listelesayfa)
        style.theme_use("default")
        style.configure("Treeview",
                        rowheight=25,  # Satır yüksekliği
                        borderwidth=1,
                        relief="solid")  # Çizgiler için stil
        style.map("Treeview", background=[("selected", "lightblue")])  # Seçim stili

        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

        # Treeview Widget'ı için Başlıklar
        columns = (
        "ilaç_Adi", "miktar", "üretim_Tarihi", "son_Kullanma_Tarihi", "alis_Fiyati", "satis_Fiyati", "firma_Adi")

        tree = ttk.Treeview(listelesayfa, columns=columns, show="headings", height=35)
        tree.grid(row=0, column=0, sticky="nsew")

        # Başlıklar Tanımlanır
        tree.heading("ilaç_Adi", text="İlaç Adı")
        tree.heading("miktar", text="Miktar")
        tree.heading("üretim_Tarihi", text="Üretim Tarihi")
        tree.heading("son_Kullanma_Tarihi", text="Son Kullanma Tarihi")
        tree.heading("alis_Fiyati", text="Alış Fiyatı")
        tree.heading("satis_Fiyati", text="Satış Fiyatı")
        tree.heading("firma_Adi", text="Firma Adı")

        # Sütun Genişlikleri
        tree.column("ilaç_Adi", width=120)
        tree.column("miktar", width=80)
        tree.column("üretim_Tarihi", width=120)
        tree.column("son_Kullanma_Tarihi", width=160)
        tree.column("alis_Fiyati", width=100)
        tree.column("satis_Fiyati", width=100)
        tree.column("firma_Adi", width=150)

        # Kaydırma Çubuğu
        scrollbar = Scrollbar(listelesayfa, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        def tabloyu_yenile():
            # Eski verileri temizle
            for item in tree.get_children():
                tree.delete(item)

            # Yeni verileri yükle
            try:
                vtp = sql.connect("ilacStokTakip.sqlite")
                imlec = vtp.cursor()
                imlec.execute("SELECT * FROM ilac_Stok_Bilgisi")
                rows = imlec.fetchall()

                # Verileri Treeview'a ekle
                for row in rows:
                    tree.insert("", END, values=row)

                vtp.close()
            except Exception as e:
                messagebox.showerror("Hata", f"Veriler yüklenirken bir hata oluştu: {e}")

        # İlk veri yüklemesi
        tabloyu_yenile()


        yenileButton = Button(listelesayfa, text="Yenile", font=("Arial", 12), bg="gray", fg="lightblue", width=10, height=2,command=tabloyu_yenile)
        yenileButton.grid(row=1, column=0, pady=10, )

    listeButon = Button(anasayfa, text="Listele", font=("Arial", 12), bg="gray", fg="white", width=20, height=5, command=listelesayfaGecis)
    listeButon.grid(row=1, column=1, padx=10, pady=10)




def kayitSayfaGecis():
    kayitsayfa = Toplevel()
    kayitsayfa.title("Kayıt Sayfası")
    pencere_ortala(kayitsayfa, 400, 200)
    kayitsayfa.maxsize(400, 200)
    kayitsayfa.minsize(400, 200)

    kullaniciAdLabel = Label(kayitsayfa, text="Kullanıcı Adı:", font=("Arial", 12))
    kullaniciAdLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    kullaniciAdEntry = Entry(kayitsayfa, width=30)
    kullaniciAdEntry.grid(row=0, column=1, padx=10, pady=10)

    # Şifre
    sifreLabel = Label(kayitsayfa, text="Şifre:", font=("Arial", 12))
    sifreLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    sifreEntry = Entry(kayitsayfa, width=30, show="*")
    sifreEntry.grid(row=1, column=1, padx=10, pady=10)

    # Kayıt Etme İşlevi
    def kullanici_kaydet():
        kullanici_adi = kullaniciAdEntry.get()
        sifre = sifreEntry.get()

        if not (kullanici_adi and sifre):
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz!")
            return

        try:
            # Veri tabanı bağlantısı
            vtp = sql.connect("ilacStokTakip.sqlite")
            imlec = vtp.cursor()

            # Kullanıcı bilgilerini kaydet
            imlec.execute("""
                INSERT INTO kullanici_Giris_Bilgisi (kullanici_Adi, sifre)
                VALUES (?, ?)
            """, (kullanici_adi, sifre))

            vtp.commit()
            vtp.close()

            messagebox.showinfo("Başarılı", "Kullanıcı başarıyla kaydedildi!")
            kayitsayfa.destroy()

        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {e}")

    # Kayıt Ol Butonu
    kayitButton = Button(kayitsayfa, text="Kayıt Ol", font=("Arial", 12), bg="gray", fg="white", width=10,
                         command=kullanici_kaydet)
    kayitButton.grid(row=3, column=1, padx=10, pady=5)


def girisYap():
    kullanici_adi = kullaniciAdEntry.get()
    sifre = sifreEntry.get()


    if not (kullanici_adi and sifre):
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurunuz!")
        return

    try:
        # Veri tabanı bağlantısı
        vtp = sql.connect("ilacStokTakip.sqlite")
        imlec = vtp.cursor()

        # Kullanıcı adı ve şifre kontrolü
        imlec.execute("""
            SELECT * FROM kullanici_Giris_Bilgisi
            WHERE kullanici_Adi = ? AND sifre = ?
        """, (kullanici_adi, sifre))

        sonuc = imlec.fetchone()
        vtp.close()

        if sonuc:
            messagebox.showinfo("Başarılı", "Giriş başarılı!")
            anasayfaGecis()  # Anasayfaya geçiş yap
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı!")

    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {e}")





kullaniciAdLabel = Label(giris, text="Kullanıcı Adı :", font=("Arial", 12))
kullaniciAdLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

kullaniciAdEntry = Entry(giris, width=30)
kullaniciAdEntry.grid(row=0, column=1, padx=10, pady=10)


sifreLabel = Label(giris, text="Şifre :", font=("Arial", 12))
sifreLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")

sifreEntry = Entry(giris, width=30, show="*")
sifreEntry.grid(row=1, column=1, padx=10, pady=10)


girisButton = Button(giris, text="Giriş Yap", font=("Arial", 12), bg="blue", fg="white", width=10, command=girisYap)
girisButton.grid(row=2, column=1, padx=10, pady=5)



kayitButton = Button(giris, text="Kayıt Ol", font=("Arial", 12), bg="gray", fg="white", width=10, command=kayitSayfaGecis)
kayitButton.grid(row=3, column=1, padx=10, pady=5)

giris.mainloop()