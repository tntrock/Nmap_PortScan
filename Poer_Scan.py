import nmap

for ip4 in range(256):
    ip = str('10.0.0.' + str(ip4))
    print(ip)
    nm = nmap.PortScanner()
    nm.scan(ip, arguments='-sS -p 1-65535 -v')

    data = [(x, nm[x]) for x in nm.all_hosts()]

    for n in range(len(data)):
        ipv4 = data[n][1]['addresses']['ipv4']
        status = data[n][1]['status']['reason']

        if 'tcp' in data[n][1]:
            for port in data[n][1]['tcp']:
                port_info = data[n][1]['tcp'][port]
                print(str(ipv4) + ' ' + 'Port:' + str(port) + ' ' + str(port_info['reason']))
        else:
            print(str(ipv4), str(status))
        print('')
