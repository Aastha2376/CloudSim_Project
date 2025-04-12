# visualization/visualize_results.py
import os
import matplotlib.pyplot as plt
from data_parser import parse_report

# Create charts/ directory if not exists
os.makedirs("visualization/charts", exist_ok=True)

# Load parsed data
data = parse_report()

strategies = ["TimeShared", "SpaceShared"]

# Plot Runtime
plt.figure()
plt.bar(strategies, [data[s]["runtime"] for s in strategies], color=["steelblue", "tomato"])
plt.title("Simulation Runtime Comparison")
plt.ylabel("Runtime (s)")
plt.savefig("visualization/charts/runtime_comparison.png")
plt.close()

# Plot Makespan
plt.figure()
plt.bar(strategies, [data[s]["makespan"] for s in strategies], color=["seagreen", "orange"])
plt.title("Makespan Comparison")
plt.ylabel("Makespan (s)")
plt.savefig("visualization/charts/makespan_comparison.png")
plt.close()

# Plot Average Execution Time
plt.figure()
plt.bar(strategies, [data[s]["avg_exec_time"] for s in strategies], color=["orchid", "skyblue"])
plt.title("Average Execution Time Comparison")
plt.ylabel("Avg Execution Time (s)")
plt.savefig("visualization/charts/avg_execution_time_comparison.png")
plt.close()

print("✅ Charts generated inside: visualization/charts/")
