import os
import sys

import datetime as dt
from typing import List, Optional
from typing import Tuple
from typing import Union

from bokeh.plotting import figure, DEFAULT_TOOLS, Figure
from bokeh.io import show
from bokeh.layouts import row
# DEFAULT_TOOLS = "pan,wheel_zoom,box_zoom,save,reset,help"
from bokeh.models import ColumnDataSource, \
    CrosshairTool, \
    HoverTool, \
    PanTool, \
    WheelZoomTool, \
    BoxZoomTool, \
    SaveTool, \
    UndoTool, \
    RedoTool, \
    ResetTool, \
    HelpTool, \
    Tool
from bokeh.models import DatetimeTickFormatter
from bokeh.models import Segment
import numpy as np
import pandas as pd

from tracetools_analysis.loading import load_file
from tracetools_analysis.processor.ros2 import Ros2Handler
from tracetools_analysis.utils.ros2 import Ros2DataModelUtil


# Functions to analyze the pre-processed data


# Functions to display data

def add_durations_to_figure(
    figure: Figure,
    segment_type: str,
    durations: List[Tuple[dt.datetime, dt.datetime, dt.timedelta]],
    color: str,
    line_width: int = 60,
    legend_label: Optional[str] = None
) -> None:
    for duration in durations:
        duration_begin, duration_end, duration_time = duration
        base_kwargs = dict()
        if legend_label:
            base_kwargs['legend_label'] = legend_label
        figure.line(
            x=[duration_begin, duration_end],
            y=[segment_type, segment_type],
            color=color,
            line_width=line_width,
            **base_kwargs,
        )


def add_markers_to_figure(
    figure: Figure,
    segment_type: str,
    times: List[dt.datetime],
    color: str,
    line_width: int = 60,
    legend_label: Optional[str] = None,
    size: int = 30,
    marker_type: str = 'diamond',
) -> None:
    for time in times:
        base_kwargs = dict()
        if legend_label:
            base_kwargs['legend_label'] = legend_label
        if marker_type == 'diamond':
            figure.diamond(
                x=[time],
                y=[segment_type],
                fill_color=color,
                line_color=color,
                size=size,
                **base_kwargs,
            )
        elif marker_type == 'plus':
            figure.plus(
                x=[time],
                y=[segment_type],
                fill_color=color,
                line_color=color,
                size=size,
                **base_kwargs,
            )
        else:
            assert False, 'invalid marker_type value'


def setup_visualization(title: str, x_axis_label: str, y_range: List[str]) -> Figure:
    # https://docs.bokeh.org/en/latest/docs/user_guide/tools.html
    crosshair_tool = CrosshairTool()
    hover_tool = HoverTool()
    pan_tool = PanTool()
    wheel_zoom_tool = WheelZoomTool()
    box_zoom_tool = BoxZoomTool()
    save_tool = SaveTool()
    undo_tool = UndoTool()
    redo_tool = RedoTool()
    reset_tool = ResetTool()
    help_tool = HelpTool()

    tools: List[Tool] = [
        crosshair_tool,
        hover_tool,
        pan_tool,
        wheel_zoom_tool,
        box_zoom_tool,
        save_tool,
        undo_tool,
        redo_tool,
        reset_tool,
        help_tool,
    ]

    fig = figure(
        title=title,
        x_axis_label=x_axis_label,
        y_range=y_range,
        plot_width=2000,
        plot_height=600,
        sizing_mode='stretch_both',
        tools=tools,
        active_drag=pan_tool,
        active_inspect=[],
        active_scroll=wheel_zoom_tool,
        # active_tap=None,
        active_multi=None,
    )
    fig.title.align = 'center'
    fig.title.text_font_size = '40px'
    fig.xaxis[0].formatter = DatetimeTickFormatter()
    fig.xaxis[0].axis_label_text_font_size = '30px'
    fig.yaxis[0].major_label_text_font_size = '25px'

    return fig
