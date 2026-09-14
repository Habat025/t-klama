import flet as ft
import shelve




def main(pencere: ft.Page):

    sayi = 0
    dil = "TR"

    with shelve.open("veri") as db:
        sayi = db.get("sayilar", 0)
        dil = db.get("diller", "TR")

        db.close()

        def guncelle_ve_kaydet():
            nonlocal sayi
            with shelve.open("veri") as db:
                db["sayilar"] = sayi 
                db["diller"] = dil


            pencere.update()


        def arti(e):
            nonlocal sayi
            nonlocal dil

            sayi += 1

            if dil == "TR":

                sayac.value = f"Tıklanan Sayi: {sayi}"

                pencere.update()

            else:
                sayac.value = f"Click Count: {sayi}"

                guncelle_ve_kaydet()
                pencere.update()


        def dil_degistir(e):
            nonlocal dil
            if dil == "TR":
                dil = "EN"
                sayac.value = f"Click Count: {sayi}"
                dilbtn.text = "Langue: EN"
                pencere.update()

            else:
                dil = "TR"
                sayac.value = f"Tıklanan Sayı: {sayi}"
                dilbtn.text = "Dil: TR"
                pencere.update()

            guncelle_ve_kaydet()





    pencere.title = "Tıklama Uygulaması"
    pencere.geometry = "500x800"
    pencere.vertical_alignment = ft.MainAxisAlignment.CENTER
    pencere.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    sayac = ft.Text(f"Tıklanan Sayı: {sayi}")


    artbuton = ft.Button("+1", on_click=arti)

    dilbtn = ft.Button("Dil: TR", on_click=dil_degistir)


    pencere.add(sayac, artbuton, dilbtn)

ft.run(main)
