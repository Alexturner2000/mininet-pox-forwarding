from mininet.topo import Topo
class LabTopo(Topo):
  def __init__(self):
    Topo.__init__(self)

    h1 = self.addHost('h1')
    h2 = self.addHost('h2', mac='D3:13:1C:1B:76:A0')
    h3 = self.addHost('h3')
    h4 = self.addHost('h4')
    h5 = self.addHost('h5')
    h6 = self.addHost('h6', mac='B9:94:91:62:F1:65')

    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    s4 = self.addSwitch('s4')
    s5 = self.addSwitch('s5')
    s6 = self.addSwitch('s6')
    s7 = self.addSwitch('s7')

    self.addLink(s1, s2)
    self.addLink(s1, s3)
    self.addLink(s2, s4)
    self.addLink(s2, s5)
    self.addLink(s3, s6)
    self.addLink(s3, s7)
    self.addLink(s4, h1)
    self.addLink(s4, h2)
    self.addLink(s5, h3)
    self.addLink(s6, h4)
    self.addLink(s7, h5)
    self.addLink(s7, h6)

topos = {'mytopo': (lambda: LabTopo())}

