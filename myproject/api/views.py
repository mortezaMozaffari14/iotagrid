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
from django.views.generic import ListView, CreateView, DetailView
def home_page(request):
    #return HttpResponse("hiiiiiiiiiiiiiiii")
    return render(request,
                 'api/home_page.html'
                  )
def hello_node(request):
    seed = 'DQNEMZUAQTIQLAJ9NUXWPGBMRKAMWBHSAEZSOKPYOYBEFYJ9IEVKTYZY9XOI9WWNRJLJPSV9CQ9KBHMK9'
    api = Iota('http://localhost:24269')
    #print(api.get_node_info())
    #neighbors = api.get_neighbors()
    #return HttpResponse(api.add_neighbors(['tcp://node1:15600']))
    #return HttpResponse(neighbors["neighbors"])
    print(api.get_balances(["WPBAP9TLZIKLAQNNAGYYTMRN9WGGHOHHDVYPZJURZTBHPISOAZOQDNEYMBVZQEWQX9BNZNBDFYJLAGYLC"]))
    return HttpResponse(api.get_balances(["WPBAP9TLZIKLAQNNAGYYTMRN9WGGHOHHDVYPZJURZTBHPISOAZOQDNEYMBVZQEWQX9BNZNBDFYJLAGYLC"]))
    #hash_of_tail_transction = 'DUBLXGWWJCMYXCHBGCZLXGMRDPZOTQYQLMHDOMSSZIDGXUUHM9PSN9WZTGEYCDMYCEZLJBQWWCDEZ9999'
    #result_hash = "FNPWL9JAZCHZQEEXXOGZAAJPCYRQEJRSXDFDPUTPQZFNN9HKHBWXQLIH9DDXPPPKKICUCYEDLPVOA9999"
    #bd = api.get_bundles(hash_of_tail_transction)
    #bd_2 = api.get_bundles(result_hash)
    #print(bd_2['bundles'][0].get_messages())
    #return HttpResponse(bd_2['bundles'][0].get_messages())


def send_and_recive_from_second_node(request):
    my_seed_for_02 = 'WWJKYPEPDJGKYTQSOFEYGZVQKDW9AOXGMJWHPKLEPHGEPWPCIBHOKLAL9OJCYVTZOKCYIGWGKKQGCTH9C'
    api = Iota('http://localhost:14265',my_seed_for_02)
    address_for_node_02 = '9YNVBPRSCHVFWZ9MBDQHRRFNCXHKCGXITISHBMTREOEOUS9HLU9RNIG9CLOLYJBMIBNANFMIARCAPFMJB'
    address_for_secondnode = 'KD9IKAHXOUYXKO9KNWDJQEZ9UPXSVW9LLFUHMDHSJZGEKG9NVOJE9LRJQVNUFT9LSGZCSAABEKMCVGKCZ'
    message = TryteString.from_unicode('hi node 022 i a\'m node 02 please solve 2+2+3 = ?')
    fictional_transactions = ProposedTransaction(
    address=Address(address_for_secondnode),
    message=message,
    value=0
    )
    result = api.send_transfer(transfers = [fictional_transactions])
    result_hash = result['bundle'].tail_transaction.hash
    #bd_2 = api.get_bundles(result_hash)
    seed = 'DQNEMZUAQTIQLAJ9NUXWPGBMRKAMWBHSAEZSOKPYOYBEFYJ9IEVKTYZY9XOI9WWNRJLJPSV9CQ9KBHMK9'
    
    try:
        api_2 = Iota('http://localhost:14266',seed)
        bd_2 = api_2.get_bundles(result_hash)
        print(bd_2['bundles'][0].get_messages())
        return HttpResponse(bd_2['bundles'][0].get_messages())
      
    except:
        return HttpResponse("cannot connect to second node" )


def search_transaction(request):
    seed = 'DQNEMZUAQTIQLAJ9NUXWPGBMRKAMWBHSAEZSOKPYOYBEFYJ9IEVKTYZY9XOI9WWNRJLJPSV9CQ9KBHMK9' 
    api_2 = Iota('http://localhost:14266',seed)
    #result = api.send_transfer(transfers = [fictional_transactions])
    result_hash = "W9PBQMJENXYDFGDZSKOPVOUCHOQQOHTZ9QLUPVUAREOUVPOMXTWOSVYPPUUYVEJMTMODLXZVIPERZ9999"
    bd_2 = api_2.get_bundles(result_hash)
    return HttpResponse(bd_2['bundles'][0].get_messages()) 

def get_neighbors_for_first_node(request):
    my_seed_for_02 = 'WWJKYPEPDJGKYTQSOFEYGZVQKDW9AOXGMJWHPKLEPHGEPWPCIBHOKLAL9OJCYVTZOKCYIGWGKKQGCTH9C'
    api = Iota('http://localhost:14265',my_seed_for_02)
    print(api.get_neighbors())
    neighbors = api.get_neighbors()
    return HttpResponse(neighbors["neighbors"])

def get_neighbors_for_second_node(request):
    seed = 'DQNEMZUAQTIQLAJ9NUXWPGBMRKAMWBHSAEZSOKPYOYBEFYJ9IEVKTYZY9XOI9WWNRJLJPSV9CQ9KBHMK9' 
    api = Iota('http://localhost:14266',seed)
    print(api.get_neighbors())
    neighbors = api.get_neighbors()
    return HttpResponse(neighbors["neighbors"])

import zmq
def send_transaction(request):
    #context = zmq.Context()
    #socket = context.socket(zmq.SUB)
    #socket.connect('tcp://localhost:5556')
    #socket.subscribe('tx')
    #print ("Socket connected")
    second_seed = 'DQNEMZUAQTIQLAJ9NUXWPGBMRKAMWBHSAEZSOKPYOYBEFYJ9IEVKTYZY9XOI9WWNRJLJPSV9CQ9KBHMK9'
    #first_seed = 'WWJKYPEPDJGKYTQSOFEYGZVQKDW9AOXGMJWHPKLEPHGEPWPCIBHOKLAL9OJCYVTZOKCYIGWGKKQGCTH9C'
    api = Iota('http://localhost:14266',second_seed)
    address_for_node_02 = '9YNVBPRSCHVFWZ9MBDQHRRFNCXHKCGXITISHBMTREOEOUS9HLU9RNIG9CLOLYJBMIBNANFMIARCAPFMJB'
    #address_for_secondnode = 'KD9IKAHXOUYXKO9KNWDJQEZ9UPXSVW9LLFUHMDHSJZGEKG9NVOJE9LRJQVNUFT9LSGZCSAABEKMCVGKCZ'
    message = TryteString.from_unicode('hi node 022 i a\'m node 02 please solve 2+2+3 = ?')
    fictional_transactions = ProposedTransaction(
            address=Address(address_for_node_02),
            message=message,
            value=0
            )
    result = api.send_transfer(transfers = [fictional_transactions])
    result_hash = result['bundle'].tail_transaction.hash
    #print ("Waiting for events from the IOTA node")
    #message = socket.recv()
    #data = message.split()
    #print("the splited data is ", data)
    #print("data befor split is ", message)
    return HttpResponse(result_hash)

####################################
###################################
###################################

def get_transaction(request):
    result_hash = "WZMQXSQUGJVWMBHUIUNRKKGUFBLUSF9EBSWYQYYJTKIBUCIQFUBOUUJBERKV9DKASAYIBZKXVBFSA9999" 
    #second_seed = 'DQNEMZUAQTIQLAJ9NUXWPGBMRKAMWBHSAEZSOKPYOYBEFYJ9IEVKTYZY9XOI9WWNRJLJPSV9CQ9KBHMK9'
    first_seed = 'WWJKYPEPDJGKYTQSOFEYGZVQKDW9AOXGMJWHPKLEPHGEPWPCIBHOKLAL9OJCYVTZOKCYIGWGKKQGCTH9C'
    api = Iota('http://localhost:14265',first_seed)
    bd_2 = api.get_bundles(result_hash)
    print(bd_2['bundles'][0].get_messages())
    return HttpResponse(bd_2['bundles'][0].get_messages())
########################################################################
########################################################################
########################################################################
########################## HORNET ######################################
########################################################################
########################################################################
seed_for_first_node = "YIZXIJNLRSFU9OGCTBJJPGVRXDEZVVFELZQUK9K9VFWBQLULQZRBRCLIVCQVSIIIMZPQVDTRRLWDAWSRL"
seed_for_second_node = "NHBDVRADCXJJYCSOJAPTITGHVULNUZIKKUKRMTM9IWXBTY9BPHUMDKVCMWEJQYQEDJLADKATNCZKX9HYO"
seed_for_third_node = "OU9BABBPHGHXQFEIZOMCIFJAP9AFZSUJJJYTUZSK9BZBHWTURMRRPVPFQWAQRTNCKOHJRIEVZJQBPMHEN"
address_for_first_node = 'EA9IAPVJCLJTBJCFERWTPZRBBGZEXDXKIXVPEWLQJZSYJTUTLCJYVKNYJLDZZSZMMSYDJCRTITMVPBNHY'
address_for_second_node = "LBHMLPDSSLNVKORURUWQ9WZKSCKTUYBELBJIMZQEHWVWWXAPUAFQENFCTYGSRIIGKOSVMAOYCOIOLJGKC"
address_for_third_node = "FWOSYILPVJPYNUTBPCQLRLGKMXWDGBCNMGLGVWAUKGSHNODRFIRIUGTGFVYSALMBWXTMJBJWALICHFOWA"
def create_seed(request):
    my_seed = Seed.random()
    return HttpResponse(my_seed)

def create_address(request):
    api = Iota('http://localhost:14267',seed_for_third_node)
    address = api.get_new_addresses(index=0, count=1, security_level = 1)['addresses'][0]
    print(address)
    return HttpResponse(address)


def distribute_task(request):
    api = Iota('http://localhost:14265',seed_for_first_node)
    form = InputForm()
    tt = str(uuid.uuid4())
    ttt = tt[0:12]
    T=TryteString.from_unicode(ttt)
    print("tag is ......:",tt)
    tagg = Tag(T)
    print("ttttttaaaaaaaaaaaaaaaggggggggggggggg issssssssssssssssssssss:",tagg)
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            
            in_1 = str(form.cleaned_data['input_1'])
            in_2 = str(form.cleaned_data['input_2'])
            inputlist = [in_1,in_2]
            print("************************************************")
            print(" data recieved by form isssssssssssss",inputlist)
            print("************************************************")
            message_2 = TryteString.from_unicode(in_1)
            message_3 = TryteString.from_unicode(in_2)
            fictional_transactions_2 = ProposedTransaction(
            address=Address(address_for_second_node),
            tag = tagg,
            message=message_2,
            value=0,
            )
            fictional_transactions_3 = ProposedTransaction(
            address=Address(address_for_third_node),
            tag = tagg,
            message=message_3,
            value=0,
            )
            result = api.send_transfer(transfers = [fictional_transactions_3,fictional_transactions_2],min_weight_magnitude=9)
            pp = nodes.objects.filter(type="IOTA node")
            print(pp)
            j = 0
            problem.objects.create(problem_tag = str(tagg))
            new_problem = problem.objects.get(problem_tag = str(tagg))
            print(new_problem)
            for i in pp:
                print("iiiiiiiiiiiii",i)
                ttt = str(uuid.uuid4())
                inputs.objects.create(input= inputlist[j],tt=ttt)
                iii = inputs.objects.get(tt=ttt)
                outputs.objects.create(node = i,input = iii, problem = new_problem)
                j+=1
            return redirect('/track/{}'.format(new_problem.id))
    context = {
        "form" :form
    }
    return render(request,
                 'api/distribute_task.html',
                  context          
                  )
def test_func(request):
    api = Iota('http://localhost:14268',seed_for_second_node)
    result_hash = "FAPWPKFKPPCKCVJSZJDQBBBPTZNARHHDQVWORONYWIRAHWSSUMHAAXXXHHRHIRQETZOWYSAWTNXOJD999"
    bd_2 = api.get_bundles(result_hash)
    print(bd_2['bundles'][0])
    tx_obj = api.get_transaction_objects(["FAPWPKFKPPCKCVJSZJDQBBBPTZNARHHDQVWORONYWIRAHWSSUMHAAXXXHHRHIRQETZOWYSAWTNXOJD999"])
    #return HttpResponse(bd_2['bundles'][0].get_messages())
    print(tx_obj['transactions'][0].signature_message_fragment.decode())
    return HttpResponse(tx_obj['transactions'][0].signature_message_fragment.decode())


def socket2(request):
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
        # print("0000000000000 ", data[0])
        # print("1111111111111 ", data[1])
        # print("2222222222222", data[2].decode("utf-8"))
        # print("3333333333333", data[3])
        # print("4444444444444", data[4])
        # print("5555555555555", data[5])
        # print("6666666666666", data[6])
        # print("7777777777777", data[7])
        # print("8888888888888", data[8])
        # print("9999999999999", data[9])
        # print("10101010101010", data[10])
        # print("11111111111111", data[11])
        # print("1212121212121212", data[12])
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


def socket3(request):
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
        # print("0000000000000 ", data[0])
        # print("1111111111111 ", data[1])
        # print("2222222222222", data[2].decode("utf-8"))
        # print("3333333333333", data[3])
        # print("4444444444444", data[4])
        # print("5555555555555", data[5])
        # print("6666666666666", data[6])
        # print("7777777777777", data[7])
        # print("8888888888888", data[8])
        # print("9999999999999", data[9])
        # print("10101010101010", data[10])
        # print("11111111111111", data[11])
        # print("1212121212121212", data[12])
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
def socket1(request):
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
        # print("0000000000000 ", data[0])
        # print("1111111111111 ", data[1])
        # print("2222222222222", data[2])
        # print("3333333333333", data[3])
        # print("4444444444444", data[4])
        # print("5555555555555", data[5])
        # print("6666666666666", data[6])
        # print("7777777777777", data[7])
        # print("8888888888888", data[8])
        # print("9999999999999", data[9])
        # print("10101010101010", data[10])
        # print("11111111111111", data[11])
        # print("1212121212121212", data[12])
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


def detail(request,pk):
    problemm = problem.objects.get(id=pk)
    final = problemm.final_answer
    outs = outputs.objects.filter(problem = problemm)
    a = 0
    final_answerr = 0
    for out in outs:
        if out.output is None:
            print("innnnnnnnn none")
            a+= 1
        else:
            print("in esslllllllllllllllllllllllllllsssssssssssssssssssssssseeeeeeeeeeeesssss")
            outt = out.output
            final_answerr+= int(outt)
    if a==0:
        final = final_answerr

    context = {
        "outs":outs,
        "final":final,

        }
 
    return render(request,'api/problem_detail.html',context)

            
            


