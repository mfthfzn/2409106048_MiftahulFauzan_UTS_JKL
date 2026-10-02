#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nama file: identitas.py
Tujuan program: Berisikan identitas dan Menyediakan function untuk membuat ID perangkat jaringan.
Nama pembuat: Miftahul Fauzan
"""

nim = "2409106048"
nama = "Miftahul Fauzan"
kode_cabang = "048"


def buat_id_perangkat(jenis, nomor):
    return f"{jenis.upper()}-{kode_cabang}-{nomor}"


if __name__ == "__main__":
    print(f"NIM         : {nim}")
    print(f"Nama        : {nama}")
    print(f"Kode Cabang : {kode_cabang}")
    print(f"Contoh ID   : {buat_id_perangkat('router', 1)}")
