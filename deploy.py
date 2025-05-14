from brownie import Inbox, accounts

def main():
    acct = accounts[0]
    contract = Inbox.deploy("Hello World!", {"from": acct})
    print(f"✅ Deployed at: {contract.address}")
