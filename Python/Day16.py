import time
import fileinput


class Packet():
    def __init__(self, bin_str, start_index):
        self.index = start_index + 6
        self.start_index = start_index
        self.bin_str = bin_str
        self.version = self.bin_str[start_index:start_index+3]
        self.type = self.bin_str[start_index+3:start_index+6]
        self.sub_packets = []
        self.literal = ""
        self.get_value()

    def get_value(self):
        if self.type == '100': # 4
            self.loop_literal()
        else:
            self.loop_operator()
        self.total_bit_length = self.index - self.start_index
        self.bin_str = self.bin_str[self.start_index:self.index]

    def check_length_id(self):
        if self.bin_str[self.index] == '0':
            return False
        elif self.bin_str[self.index] == '1':
            return True

    def loop_literal(self):
        # Loop through the binary string and get each group of 5 bits until a group of 5 bits that starts with a 1 is found
        while True:
            if self.index > len(self.bin_str):
                break
            if self.check_length_id():
                self.literal += self.bin_str[self.index+1:self.index+5]
                self.index += 5
            else:
                self.literal += self.bin_str[self.index+1:self.index+5]
                self.index += 5
                break
        self.literal = int(self.literal, 2)

    def loop_operator(self):
        if self.check_length_id():
            # If length type is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
            self.loop_length()
        else:
            # If length type is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
            self.loop_num()

    def loop_length(self):
        self.packets = int(self.bin_str[self.index+1:self.index+12], 2)
        self.index += 12
        for _ in range(self.packets):
            packet = Packet(self.bin_str, self.index)
            self.sub_packets.append(packet)
            self.index += self.sub_packets[-1].total_bit_length

    def loop_num(self):
        bit_length = int(self.bin_str[self.index+1:self.index+16], 2)
        self.index += 16
        sub_packet_start_index = self.index
        while self.index < sub_packet_start_index + bit_length:
            packet = Packet(self.bin_str, self.index)
            self.sub_packets.append(packet)
            self.index += self.sub_packets[-1].total_bit_length

    @property
    def values(self):
        return int(self.version, 2) + sum([sub_packet.values for sub_packet in self.sub_packets])

    @property
    def expression(self):
        if self.type == '000':
            return sum([sub_packet.expression for sub_packet in self.sub_packets])
        elif self.type == '001':
            product = 1
            for x in self.sub_packets:
                product *= x.expression
            return product
        elif self.type == '010':
            return min([sub_packet.expression for sub_packet in self.sub_packets])
        elif self.type == '011':
            return max([sub_packet.expression for sub_packet in self.sub_packets])
        elif self.type == '100':
            return self.literal
        elif self.type == '101':
            if self.sub_packets[0].expression > self.sub_packets[1].expression: return 1
            else: return 0
        elif self.type == '110':
            if self.sub_packets[0].expression < self.sub_packets[1].expression: return 1
            else: return 0
        elif self.type == '111':
            if self.sub_packets[0].expression == self.sub_packets[1].expression: return 1
            else: return 0


def hex_to_bin_str(hex_str):
    return {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111",
    }[hex_str]

def part1(bin_str):
    packet = Packet(bin_str, 0)
    print(packet.values)

def part2(bin_str):
    packet = Packet(bin_str, 0)
    print(packet.expression)

def main():
    num = [line.strip() for line in fileinput.input("./Input/Day16.txt")][0]
    bin_str = "".join([hex_to_bin_str(x) for x in num])
    part1(bin_str)
    part2(bin_str)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))