from datetime import datetime
import os
import sys

import pandas
import plotly.graph_objects as go


def generate(user):
    df = pandas.read_csv(f"data/{user}.csv")

    image_root = f"images/{user}/"
    os.makedirs(image_root, exist_ok=True)

    for i in range(1, len(df["race number"] + 1)):
        datetime_obj = datetime.strptime(df["date"][i], "%Y-%m-%d")
        fig = go.Figure(
            data=go.Scatter(
                y=df["wpm"][0:i],
                x=df["race number"][0:i],
                mode="markers",
                marker=dict(
                    size=8,
                    color=df["acc"],
                    colorscale="Magma",
                    showscale=True,
                    colorbar=dict(title="acc"),
                ),
            )
        )
        fig.update_layout({"xaxis": {"title": "race #"}, "yaxis": {"title": "speed (WPM)"}})
        fig.update_layout(
            annotations=[
                go.layout.Annotation(
                    x=1,
                    y=1,
                    xref="paper",
                    yref="paper",
                    xanchor="right",
                    yanchor="top",
                    text=datetime_obj.strftime("%B %Y"),
                    font=go.layout.annotation.Font(size=20),
                    showarrow=False,
                )
            ]
        )
        fig.write_image(image_root + f"{i:0>6}.jpg")


if __name__ == "__main__":
    generate(sys.argv[1])
