import sys
from src.owner import *

def test_add_anggota():
    ownerwindow = Owner()
    ownerwindow.ui.lineEditNamaAnggota.setText(" ")
    assert ownerwindow.add_anggota() == "Add Data Anggota Success"

def test_update_anggota():
    ownerwindow = Owner()
    ownerwindow.ui.lineEditNamaAnggota.setText(" ")
    assert ownerwindow.update_anggota() == "Update Data Anggota Success"

def test_delete_anggota():
    ownerwindow = Owner()
    ownerwindow.ui.lineEditNamaAnggota.setText(" ")
    assert ownerwindow.delete_anggota() == "Delete Data Anggota Success"

def test_add_produk():
    ownerwindow = Owner()
    ownerwindow.ui.lineEditNamaProduk.setText("test")
    ownerwindow.ui.lineEditDeskripsi.setText("test")
    ownerwindow.ui.lineEditHarga.setText("0")
    ownerwindow.ui.lineEditStok.setText("0")
    assert ownerwindow.add_produk() == "Add Data Produk Success"

def test_update_produk():
    ownerwindow = Owner()
    ownerwindow.ui.lineEditNamaProduk.setText("test")
    ownerwindow.ui.lineEditDeskripsi.setText("test")
    ownerwindow.ui.lineEditHarga.setText("0")
    ownerwindow.ui.lineEditStok.setText("0")
    assert ownerwindow.update_produk() == "Update Data Produk Success"

def test_delete_produk():
    ownerwindow = Owner()
    ownerwindow.ui.lineEditNamaProduk.setText("test")
    ownerwindow.ui.lineEditDeskripsi.setText("test")
    ownerwindow.ui.lineEditHarga.setText("0")
    ownerwindow.ui.lineEditStok.setText("0")
    assert ownerwindow.delete_produk() == "Delete Data Produk Success"

def test_add_promosi():
    ownerwindow = Owner()
    ownerwindow.ui.lineEditNamaPromosi.setText("test")
    ownerwindow.ui.lineEditJumlahPromosi.setText("0")
    assert ownerwindow.add_promosi() == "Add Data Promosi Success"

def test_update_promosi():
    ownerwindow = Owner()
    ownerwindow.ui.lineEditNamaPromosi.setText("test")
    ownerwindow.ui.lineEditJumlahPromosi.setText("0")
    assert ownerwindow.update_promosi() == "Update Data Promosi Success"

def test_delete_promosi():
    ownerwindow = Owner()
    ownerwindow.ui.lineEditNamaPromosi.setText("test")
    ownerwindow.ui.lineEditJumlahPromosi.setText("0")
    assert ownerwindow.delete_promosi() == "Delete Data Promosi Success"

def test_laporan_bulanan():
    ownerwindow = Owner()
    assert ownerwindow.laporan_bulanan() == "Laporan Bulanan Success"

def test_laporan_harian():
    ownerwindow = Owner()
    assert ownerwindow.laporan_harian() == "Laporan Harian Success"

