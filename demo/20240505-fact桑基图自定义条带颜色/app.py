import dash
from dash import html
import feffery_antd_charts as fact

app = dash.Dash(__name__)

demo_data = [
    {"source": "首次打开", "target": "首页 UV", "value": 160},
    {"source": "结果页", "target": "首页 UV", "value": 40},
    {"source": "验证页", "target": "首页 UV", "value": 10},
    {"source": "我的", "target": "首页 UV", "value": 10},
    {"source": "朋友", "target": "首页 UV", "value": 8},
    {"source": "其他来源", "target": "首页 UV", "value": 27},
    {"source": "首页 UV", "target": "理财", "value": 30},
    {"source": "首页 UV", "target": "扫一扫", "value": 40},
    {"source": "首页 UV", "target": "服务", "value": 35},
    {"source": "首页 UV", "target": "蚂蚁森林", "value": 25},
    {"source": "首页 UV", "target": "跳失", "value": 10},
    {"source": "首页 UV", "target": "借呗", "value": 30},
    {"source": "首页 UV", "target": "花呗", "value": 40},
    {"source": "首页 UV", "target": "其他流向", "value": 45},
]

app.layout = html.Div(
    [
        fact.AntdSankey(
            data=demo_data,
            sourceField="source",
            targetField="target",
            weightField="value",
            nodeWidthRatio=0.008,
            nodePaddingRatio=0.03,
            nodeDraggable=True,
            height=600,
            color={
                "func": """(e) => {
                    if ( e.source === '首页 UV' ) {
                        if ( e.target === '蚂蚁森林' ) {
                            return '#389e0d';
                        }
                        return '#d9f7be';
                    } else if ( e.source === '首次打开' ) {
                        return '#40a9ff';
                    }
                    return '#bae7ff';
                }"""
            },
        )
    ],
    style={"padding": 50},
)

if __name__ == "__main__":
    app.run(debug=True)
