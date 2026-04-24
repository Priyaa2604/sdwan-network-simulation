import random

class Link:
    def __init__(self, name, latency, bandwidth, cost):
        self.name = name
        self.latency = latency
        self.bandwidth = bandwidth
        self.cost = cost

    def __str__(self):
        return f"{self.name} | Latency: {self.latency}ms | Bandwidth: {self.bandwidth}Mbps | Cost: {self.cost}"


class SDWANController:
    def __init__(self, links):
        self.links = links

    def select_best_link(self, traffic_type):
        print(f"\nSelecting best link for {traffic_type} traffic...")

        if traffic_type == "video":
            best = max(self.links, key=lambda x: x.bandwidth)

        elif traffic_type == "voice":
            best = min(self.links, key=lambda x: x.latency)

        elif traffic_type == "data":
            best = min(self.links, key=lambda x: x.cost)

        else:
            best = random.choice(self.links)

        return best


mpls = Link("MPLS", latency=20, bandwidth=50, cost=100)
broadband = Link("Broadband", latency=50, bandwidth=100, cost=50)
lte = Link("LTE", latency=30, bandwidth=30, cost=70)

links = [mpls, broadband, lte]

controller = SDWANController(links)

traffic_types = ["video", "voice", "data"]

for traffic in traffic_types:
    best_link = controller.select_best_link(traffic)
    print(f"Best link for {traffic}: {best_link}")
