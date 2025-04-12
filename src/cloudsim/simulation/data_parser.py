# visualization/data_parser.py
def parse_report(file_path="scheduling_comparison_report.txt"):
    with open(file_path, "r") as f:
        lines = f.readlines()

    metrics = {
        "TimeShared": {"makespan": 0.0, "avg_exec_time": 0.0, "runtime": 0.0},
        "SpaceShared": {"makespan": 0.0, "avg_exec_time": 0.0, "runtime": 0.0}
    }

    for line in lines:
        if "Time-Shared Runtime" in line:
            metrics["TimeShared"]["runtime"] = float(line.split(":")[1].replace("s", "").strip())
        elif "Space-Shared Runtime" in line:
            metrics["SpaceShared"]["runtime"] = float(line.split(":")[1].replace("s", "").strip())
        elif "Time-Shared Makespan" in line:
            metrics["TimeShared"]["makespan"] = float(line.split(":")[1].strip())
        elif "Space-Shared Makespan" in line:
            metrics["SpaceShared"]["makespan"] = float(line.split(":")[1].strip())
        elif "Time-Shared Avg Exec Time" in line:
            metrics["TimeShared"]["avg_exec_time"] = float(line.split(":")[1].strip())
        elif "Space-Shared Avg Exec Time" in line:
            metrics["SpaceShared"]["avg_exec_time"] = float(line.split(":")[1].strip())

    return metrics
