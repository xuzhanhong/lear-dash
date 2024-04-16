import json
import uuid
from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State, ALL, MATCH

from server import app

# 载入元素周期表布局参数
with open("./periodicTableElement.json") as j:
    layout_elements = json.load(j)


max_x = max([item["tablecolumn18col"] for item in layout_elements])
max_y = max([item["tablerow18col"] for item in layout_elements])


def render(color: str = "#d9f7be"):
    new_uuid = str(uuid.uuid4())

    return html.Div(
        [
            fac.AntdTitle("组件" + new_uuid, level=3),
            dcc.Store(id="componnet-uuid", data=new_uuid),
            dcc.Store(id="componnet-color", data=color),
            dcc.Store(id={"type": "click-event-collector", "key": new_uuid}),
            dcc.Store(id={"type": "selected-element", "key": new_uuid}),
            fac.AntdCenter(
                html.Div(
                    [
                        html.Div(
                            html.Div(
                                item["symbol"],
                                id={
                                    "type": "element-block",
                                    "key": new_uuid,
                                    "index": item["symbol"],
                                },
                                style={
                                    "display": "flex",
                                    "alignItems": "center",
                                    "justifyContent": "center",
                                    "background": color,
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
                    id={"type": "elements-container", "key": new_uuid},
                    style={
                        "width": "75vw",
                        "height": f"calc(75vw * {max_y} / {max_x} )",
                        "position": "relative",
                    },
                ),
            ),
            html.Div(
                id={"type": "show-current-selected-element", "key": new_uuid},
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
    Output({"type": "click-event-collector", "key": MATCH}, "data"),
    Input({"type": "element-block", "key": MATCH, "index": ALL}, "n_clicks"),
    prevent_initial_call=True,
)

app.clientside_callback(
    """(clicked_element, origin_selected_element, componnet_uuid, componnet_color) => {
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
                    key: componnet_uuid,
                    index: clicked_element.element
                },
                {
                    style: {
                        ...new_style,
                        "background": componnet_color
                    }
                }
            )

            return [
                null,
                `组件${componnet_uuid}当前选中元素：无`
            ];
        } else {
            // 高亮新选中元素
            window.dash_clientside.set_props(
                {
                    type: "element-block",
                    key: componnet_uuid,
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
                        key: componnet_uuid,
                        index: origin_selected_element
                    },
                    {
                        style: {
                            ...new_style,
                            "background": componnet_color
                        }
                    }
                )
            }

            return [
                clicked_element.element,
                `组件${componnet_uuid}当前选中元素：${clicked_element.element}`
            ];
        }
    }""",
    Output({"type": "selected-element", "key": MATCH}, "data"),
    Output({"type": "show-current-selected-element", "key": MATCH}, "children"),
    Input({"type": "click-event-collector", "key": MATCH}, "data"),
    State({"type": "selected-element", "key": MATCH}, "data"),
    State("componnet-uuid", "data"),
    State("componnet-color", "data"),
    prevent_initial_call=True,
)
