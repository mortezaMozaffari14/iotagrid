from zmq.sugar import context
from myproject.api.models import outputs, problem, nodes,inputs
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
from iota.crypto.types import Seed
from iota import( Iota, 
                  ProposedTransaction, 
                  Address,
                  Tag,
                  TryteString,
                )
import time
from .form import InputForm
import uuid
import zmq
address_for_first_node = 'EA9IAPVJCLJTBJCFERWTPZRBBGZEXDXKIXVPEWLQJZSYJTUTLCJYVKNYJLDZZSZMMSYDJCRTITMVPBNHY'
address_for_second_node = "LBHMLPDSSLNVKORURUWQ9WZKSCKTUYBELBJIMZQEHWVWWXAPUAFQENFCTYGSRIIGKOSVMAOYCOIOLJGKC"
address_for_third_node = "FWOSYILPVJPYNUTBPCQLRLGKMXWDGBCNMGLGVWAUKGSHNODRFIRIUGTGFVYSALMBWXTMJBJWALICHFOWA"
seed_for_first_node = "YIZXIJNLRSFU9OGCTBJJPGVRXDEZVVFELZQUK9K9VFWBQLULQZRBRCLIVCQVSIIIMZPQVDTRRLWDAWSRL"
seed_for_second_node = "NHBDVRADCXJJYCSOJAPTITGHVULNUZIKKUKRMTM9IWXBTY9BPHUMDKVCMWEJQYQEDJLADKATNCZKX9HYO"
seed_for_third_node = "OU9BABBPHGHXQFEIZOMCIFJAP9AFZSUJJJYTUZSK9BZBHWTURMRRPVPFQWAQRTNCKOHJRIEVZJQBPMHEN"

def second_node_socket():
    print("=================================================================")
    api = Iota('http://localhost:14268',seed_for_second_node)
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://localhost:5558')
    print ("Socket connected")
    print(socket.subscribe('tx'))
    while True:
        print ("Waiting for events from the IOTA node")
        message = socket.recv()
        print(message)
        data = message.split()
        if data[2].decode("utf-8") == address_for_second_node:
            print("in iffffffffffffffffffffffffffffffffffff")
            transaction_hash = data[1]
            tx_obj = api.get_transaction_objects([transaction_hash])
            input = tx_obj['transactions'][0].signature_message_fragment.decode()
            print('input issssssssssssssss',input)
            output = str(int(input) *int(input) )
            print("************************************************")
            print("out put computed by node 2",output)
            print("************************************************")
            message = TryteString.from_unicode(output)
            fictional_transactions = ProposedTransaction(
            address=Address(address_for_first_node),
            message=message,
            value=0,
            tag = data[12]
            )
            result = api.send_transfer(transfers = [fictional_transactions],min_weight_magnitude=9)
            print('answer transaction 1 ', result['bundle'].tail_transaction.hash)

def third_node_socket():
    api = Iota('http://localhost:14267',seed_for_third_node)
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://localhost:5557')
    print ("Socket connected")
    print(socket.subscribe('tx'))
    while True:
        print ("Waiting for events from the IOTA node")
        message = socket.recv()
        print(message)
        data = message.split()
        if data[2].decode("utf-8") == address_for_third_node:
            print("in iffffffffffffffffffffffffffffffffffff33333333")
            transaction_hash = data[1]
            tx_obj = api.get_transaction_objects([transaction_hash])
            input = tx_obj['transactions'][0].signature_message_fragment.decode()
            print('input issssssssssssssss',input)
            output = str(int(input) * int(input))
            print("************************************************")
            print(" output computed bu third nodeeeeeee",output)
            print("************************************************")
            message = TryteString.from_unicode(output)
            fictional_transactions = ProposedTransaction(
            address=Address(address_for_first_node),
            message=message,
            value=0,
            tag = data[12]
            )
            result = api.send_transfer(transfers = [fictional_transactions],min_weight_magnitude=9)
            print('answer transaction 1 ', result['bundle'].tail_transaction.hash)
      
import math
def first_node_socket():
    api = Iota('http://localhost:14265',seed_for_first_node)
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://localhost:5556')
    print ("Socket connected")
    print(socket.subscribe('tx'))
    while True:
        print ("Waiting for events from the IOTA node")
        message = socket.recv()
        print(message)
        data = message.split()
        if(data[2].decode("utf-8") == address_for_first_node):
            print("in first node transaction recieve")
            transaction_hash = data[1]
            tx_obj = api.get_transaction_objects([transaction_hash])
            answer = tx_obj['transactions'][0].signature_message_fragment.decode()
            problemm = problem.objects.get(problem_tag=str(data[12].decode("utf-8")))
            outs = outputs.objects.filter(problem = problemm)
            print("whole outss is ",outs)
            inputt = int(answer)
            print("**********************************************************")
            print("answer recieve by first nodddddddddddeeeeeeeeee",inputt)
            print("**********************************************************")
            for out in outs:

                print("out.input type  issssssssssssss",type(out.input))
                print("in argggggggggg is ",out.input )
                out_in = out.input
                out_inn = str(out_in)
                print("type of out_Inn issssssssssssssssssssssssssssssss",type(out_inn)) 
                outt = int(out_inn) * int(out_inn)
                if outt == inputt :
                    print("**********************************************************")
                    print("**********************************************************")
                    print("**********************************************************")
                    print("**********************************************************")
                    out.output = str(answer)
                    out.save()
                    # print("in sok1111111111111111111", inputt[0])
                    # problem_obj = problem.objects.get(input = inputt[0])
                    # print(problem_obj)
                    # problem_obj.output = answer
                    # problem_obj.save()
            print("finishhhhhhhhhhhhhhh")



