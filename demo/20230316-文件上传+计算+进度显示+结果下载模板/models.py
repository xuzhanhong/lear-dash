from peewee import (
    SqliteDatabase,
    CharField,
    DateTimeField,
    FloatField,
    Model
)

db = SqliteDatabase('./tasks.db')


class Tasks(Model):

    # 任务id，主键
    task_id = CharField(primary_key=True)

    # 上传文件路径id
    upload_id = CharField()

    # 上传文件名
    upload_file_name = CharField()

    # 任务创建时间
    create_datetime = DateTimeField()

    # 任务进度
    task_progress = FloatField()

    # 任务完成时间
    complete_datetime = DateTimeField(null=True)

    # 计算结果下载路径id
    download_id = CharField(null=True)

    class Meta:

        database = db
        table_name = 'tasks'


db.create_tables([Tasks])
