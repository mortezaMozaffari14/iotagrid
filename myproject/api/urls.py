from django.conf.urls import url

from .views import(
                    hello_node,
                    send_and_recive_from_second_node,
                    search_transaction,
                    get_neighbors_for_first_node,
                    get_neighbors_for_second_node,
                    home_page,
                    send_transaction,
                    socket1,
                    socket2,
                    socket3,
                    get_transaction,
                    distribute_task,
                    create_seed,
                    create_address,
                    test_func,
                   detail
                    

                  )

app_name='api'
urlpatterns = [
    url(r'hello/$', hello_node, name = 'hello_node'),
    url(r'send_recive/$',send_and_recive_from_second_node, name = 'send_recive'),
    url(r'search/$',search_transaction, name = 'search_transaction'),
    url(r'neighbor1/$',get_neighbors_for_first_node, name = 'neighboor1'),
    url(r'neighbor2/$',get_neighbors_for_second_node, name = 'neighboor2'),
    #url(r'',home_page, name = 'homepage'),
    url(r'send/$',send_transaction, name = 'send'),
    url(r'111/$',socket1, name = 'so1'),
    url(r'222/$',socket2, name = 'so2'),
    url(r'333/$',socket3, name = 'so3'),
    url(r'get/$',get_transaction, name = 'get'),
    url(r'distribute_task/$',distribute_task, name = 'distribute_task'),
    url(r'create_seed/$',create_seed, name = 'create_seed'),
    url(r'create_address/$',create_address, name = 'create_address'),
    url(r'test_function/$',test_func, name = 'tttt'),
    url(r'^track/(?P<pk>[0-9a-f-]+)/$', detail,
        name = 'track'
       )

]