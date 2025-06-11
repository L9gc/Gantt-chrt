import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define project tasks and their durations
tasks = [
    ("Proposal submission", "2025-03-01", "2025-03-31"),
    ("Planning Phase", "2025-04-01", "2025-05-05"),
    ("Analysis Phase", "2025-05-06", "2025-07-04"),
    ("System design Phase", "2025-06-05", "2025-07-04"),
    ("Development Phase", "2025-07-05", "2025-09-30"),
    ("Testing Phase", "2025-10-01", "2025-10-20"),
    ("Deployment Phase", "2025-10-21", "2025-10-31"),
    ("Training & Support", "2025-11-01", "2025-11-02"),
    ("Poject Presentation", "2025-11-03", "2025-11-12"),
    ("Presentation & Maintenance", "2025-11-01", "2025-12-20")
]

# Convert task data to a DataFrame
df = pd.DataFrame(tasks, columns=["Task", "Start", "End"])
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])
df["Duration"] = df["End"] - df["Start"]

# Plot Gantt chart
fig, ax = plt.subplots(figsize=(10, 5))
for i, task in enumerate(df.itertuples()):
    ax.barh(task.Task, (task.End - task.Start).days, left=mdates.date2num(task.Start), color="red", edgecolor="black")

# Format x-axis as dates
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b-%Y"))
ax.xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)

# Labels and title
plt.xlabel("Timeline")
plt.ylabel("Tasks")
plt.title("Gantt Chart")
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Show plot
plt.show()