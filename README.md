# Ujian Tengah Semester Mata Kuliah Jaringan Komputer Lanjut

Integrasi SSH, SNMP, NETCONF, dan Telemetry menggunakan Python untuk simulasi kantor cabang virtual.

**Nama:** Miftahul Fauzan
**NIM:** 2409106048

## Struktur Project
- `identitas.py` — identitas kantor cabang & fungsi pembuat ID perangkat
- `ssh_modul.py` — koneksi & diagnostik jarak jauh via SSH (Paramiko)
- `snmp_modul.py` — monitoring perangkat via SNMP (PySNMP)
- `netconf_modul.py` — pembuatan pesan NETCONF edit-config untuk VLAN
- `telemetry_modul.py` — analisis & klasifikasi data sampel telemetry
- `main.py` — mengintegrasikan seluruh modul dan mencetak laporan akhir
- `.gitignore` — mengecualikan venv/, __pycache__/, dan file log/backup hasil eksekusi

## Cara Menjalankan (Windows)

1. Buat virtual environment dan install dependensi:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install paramiko "pysnmp==4.4.12" "pyasn1==0.4.8" pyasyncore pyasynchat
   ```
2. Pastikan VM (SSH & SNMP) sudah menyala dan port forwarding aktif.
3. Jalankan program utama:
   ```bash
   python main.py
   ```

## Ringkasan Personalisasi
Seluruh nilai personalisasi diturunkan dari NIM mahasiswa sesuai ketentuan tugas:
- Username SSH mengikuti pola `admin_<kode_cabang>`
- Community string SNMP mengikuti pola `comm_<kode_cabang>`
- VLAN ID pada modul NETCONF menggunakan angka dari kode_cabang secara langsung
- Sampel data telemetry diambil dari potongan digit NIM dengan variasi,
  disusun agar mewakili ketiga kategori klasifikasi (NORMAL, WASPADA, KRITIS)
