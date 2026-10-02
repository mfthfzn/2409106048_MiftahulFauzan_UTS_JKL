#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Nama file: snmp_modul.py
Tujuan program: Modul monitoring perangkat via SNMP (PySNMP) untuk kantor cabang virtual.
Nama pembuat: Miftahul Fauzan
"""
import importlib.util
import importlib.machinery
from pysnmp.hlapi import (
    SnmpEngine, CommunityData, UdpTransportTarget, ContextData,
    ObjectType, ObjectIdentity, getCmd
)
from identitas import kode_cabang

host_vm = "127.0.0.1"
port_snmp_vm = 1161
community = f"comm_{kode_cabang}"


def cek_snmp():
    """Mengambil nilai sysName (OID 1.3.6.1.2.1.1.5.0) dari VM via SNMPv2c."""
    hasil = {"status": "GAGAL", "sysname": None}
    try:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((host_vm, port_snmp_vm)),
            ContextData(),
            ObjectType(ObjectIdentity("1.3.6.1.2.1.1.5.0"))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication:
            print(f"[SNMP] GAGAL: {errorIndication}")
            hasil["error"] = str(errorIndication)
        elif errorStatus:
            print(f"[SNMP] GAGAL: {errorStatus.prettyPrint()}")
            hasil["error"] = errorStatus.prettyPrint()
        else:
            for vb in varBinds:
                sysname = str(vb[1])
                print(f"[SNMP] sysName: {sysname}")
                hasil = {"status": "OK", "sysname": sysname}
    except Exception as e:
        print(f"[SNMP] GAGAL: {e}")
        hasil["error"] = str(e)
    return hasil


if __name__ == "__main__":
    cek_snmp()