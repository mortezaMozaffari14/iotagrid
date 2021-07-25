# iotagrid
Iotagrid is the IOTA-based distributed computing platform where a task is distributed amontg IOTA nodes. These nodes are running in the docker container.
## set up private tangle
In order to set up the private tangle, you need to clone the repository:
```
git clone https://github.com/mortezaMozaffari14/iotagrid.git
```
Then:
```
cd iotagrid/one-click-tangle/hornet-private-net
chmod +x ./private-tangle.sh
```
Now start private tangle with  Merkle Tree of Depth 16 by :

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
## Refrences


