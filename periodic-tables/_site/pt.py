""" Periodic table plots """
import pandas as pd
from bokeh import palettes
from bokeh.io import output_file, show, export_png
from bokeh.models import ColorBar
from bokeh.plotting import figure
from bokeh.sampledata.periodic_table import elements
from bokeh.transform import dodge, linear_cmap


def main(data, property="Cohesive energy"):
    """
Main program
https://docs.bokeh.org/en/latest/docs/gallery/periodic.html
    """
    prop_dict = {
        "Cohesive energy": {
            "column_name": "Per Atom",
            "units": " (eV/atom)"
        }
    }
    properties = prop_dict[property]

    output_file("periodic.html")
    periods = [str(x) for x in range(1, 11)]
    groups = [str(x) for x in range(1, 19)]
    df = elements.merge(right=data, how="left", on="name")
    df["group"] = df["group"].astype(str)
    df["period"] = [periods[x - 1] for x in df.period]

    # update period for lanthanides and actinides
    period = []
    for ind, row in df.iterrows():
        if row.metal == "lanthanoid" or row.metal == "actinoid":
            period.append(int(row.period) + 3)
        else:
            period.append(int(row.period))
    period = [str(x) for x in period]
    df["period"] = period

    # update group for lanthanides and actinides
    count = 0
    group = []
    for ind, row in df.iterrows():
        if int(row.period) >= 8:
            group.append(count % 14 + 3)
            count += 1
        else:
            group.append(int(row.group))
    group = [str(x) for x in group]
    df["group"] = group

    TOOLTIPS = [
        ("Name", "@name"),
        ("Atomic number", "@{atomic number}"),
        (property, "@{" + properties["column_name"] + "}"),
    ]

    p = figure(title=property + properties["units"], plot_width=1000, plot_height=int(1000 / 18 * 10),
               x_range=groups, y_range=list(reversed(periods)),
               tools="hover", toolbar_location=None, tooltips=TOOLTIPS)

    low = df[properties["column_name"]].min()
    high = df[properties["column_name"]].max()
    color_mapper = linear_cmap(properties["column_name"], palette=palettes.Viridis256, low=low, high=high)
    r = p.rect("group", "period", 0.95, 0.95, source=df, fill_alpha=0.6, color=color_mapper)
    color_bar = ColorBar(color_mapper=color_mapper["transform"])
    p.add_layout(color_bar, 'right')

    text_props = {"source": df, "text_align": "center", "text_baseline": "middle"}

    x = dodge("group", 0.0, range=p.x_range)
    y = dodge("period", 0.0, range=p.y_range)
    x1 = dodge("group", 0.0, range=p.x_range)
    y1 = dodge("period", 0.3, range=p.y_range)
    x2 = dodge("group", 0.0, range=p.x_range)
    y2 = dodge("period", -0.3, range=p.y_range)

    p.text(x=x, y=y, text="symbol", text_font_style="bold", **text_props)

    p.text(x=x1, y=y1, text="atomic number", text_font_size="10px", **text_props)

    df["trend"] = df[properties["column_name"]].apply(lambda x: "{:.2f}".format(x))
    p.text(x=x2, y=y2, text="trend", text_font_size="10px", **text_props)

    p.outline_line_color = None
    p.grid.grid_line_color = None
    p.axis.axis_line_color = None
    p.axis.major_tick_line_color = None
    p.axis.major_label_standoff = 0
    p.hover.renderers = [r]  # only hover element boxes

    export_png(p, filename="cept.png")
    # show(p)


if __name__ == "__main__":
    path = "/Users/robertwexler/Dropbox (Princeton)/ML-for-TWS/ml/data/reference/Cohesive-energies" \
           "/element_cohesive_energies.csv"
    data = pd.read_csv(path)
    data.rename(columns={"Element": "name"}, inplace=True)
    main(data)
