import matplotlib as mpl
import matplotlib.pyplot as plt

import radar

import demodata


colors = mpl.rcParams['axes.color_cycle']


def make_autos_radar_plot(figure, gs, pddata):
    min_data = pddata.groupby("make", sort=True).min()
    max_data = pddata.groupby("make", sort=True).max()
    mean_data = pddata.groupby("make", sort=True).mean()
    projection = radar.RadarAxes(spoke_count=len(mean_data.columns))
    subplot_axes = [plt.subplot(x, projection=projection) for x in gs]

    for i, make in enumerate(demodata.get_make_names(pddata)):
        axes = subplot_axes[i]
        axes.set_title(
            make.title(), weight='bold', size='large', position=(0.5, 1.1),
            horizontalalignment='center', verticalalignment='center')
        for (color, alpha, data) in zip([1, 2, 0],
                                        [0.2, 0.3, 0.4],
                                        [max_data, mean_data, min_data]):
            axes.fill(axes.radar_theta, data.loc[make], color=colors[color],
                      alpha=alpha)
            axes.plot(axes.radar_theta, data.loc[make], color=colors[color])
        axes.set_varlabels([x.replace(" ", "\n") for x in mean_data.columns])
        axes.set_rgrids([0.2, 0.6, 0.8])
    return subplot_axes


def make_autos_mpg_plot(figure, gs, pddata):
    data = demodata.get_numeric_data(pddata)
    axes = plt.subplot(gs[0, 0])
    axes.set_title("Ranges of City and Highway MPG", fontsize=20)
    axes.scatter(data["make"], data["highway mpg"], c=colors[3],
                 s=200, alpha=0.4)
    axes.scatter(data["make"], data["city mpg"], c=colors[0],
                 s=200, alpha=0.4)
    axes.set_xticks(range(0, 13))
    axes.set_xticklabels(demodata.get_make_labels(pddata))
    axes.set_xlabel("Make", fontsize=16)
    axes.set_ylabel("MPG", fontsize=16)
    city_patch = mpl.patches.Patch(color=colors[0], alpha=0.7, label="City")
    highway_patch = mpl.patches.Patch(color=colors[3], alpha=0.7, label="Highway")
    axes.legend(handles=[city_patch, highway_patch])
    return axes
