import json
import dash
from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, ALL

# 载入元素周期表布局参数
with open("./periodicTableElement.json") as j:
    layout_elements = json.load(j)


max_x = max([item["tablecolumn18col"] for item in layout_elements])
max_y = max([item["tablerow18col"] for item in layout_elements])

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Store(id="click-event-collector"),
        dcc.Store(id="selected-element"),
        fac.AntdCenter(
            html.Div(
                [
                    html.Div(
                        html.Div(
                            item["symbol"],
                            id={"type": "element-block", "index": item["symbol"]},
                            style={
                                "display": "flex",
                                "alignItems": "center",
                                "justifyContent": "center",
                                "background": "#d9f7be",
                                "position": "absolute",
                                "inset": "2px",
                                "borderRadius": "4px",
                                "cursor": "pointer",
                                "userSelect": "none",
                            },
                            className="hover-zoom",
                        ),
                        style={
                            "position": "absolute",
                            "width": f"calc(100% / {max_x})",
                            "height": f"calc(100% / {max_y})",
                            "left": f"calc(100% * ( {item['tablecolumn18col'] - 1} / {max_x} ))",
                            "top": f"calc(100% * ( {item['tablerow18col'] - 1} / {max_y} ))",
                        },
                    )
                    for item in layout_elements
                ],
                id="elements-container",
                style={
                    "width": "75vw",
                    "height": f"calc(75vw * {max_y} / {max_x} )",
                    "position": "relative",
                },
            ),
        ),
        html.Div(
            id="show-current-selected-element",
            style={"textAlign": "center", "fontSize": 24},
        ),
    ],
    style={"padding": 50},
)


app.clientside_callback(
    """() => {
        // 更新最近被点击的元素
        return {
            element: window.dash_clientside.callback_context.triggered_id.index,
            timestamp: Date.now()
        };
    }""",
    Output("click-event-collector", "data"),
    Input({"type": "element-block", "index": ALL}, "n_clicks"),
    prevent_initial_call=True,
)

app.clientside_callback(
    """(clicked_element, origin_selected_element) => {
        let new_style = {
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "position": "absolute",
            "inset": "2px",
            "borderRadius": "4px",
            "cursor": "pointer",
            "userSelect": "none"
        };
        if (origin_selected_element === clicked_element.element) {
            // 还原先前选中的元素
            window.dash_clientside.set_props(
                {
                    type: "element-block",
                    index: clicked_element.element
                },
                {
                    style: {
                        ...new_style,
                        "background": "#d9f7be"
                    }
                }
            )

            return [
                null,
                `当前选中元素：无`
            ];
        } else {
            // 高亮新选中元素
            window.dash_clientside.set_props(
                {
                    type: "element-block",
                    index: clicked_element.element
                },
                {
                    style: {
                        ...new_style,
                        background: "#ff4d4f",
                        color: "white"
                    }
                }
            )
            if ( origin_selected_element ) {
                // 还原先前选中元素
                window.dash_clientside.set_props(
                    {
                        type: "element-block",
                        index: origin_selected_element
                    },
                    {
                        style: {
                            ...new_style,
                            "background": "#d9f7be"
                        }
                    }
                )
            }

            return [
                clicked_element.element,
                `当前选中元素：${clicked_element.element}`
            ];
        }
    }""",
    Output("selected-element", "data"),
    Output("show-current-selected-element", "children"),
    Input("click-event-collector", "data"),
    State("selected-element", "data"),
    prevent_initial_call=True,
)

if __name__ == "__main__":
    app.run(debug=True)
