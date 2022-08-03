# ROS 2 tracing experiments

A collection of scripts to perform analysis of trace events collected with [ros2_tracing].

**It implements a simple ROS 2 message flow analysis.** It is inspired and based on the work done
in the _[Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems][ros2-message-flow-analysis]_
paper. But instead of developing a custom Eclipse Trace Compass plugin for analysis and visualization (which is what the
paper does), **we use an extended version of [tracetools_analysis][pokusew_tracetools_analysis], Python scripts,
and [bokeh] for visualization**.


## Usage

TODO: document


## Related work

* [CARET] – much more advanced tool, also using Python, [bokeh] and building on the original [tracetools_analysis], but
  adding more instrumentation to rclcpp and DDS, supporting only galactic (as of Aug 8, 2022)
* [Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems][ros2-message-flow-analysis]


<!-- Links and References -->

[ros2_tracing]: https://github.com/ros2/ros2_tracing

[pokusew_tracetools_analysis]: https://github.com/pokusew/tracetools_analysis

[original_tracetools_analysis]: https://gitlab.com/ros-tracing/tracetools_analysis

[bokeh]: https://bokeh.org/

[ros2-message-flow-analysis]: https://github.com/christophebedard/ros2-message-flow-analysis

[CARET]: https://github.com/tier4/caret
