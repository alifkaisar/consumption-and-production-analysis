import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd


def bar_plot(x, y, color, ylabel):
    fig = plt.figure(figsize=(12, 8), dpi=200)

    with sns.axes_style("darkgrid"):
        sns.barplot(x=x, y=y, color=color)

    plt.xticks(rotation=45)
    plt.xlabel(" ")
    plt.ylabel(ylabel, fontsize=15)

    return fig


def recreate_df(data_frame, columns_name: list, unselected_columns: int):
    """
    Change a selected column and its value to a new column which then merges the unselected columns and creates
    a new data frame
    """
    column_list = data_frame.columns.tolist()

    data = []

    for column in column_list[unselected_columns::]:
        for data_groups in data_frame[column_list[:unselected_columns:] + [column]].values.tolist():
            data.append([column] + data_groups)

    return pd.DataFrame(data, columns=columns_name)


def barh_plotly(data_frame, x, y, group):
    fig = px.bar(
        data_frame,
        x=x,
        y=y,
        orientation="h",
        barmode="group",
        color=group,
    )
    fig.update_layout(height=600)
    fig.update_xaxes(title_font={"size": 20})
    fig.update_yaxes(title_font={"size": 20})

    return fig


def heatmap_plotly(data_frame):
    fig = px.imshow(data_frame, color_continuous_scale="ice", aspect="auto")
    fig.update_layout(height=800)
    fig.update_xaxes(tickangle=-90)

    return fig
