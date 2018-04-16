from scapy.all import *

dstport=9999
srcport=2555
seqid=123456

c_s_syn=sr(IP(dst='192.168.32.50')/TCP(dport=dstport,sport=srcport,flags=2,seq=seqid), verbose = False)
resv_list=c_s_syn[0].res
tcp_fields=resv_list[0][1][1].fields

sc_sn=tcp_fields['seq']+1
cs_sn=tcp_fields['ack']

send(IP(dst='192.168.32.50')/TCP(dport=dstport,sport=srcport,flags=16,seq=cs_sn,ack=sc_sn), verbose = False)