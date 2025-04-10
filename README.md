# Nmap_PortScan
使用python呼叫nmap做Port Scan  
確認那些Port有對外開放服務  
  
若無法連線，會顯示 no-response
```
10.0.0.1
10.0.0.1 no-response
```

若可以連線，會根據每個Port的連線結果回傳
```
10.0.0.2
10.0.0.2 Port:22 reset
10.0.0.2 Port:80 syn-ack
10.0.0.2 Port:443 syn-ack
10.0.0.2 Port:5988 reset
10.0.0.2 Port:5989 reset
10.0.0.2 Port:8000 syn-ack

10.0.0.3
10.0.0.3 Port:22 syn-ack
10.0.0.3 Port:23 no-response
10.0.0.3 Port:80 syn-ack
10.0.0.3 Port:443 syn-ack
```
