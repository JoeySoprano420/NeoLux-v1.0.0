class CORI:
    def __init__(self):
        self.code_packets = []

    def add_packet(self, packet):
        self.code_packets.append(packet)

    def process_packets(self):
        results = []
        for packet in self.code_packets:
            results.append(self._process_packet(packet))
        return results

    def _process_packet(self, packet):
        # Example of packet processing
        return packet * 2

# Example usage
cori = CORI()
cori.add_packet(10)
cori.add_packet(20)
print(f"Processed packets: {cori.process_packets()}")
