import dash
import json
from dash import html
from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Input, Output
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

app = dash.Dash(__name__)

# 创建全局示例变量，作为定时任务的示例更新目标
GLOBAL_VAR = {
    "定时任务执行次数": 0,
    "当前时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}

app.layout = html.Div(
    [
        fac.AntdButton("获取最新信息", id="get-info", type="primary"),
        html.Pre(id="info"),
    ],
    style={"padding": 50},
)


@app.callback(Output("info", "children"), Input("get-info", "nClicks"))
def get_info(nClicks):
    return json.dumps(GLOBAL_VAR, indent=4, ensure_ascii=False)


def update_global_var():
    global GLOBAL_VAR
    GLOBAL_VAR = {
        "定时任务执行次数": GLOBAL_VAR["定时任务执行次数"] + 1,
        "当前时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    print("第{}次更新完成".format(GLOBAL_VAR["定时任务执行次数"]))


if __name__ == "__main__":
    scheduler.add_job(
        func=update_global_var, id="demo_job", trigger="interval", seconds=1
    )
    scheduler.start()  # 启动定时任务
    app.run(debug=False)
