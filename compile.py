from solcx import compile_standard, install_solc
import json

# Install specific Solidity version
install_solc("0.8.30")

# Read the source code
with open("Inbox.sol", "r") as file:
    source_code = file.read()

# Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "Inbox.sol": {
            "content": source_code
        }
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
            }
        }
    }
}, solc_version="0.8.30")

# Save to JSON file (optional)
with open("compiled_inbox.json", "w") as f:
    json.dump(compiled_sol, f)

print("✅ Contract compiled successfully!")
