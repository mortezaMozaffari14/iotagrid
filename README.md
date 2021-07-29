# iotagrid
Iotagrid is the IOTA-based distributed computing platform where a task is distributed amontg IOTA nodes. These nodes are running in the docker container.
## set up private tangle
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
Now all services(all iota nodes, django server and postgress) are running in the docker containers. To see these services:

```
docker ps -a

```
If you want to stop all service just press *** Ctrl + C ***	

when you want to start iotagrid for second time:

```
docker-compose up

```
Now browse: 127.0.0.1:8000/

## Refrences
* one-click-tangle repository: https://github.com/iotaledger/one-click-tangle


