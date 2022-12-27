import web3

# Connect to the Ethereum network using the Infura API
w3 = web3.Web3(web3.Web3.HTTPProvider("https://mainnet.infura.io/v3/your-api-key"))

# Get the latest block number
latest_block = w3.eth.blockNumber

# Create a dictionary to store the balance of each account
balances = {}

# Iterate over all of the blocks
for block_num in range(latest_block - 20000, latest_block):
    # Get the block data
    block = w3.eth.getBlock(block_num, full_transactions=True)
    
    # Iterate over all of the transactions in the block
    for tx in block['transactions']:
        # Get the from and to addresses for the transaction
        from_address = tx['from']
        to_address = tx['to']
        
        # Get the value of the transaction in ETH
        value = w3.fromWei(tx['value'], 'ether')
        
        # Update the balances of the from and to addresses
        if from_address in balances:
            balances[from_address] -= value
        else:
            balances[from_address] = -value
            
        if to_address in balances:
            balances[to_address] += value
        else:
            balances[to_address] = value

# Sort the accounts by balance
sorted_balances = sorted(balances.items(), key=lambda x: x[1], reverse=True)

# Print the top 10000 whales
for i in range(10000):
    address, balance = sorted_balances[i]
    print(f"{address}: {balance} ETH")
