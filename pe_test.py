import squarify
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

point_df = pd.read_csv(
    "input/PE.csv",index_col=False
)

sectors = list(set(point_df["GICS_INDUSTRY_GROUP_NAME"]))
sub_sectors = list(set(point_df["GICS_SUB_INDUSTRY_NAME"]))

print(sectors[0])
# point_df = point_df[point_df["GICS_INDUSTRY_GROUP_NAME"]==sectors[0]]
shapes = point_df["Name MC PE".split()]
shapes = shapes.sort_values("MC", ascending=False).reset_index(level=0)
# shapes = shapes.iloc[:100,:]
# print(shapes)
# print(shapes.head(10))
# exit()

norm = matplotlib.colors.Normalize(vmin=5, vmax=20)
shapes['color'] = shapes.PE.apply(lambda x: matplotlib.cm.Reds(-norm(x)+1))

plt.rcParams.update({'font.size': 6})
fig = plt.figure(figsize=(16, 9))
squarify.plot(
    sizes=shapes.MC,
    label=shapes.apply(lambda x: x.Name[:6] if x.MC > 5e8 else '', axis=1),
    color=shapes.color
)
# plt.rc('font', size=1)          # controls default text sizes
# plt.title(sectors[0])
ax = plt.axis('off')
fig.savefig("lse_heatmap.jpeg")