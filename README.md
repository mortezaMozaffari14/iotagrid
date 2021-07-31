# Iotagrid
Iotagrid is the IOTA-based distributed computing platform where a task is distributed among IOTA nodes. These nodes are running in the Docker container.
## Set up private tangle and django web application
In order to set up the private tangle and run django server, you need to clone iotagrid repository:

```
git clone -b development https://github.com/mortezaMozaffari14/iotagrid.git
```
Then:

```
cd iotagrid/one-click-tangle/hornet-private-net
chmod +x ./private-tangle.sh

```
Now start private tangle with  Merkle Tree of Depth 16 by:

```
./private-tangle.sh start 16 30

```
Since above command computes Merkle Tree, that takes some minutes to be built. 

Now all services(all iota nodes, django server, and postgress) are running in the docker containers. To see these services:

```
docker ps -a

```
you should see all containers in the compose file.

Now browse: 127.0.0.1:8000/

All containers are running in the backend and if  you want to stop Iotagird:

```
./private-tangle.sh stop

``` 

when you want to start iotagrid for second time:

```
cd iotagrid/one-click-tangle/hornet-private-net
docker-compose --env-file ./.env up

```


## Refrences
* one-click-tangle repository: https://github.com/iotaledger/one-click-tangle


