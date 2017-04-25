#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import amazon_pb2
# from google.protobuf.internal.decoder import _DecodeVarint32 as decoder
from google.protobuf.internal import encoder as protobuf_encoder
from google.protobuf.internal import decoder as protobuf_decoder
# from google.protobuf.internal.decoder import _DecodeVarint32
# from google.protobuf.internal.encoder import _EncodeVarint
import struct
import io

HOST = '10.236.48.21'
PORT = 23456
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))  # Connect

connect_msg = amazon_pb2.AConnect();
connect_msg.worldid = 1002;
# w1 = connect_msg.initwh.add()
# w1.x = -664
# w1.y = -1081
print
"msg is " + connect_msg.__str__();
sc = connect_msg.SerializeToString()

size = len(sc);
delimiter = protobuf_encoder._VarintBytes(size)

s.send(delimiter);
s.send(sc)  # send msg
response = amazon_pb2.AConnected()
head_byte = s.recv(4)

(msg_length, msg_pos) = protobuf_decoder._DecodeVarint32(head_byte, 0)
print(msg_length, msg_pos)
data = s.recv(msg_length)

command_msg = amazon_pb2.ACommands()
buy = command_msg.buy.add()
buy.whnum = 0
product = buy.things.add()
product.id = 123
product.description = "sample products"
product.count = 10

# topack = command_msg.topack.add()
# topack.whnum = 0;
# topack.things

# load = command_msg.load.add();
# load.whnum = 0;
# load.truckid = 0;
# load.shipid = 0;

print
"msg is " + command_msg.__str__()
command_str = command_msg.SerializeToString()

size = len(command_str)
delimiter = protobuf_encoder._VarintBytes(size)
s.send(delimiter)
s.send(command_str)  # send msg
print
"response is" + s.recv(1024)
# head_byte = s.recv(4)
# print head_byte;
# (msg_length,msg_pos)= protobuf_decoder._DecodeVarint32(head_byte,0)
# print (msg_length,msg_pos)
# data = s.recv(msg_length);








s.close()  # 关闭连接