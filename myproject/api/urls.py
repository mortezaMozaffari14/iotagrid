from django.conf.urls import url

from .views import(
                    search_transaction,
                    get_neighbors_for_first_node,
                    get_neighbors_for_second_node,
                    home_page,
                    distribute_task,
                    create_seed,
                    create_address,
                    detail
                    

                  )

app_name='api'
urlpatterns = [
    url(r'search/$',search_transaction, name = 'search_transaction'),
    url(r'neighbor1/$',get_neighbors_for_first_node, name = 'neighboor1'),
    url(r'neighbor2/$',get_neighbors_for_second_node, name = 'neighboor2'),
    #url(r'',home_page, name = 'homepage'),
    url(r'distribute_task/$',distribute_task, name = 'distribute_task'),
    url(r'create_seed/$',create_seed, name = 'create_seed'),
    url(r'create_address/$',create_address, name = 'create_address'),
    url(r'^track/(?P<pk>[0-9a-f-]+)/$', detail,
        name = 'track'
       )

]