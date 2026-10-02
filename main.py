#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nama file: main.py
Tujuan program: Program utama yang mengintegrasikan modul identitas, SSH, SNMP, NETCONF, dan telemetry 
untuk kantor cabang virtual, lalu mencetak satu laporan akhir gabungan.
Nama pembuat: Miftahul Fauzan
"""
import identitas
import ssh_modul
import snmp_modul
import netconf_modul
import telemetry_modul


class LaporanCabang:
    """Merangkum hasil SSH, SNMP, NETCONF, dan telemetry jadi satu laporan."""

    def __init__(self, nim, nama, kode_cabang):
        self.nim = nim
        self.nama = nama
        self.kode_cabang = kode_cabang

    def tampilkan_laporan(self, hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry):
        print("\n" + "=" * 55)
        print("LAPORAN AKHIR KANTOR CABANG VIRTUAL")
        print("=" * 55)
        print(f"NIM          : {self.nim}")
        print(f"Nama         : {self.nama}")
        print("-" * 55)
        print(f"[SSH]     Status   : {hasil_ssh.get('status')}")
        print(f"[SSH]     Hostname : {hasil_ssh.get('hostname')}")
        print(f"[SNMP]    Status   : {hasil_snmp.get('status')}")
        print(f"[SNMP]    sysName  : {hasil_snmp.get('sysname')}")
        print("-" * 55)
        print("[NETCONF] Pesan edit-config VLAN yang dibuat:")
        print(pesan_netconf)
        print("-" * 55)
        print("[TELEMETRY] Ringkasan klasifikasi:")
        for item in hasil_telemetry:
            print(f"   - {item['perangkat']}: {item['cpu']}% -> {item['status']}")
        print("=" * 55)


def main():
    contoh_id = identitas.buat_id_perangkat("router", 1)
    print(f"[IDENTITAS] Contoh ID perangkat: {contoh_id}\n")

    hasil_ssh = ssh_modul.cek_ssh()
    hasil_snmp = snmp_modul.cek_snmp()
    pesan_netconf = netconf_modul.buat_pesan_netconf()
    hasil_telemetry = telemetry_modul.klasifikasi_telemetry()

    laporan = LaporanCabang(identitas.nim, identitas.nama, identitas.kode_cabang)
    laporan.tampilkan_laporan(hasil_ssh, hasil_snmp, pesan_netconf, hasil_telemetry)


if __name__ == "__main__":
    main()
