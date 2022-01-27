[test_client_hosts]
%{ for ip in test_clients ~}
${ip}
%{ endfor ~}