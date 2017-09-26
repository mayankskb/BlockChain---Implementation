#
# illustrating the creation of simple blocks and appending them to blockchain
# author : Mayank Mishra
#

# importing basic requisites
import hashlib
import datetime as date

# creating the structure of a single block in block chain
# it contains timestamp, index, data and the hash of the previous block
# these all are used for creating the hash of the current block
class block:
    def __init__(self, timestamp, index, data, hash_prev):
        self.timestamp = timestamp
        self.index = index
        self.data = data
        self.hash_prev = hash_prev
        self.hash = self.getHash()

    def getHash(self):
        md5 = hashlib.md5()
        md5.update((str(self.timestamp) +
               str(self.index) +                 
               str(self.data) + 
               str(self.hash_prev)).encode(encoding='utf_8'))
        return md5.digest()


#creating genesis block
def createGenesisBlock():
    return block(date.datetime.now(), 0, "Block Chain", "0")

#creating subsequent block in the blockchain
def createSubsequentBlock(prev_block):
    index = prev_block.index + 1
    timestamp = date.datetime.now()
    data = "Block Chain! Block "+str(index)
    prev_hash = prev_block.hash
    return block(timestamp, index, data, prev_hash)


if __name__ == '__main__':
    
    # creating the blockchain and adding the genesis block in that
    blockchain = [createGenesisBlock()]
    previous_block = blockchain[0]

    #number of block for illustration
    blocknumber = 30

    # implementing and growing blockchain to count of blocknumber
    for i in range(0, blocknumber):
        next_block = createSubsequentBlock(previous_block)
        blockchain.append(next_block)
        previous_block = next_block

        #printing the information of the added block
        print("Block #{} is added to the blockchain!!..".format(next_block.index))
        print("Hash is {}".format(next_block.hash))
