import hashlib
from datetime import datetime

#====================================================================================
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.prev = None

    def calc_hash(self):
          sha = hashlib.sha256()
          hash_str = (self.timestamp + self.data).encode('utf-8')
          sha.update(hash_str)
          return sha.hexdigest()

    def __repr__(self):
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)

    def __str__(self):
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)

#====================================================================================
class BlockChain(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_block(self, data):
        current_ts = self.get_current_timestamp()
        if data is None or data =="":
            return None
        elif self.head is None:
            self.head = Block(current_ts, data, 0)
            self.tail = self.head
        else:
            new_block = Block(current_ts, data, self.tail.hash)
            new_block.prev = self.tail
            self.tail = new_block
        self.size += 1
        return self.tail

    def get_chain_size(self):
        return self.size

    def to_list(self):
        blocks_list = []
        if self.tail:
            self.to_list_recursively(self.tail, blocks_list)
        return blocks_list

    def to_list_recursively(self, block, blocks_list):
        if block.prev is not None:
            self.to_list_recursively(block.prev, blocks_list)
        blocks_list.append(block)

    def get_current_timestamp(self):
        # datetime object containing current date and time
        now = datetime.now()
        #print("now =", now)
        dt_string = now.strftime("%H:%M:%S %d/%m/%Y")
        #print("date and time =", dt_string)
        return dt_string

    def display(self):
        print(f"**** << size = {self.size} >>****")
        blocks_list = self.to_list()
        if len(blocks_list) == 0:
            print("The BlockChain is empty")
        else:
            for b in blocks_list:
                print(b)


#====================================================================================

def main():

    my_bl = BlockChain()
    #my_bl.display()

    print("\n")
    print("************** < Test case 1: Adding an empty block >*******************")
    my_bl.add_block("")
    my_bl.display()

    print("\n")
    print("************** < Test case 2: Adding None block >*******************")
    my_bl.add_block(None)
    my_bl.display()

    print("\n")
    print("************** < Test case 3: Adding Block_0 block >*******************")
    my_bl.add_block("Block_0")
    my_bl.display()

    print("\n")
    print("************** < Test case 4: Adding Block_1 block >*******************")
    my_bl.add_block("Block_1")
    my_bl.display()

    print("\n")
    print("************** < Test case 5: Adding an empty block >*******************")
    my_bl.add_block("")
    my_bl.display()

    print("\n")
    print("************** < Test case 6: Adding Block_2 block >*******************")
    my_bl.add_block("Block_2")
    my_bl.display()

    print("\n")
    print("************** < Test case 7: Adding None block >*******************")
    my_bl.add_block(None)
    my_bl.display()
    print("\n")



#====================================================================================
if __name__ == "__main__":
    main()
