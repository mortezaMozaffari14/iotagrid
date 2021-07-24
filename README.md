# iotagrid
Iotagrid is the IOTA-based distributed computing platform where a task is distributed amontg IOTA nodes. 
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
## run webserver