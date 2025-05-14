# Our First Python based Solidity Contract

## Prerequisites

Python version 3.11

Create Python virtual environment using the following command:

```
python3.11 -m venv sol_env
```

Activate the virtual environment:

```
source sol_env/bin/activate
```

### Install Python Libraries

First upgrade pip installer:


```
pip install --upgrade pip
```

Install the required Python packages:

```
pip install web3 py-solc-x pytest
```

## Install Ganache-Cli

Ganache-cli is used to create local eth network. It is needed by brownie eth for simulating solidity contract deployments

```
    npm cache clean --force
    npm config set registry https://registry.npmjs.org/
    npm config get registry
    npm install -g ganache
```

Test ganache by running the following code:

```
    ganache
```




## Testing locally using brownie and ganache

### Create a local network

```
    brownie networks add development local-ganache host=http://127.0.0.1:8545 cmd=ganache-cli
```

### Deploying on the local network

First start a new screen on Linux and start the ganache on a port number: 8545

```
    ganache --port 8545
```

Now start the deployment:

```
    brownie run scripts/deploy.py
```

