import squarify
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

point_df = pd.read_csv(
    "input/ufo-scrubbed-geocoded-time-standardized.csv",
    names=[
        'observed',
        'city',
        'state',
        'country',
        'shape',
        'unknown',
        'duration',
        'description',
        'recorded',
        'lat',
        'lng'
    ]
)


shapes = point_df.groupby(["shape"]).size().reset_index()
shapes.columns = ['shape_name', 'total']
shapes = shapes.sort_values("total", ascending=False)
print(shapes.head(10))
# exit()

norm = matplotlib.colors.Normalize(vmin=shapes.total.min(), vmax=shapes.total.max())
shapes['color'] = shapes.total.apply(lambda x: matplotlib.cm.Reds(norm(x)))

fig = plt.figure(figsize=(16, 9))
squarify.plot(
    sizes=shapes.total,
    label=shapes.apply(lambda x: x.shape_name if x.total > 200 else '', axis=1),
    color=shapes.color
)
ax = plt.axis('off')

plt.show()