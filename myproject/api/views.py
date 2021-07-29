import time
import uuid
from zmq.sugar import context
from django.views.generic import ListView, CreateView, DetailView
from myproject.api.models import outputs, problem, nodes,inputs
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from iota.crypto.types import Seed
from .form import InputForm
from iota import( Iota, 
                  ProposedTransaction, 
                  Address,
                  Tag,
                  TryteString,
                )

seed_for_first_node = "YIZXIJNLRSFU9OGCTBJJPGVRXDEZVVFELZQUK9K9VFWBQLULQZRBRCLIVCQVSIIIMZPQVDTRRLWDAWSRL"
seed_for_second_node = "NHBDVRADCXJJYCSOJAPTITGHVULNUZIKKUKRMTM9IWXBTY9BPHUMDKVCMWEJQYQEDJLADKATNCZKX9HYO"
seed_for_third_node = "OU9BABBPHGHXQFEIZOMCIFJAP9AFZSUJJJYTUZSK9BZBHWTURMRRPVPFQWAQRTNCKOHJRIEVZJQBPMHEN"
address_for_first_node = 'EA9IAPVJCLJTBJCFERWTPZRBBGZEXDXKIXVPEWLQJZSYJTUTLCJYVKNYJLDZZSZMMSYDJCRTITMVPBNHY'
address_for_second_node = "LBHMLPDSSLNVKORURUWQ9WZKSCKTUYBELBJIMZQEHWVWWXAPUAFQENFCTYGSRIIGKOSVMAOYCOIOLJGKC"
address_for_third_node = "FWOSYILPVJPYNUTBPCQLRLGKMXWDGBCNMGLGVWAUKGSHNODRFIRIUGTGFVYSALMBWXTMJBJWALICHFOWA"


def home_page(request):
    return render(request,
                 'api/home_page.html'
                  )


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

            
            


