#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nama file: ssh_modul.py
Tujuan program: Modul akses jarak jauh via SSH (Paramiko) untuk kantor cabang virtual
Nama pembuat: Miftahul Fauzan
"""
import paramiko
from identitas import kode_cabang

host_vm = "127.0.0.1"
port_ssh_vm = 2222
user_ssh = f"admin_{kode_cabang}"
pass_ssh = "jkl-2026"


def cek_ssh():
    """Login ke VM via SSH dan menjalankan 2 perintah diagnostik."""
    hasil = {"status": "GAGAL", "hostname": None, "uptime": None}
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host_vm, port=port_ssh_vm, username=user_ssh,
                        password=pass_ssh, timeout=5)

        stdin, stdout, stderr = client.exec_command("hostname")
        hostname = stdout.read().decode().strip()

        stdin, stdout, stderr = client.exec_command("uptime")
        uptime = stdout.read().decode().strip()

        print(f"[SSH] hostname: {hostname}")
        print(f"[SSH] uptime  : {uptime}")

        client.close()
        hasil = {"status": "OK", "hostname": hostname, "uptime": uptime}
    except Exception as e:
        print(f"[SSH] GAGAL: {e}")
        hasil["error"] = str(e)
    return hasil


if __name__ == "__main__":
    cek_ssh()
