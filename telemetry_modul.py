#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nama file: telemetry_modul.py
Tujuan program: Modul analisis & klasifikasi data sampel telemetry untuk kantor cabang virtual.
Nama pembuat: Miftahul Fauzan
"""
# Sampel cpuUsage diturunkan dari potongan digit NIM (2409106048) dengan
# variasi, supaya mewakili ketiga kategori klasifikasi:
#   digit ke-1,2   -> "24"  -> 24  (NORMAL)
#   digit ke-6,7,8 -> "060" -> 60  (WASPADA)
#   digit ke-3,4,5 -> "091" -> 91  (KRITIS)
data_telemetry = {
    "router-048-1": 24,
    "switch-048-1": 60,
    "ap-048-1": 91,
}


def klasifikasi_telemetry():
    """Meng-iterasi data_telemetry dan mengklasifikasikan tiap sampel
    cpuUsage: >80 KRITIS, 50-80 WASPADA, <50 NORMAL."""
    hasil = []
    for nama_perangkat, cpu in data_telemetry.items():
        if cpu > 80:
            status = "KRITIS"
        elif cpu >= 50:
            status = "WASPADA"
        else:
            status = "NORMAL"
        print(f"[TELEMETRY] {nama_perangkat}: cpuUsage={cpu}% -> {status}")
        hasil.append({"perangkat": nama_perangkat, "cpu": cpu, "status": status})
    return hasil


if __name__ == "__main__":
    klasifikasi_telemetry()
