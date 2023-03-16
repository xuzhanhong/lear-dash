from peewee import PostgresqlDatabase, CharField, IntegerField, FloatField, DateTimeField, CompositeKey, Model

# 连接到指定数据库
db = PostgresqlDatabase(
    'postgres',
    user='postgres',
    password='替换成你的密码',
    host='localhost',
    port=5432
)


class DemoTable1(Model):
    # 订单编号，主键
    order_id = IntegerField(primary_key=True)

    # 商品名称
    item_name = CharField()

    # 商品数量
    amount = IntegerField()

    # 商品单价
    unit_price = FloatField()

    class Meta:
        database = db
        db_table = 'demo_table1'


class DemoTable2(Model):
    # 部门，主键
    apartment = CharField()

    # 部门任务序号，主键
    task_id = IntegerField()

    # 任务开始时间
    task_start_datetime = DateTimeField()

    # 任务结束时间
    task_end_datetime = DateTimeField()

    # 任务内容描述
    task_description = CharField()

    class Meta:
        database = db
        db_table = 'demo_table2'
        primary_key = CompositeKey('apartment', 'task_id')


# 若库中不存在对应表则会新建否则会跳过
db.create_tables([DemoTable1, DemoTable2])

if __name__ == '__main__':
    pass
