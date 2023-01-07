# mininet-pox-forwarding
Mininet topology and SDN controller software for POX SDN. Uses L2 learning/Forwarding for custom packet drops

NOTE that the l2 learning and forwarding is all taken from POX's sample code, but i have modified it to 
drop packets from H2s MAC address

# Topology
```
└───s1
    |
    ├───s2
    │   ├───s4
    │   │       h1.txt
    │   │       h2.txt
    │   │       
    │   └───s5
    │           h3.txt
    │
    └───s3
        ├───s6
        │       h4.txt
        │       
        └───s7
                h5.txt
                h6.txt
```

Files are stored:
	Custom Topology 		mininet/mininet/custom/custom-topo.py
	L2-Learning/block		pox/pox/forwarding/custom.py

ON VIRTUAL MACHINE:
```cd mininet/custom
sudo mn --custom custom-topo.py --topo mytopo --controller=remote```

ON SSH LINE
```cd pox
./pox.py forwarding.custom info.packet_dump samples.pretty_log log.level --debug```
