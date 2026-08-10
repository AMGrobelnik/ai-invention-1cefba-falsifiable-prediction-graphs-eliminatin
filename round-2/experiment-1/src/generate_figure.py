import json
import matplotlib.pyplot as plt
import numpy as np

with open('method_out.json', 'r') as f:
    data = json.load(f)

summary = data['summary_stats']
thresholds = [0.00, 0.01, 0.02, 0.05, 0.10, 0.15, 0.20]
tau_labels = [str(t) for t in thresholds]

proc_det = [summary['procedural']['threshold_breakdown'][t]['detection_rate'] for t in tau_labels]
fals_det = [summary['falsifiable_graph']['threshold_breakdown'][t]['detection_rate'] for t in tau_labels]

proc_fpr = [summary['procedural']['threshold_breakdown'][t]['false_positive_rate'] for t in tau_labels]
fals_fpr = [summary['falsifiable_graph']['threshold_breakdown'][t]['false_positive_rate'] for t in tau_labels]

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=300)

ax1.plot(thresholds, proc_det, marker='o', linewidth=2, linestyle='--', color='#e74c3c', label='Procedural Planner (Baseline)')
ax1.plot(thresholds, fals_det, marker='s', linewidth=2, linestyle='-', color='#2980b9', label='Falsifiable Graph (Ours)')
ax1.set_title('Negative Result Detection Rate', fontsize=12, fontweight='bold')
ax1.set_xlabel('Refutation Threshold ($\\tau$)', fontsize=11)
ax1.set_ylabel('Detection Rate', fontsize=11)
ax1.set_ylim(-0.05, 1.05)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(frameon=True, facecolor='white', edgecolor='none')

ax2.plot(thresholds, proc_fpr, marker='o', linewidth=2, linestyle='--', color='#e74c3c', label='Procedural Planner (Baseline)')
ax2.plot(thresholds, fals_fpr, marker='s', linewidth=2, linestyle='-', color='#2980b9', label='Falsifiable Graph (Ours)')
ax2.set_title('False Positive Rate', fontsize=12, fontweight='bold')
ax2.set_xlabel('Refutation Threshold ($\\tau$)', fontsize=11)
ax2.set_ylabel('False Positive Rate', fontsize=11)
ax2.set_ylim(-0.05, 1.05)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(frameon=True, facecolor='white', edgecolor='none')

plt.tight_layout()
plt.savefig('figure_results.png')
plt.savefig('figure_results.pdf')
print("Successfully generated figure_results.png and figure_results.pdf")
