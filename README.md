# Custom TCP Ack & Seq Numbers

This Python3 tool sends three packets with custom TCP Acknowledgement and Sequence numbers. This script will trigger a situation with unusually large orig_bytes in Zeek logs (https://github.com/zeek/zeek/issues/3313).

## Usage

Run using Python3 as follows (sending packets needs special privileges on Linux):

```bash
:~$ python3 tcp_custom_ackseqnum.py
```

Command-Line Arguments:
```bash
--src_ip: Source IP address (default: 172.10.0.10)
--dst_ip: Destination IP address (default: 172.10.0.20)
--sport: Source port (default: 12345)
--dport: Destination port (default: 80)
--seq_increment: Sequence number increment (default: 1073741824)
--ack_increment: Acknowledgment number increment (default: 1073741824)
```

Example:
```bash
:~$ sudo python3 tcp_custom_ackseqnum.py --src_ip 192.168.1.1 --dst_ip 192.168.1.2 --sport 54321 --seq_increment 1431655765
```

## Capture Packets with Tcpdump

Use tcpdump to capture the generated packets:

```bash
:~$ tcpdump -n -s0 -i <iface> port 54321 -v -c 3 -w /tmp/tcp_custom_ackseqnum-1.pcap
```

## Generate Zeek Logs

Use zeek to generate netflows from the generated packets (Note the generation of JSON logs is optional):

```bash
:~$ /opt/zeek/bin/zeek -r /tmp/tcp_custom_ackseqnum-1.pcap /opt/zeek/share/zeek/policy/tuning/json-logs.zeek
```

Read the JSON logs with jq:

```bash
:~$ jq . conn.log
```

```json
{
  "ts": 1722168596.475325,
  "uid": "CtNJeX2F1CkMho5SW9",
  "id.orig_h": "192.168.1.1",
  "id.orig_p": 54321,
  "id.resp_h": "192.168.1.2",
  "id.resp_p": 80,
  "proto": "tcp",
  "duration": 0.03772783279418945,
  "orig_bytes": 2863311530,
  "resp_bytes": 0,
  "conn_state": "OTH",
  "local_orig": true,
  "local_resp": true,
  "missed_bytes": 0,
  "history": "A",
  "orig_pkts": 3,
  "orig_ip_bytes": 120,
  "resp_pkts": 0,
  "resp_ip_bytes": 0
}
```
