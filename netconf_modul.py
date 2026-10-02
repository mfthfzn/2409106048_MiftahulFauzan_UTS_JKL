#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
netconf_modul.py - Modul pembuatan pesan NETCONF (edit-config VLAN)
untuk kantor cabang virtual.
Nama: Miftahul Fauzan | NIM: 2409106048
"""
from identitas import kode_cabang

vlan_id = int(kode_cabang)


def buat_pesan_netconf():
    """Membangun string XML permintaan NETCONF <rpc><edit-config>
    untuk membuat VLAN baru, disusun berdasarkan 3 lapisan arsitektur
    NETCONF: content, operations, dan messages."""

    # ===== CONTENT LAYER =====
    # Lapisan ini berisi DATA KONFIGURASI sesungguhnya yang ingin
    # diterapkan ke perangkat: definisi VLAN baru beserta ID dan namanya.
    content_layer = f"""<config>
      <vlan xmlns="urn:example:params:xml:ns:yang:vlan">
        <vlan-id>{vlan_id}</vlan-id>
        <name>cabang-{kode_cabang}</name>
      </vlan>
    </config>"""

    # ===== OPERATIONS LAYER =====
    # Lapisan ini menentukan OPERASI NETCONF yang dijalankan (edit-config)
    # beserta target datastore yang akan diubah (running).
    operations_layer = f"""<edit-config>
    <target>
      <running/>
    </target>
    {content_layer}
  </edit-config>"""

    # ===== MESSAGES LAYER =====
    # Lapisan ini adalah pembungkus RPC request beserta message-id,
    # dipakai untuk mencocokkan request dengan reply dari perangkat.
    messages_layer = f"""<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  {operations_layer}
</rpc>"""

    return messages_layer


if __name__ == "__main__":
    print(buat_pesan_netconf())
