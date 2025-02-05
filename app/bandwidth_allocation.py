# scripts/bandwidth_allocation.py
def allocate_bandwidth(predicted_segment, network_load=0.5, peak_time=False):
    # Define basic allocation for each segment
    bandwidth_allocation = {
        0: "Heavy Data User: High (10+ Mbps), may experience throttling",
        1: "Casual User: Moderate (5-10 Mbps), fair access",
        2: "Peak Time Heavy User: Dynamic (5-15 Mbps), adjusted per congestion",
        3: "Low Activity User: Low (1-5 Mbps), priority on off-peak"
    }

    # Adjust allocation for peak time with high network load
    if peak_time and network_load > 0.7:
        return f"{bandwidth_allocation[predicted_segment]} (adjusted due to peak load)"
    else:
        return bandwidth_allocation[predicted_segment]
