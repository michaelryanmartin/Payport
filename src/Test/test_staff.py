import sys
from src.staff import *
from src.main import Anggota

def test_load_produk():
    staffwindow = Staff()
    assert staffwindow.load_produk() == "Load Stok Success"

def test_update_produk():
    staffwindow = Staff()
    assert staffwindow.update_produk() == "Update Stok Success"

def test_input_pesanan():
    staffwindow = Staff()
    staffwindow.ui.labelIDAnggota.setText("7")
    assert staffwindow.buat_pesanan() == "Buat Pesanan Success"
    staffwindow.ui.lineEditPilihProduk.setText("Original Chicken")
    staffwindow.ui.spinBoxKuantitas.setValue(1)
    assert staffwindow.input_produk() == "Input Pesanan Success"

def test_load_transaksi():
    staffwindow = Staff()
    assert staffwindow.load_transaksi() == "Load Transaksi Success"

def test_hitung_promosi():
    staffwindow = Staff()
    staffwindow.ui.comboBox.addItem("12.12")
    staffwindow.totalHargaPesanan = 5000
    staffwindow.hitung_promosi()
    assert staffwindow.discount == 1000

def test_hitung_ppn():
    staffwindow = Staff()
    staffwindow.totalHargaPesanan = 5000
    staffwindow.discount = 1000
    staffwindow.hitung_ppn()
    assert staffwindow.ppn == 400

def test_hitung_total_harga():
    staffwindow = Staff()
    staffwindow.totalHargaPesanan = 5000
    staffwindow.discount = 1000
    staffwindow.ppn = 400
    staffwindow.hitung_totalHarga()
    assert staffwindow.totalHarga == 4400

def test_hitung_kembalian():
    staffwindow = Staff()
    staffwindow.totalHarga = 4400
    staffwindow.ui.lineEditBayar.setText("5000")
    staffwindow.hitung_kembalian()
    assert staffwindow.ui.labelKembalian.text() == "Rp600.00"

def test_bayar_transaksi():
    staffwindow = Staff()
    assert staffwindow.bayar_transaksi() == "Pembayaran Success"

def test_clearData():
    data = Anggota()
    assert data.clearData() == "Clear Data Success"