import re
import dash


class CustomDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        scripts = kwargs.pop("scripts")

        # 提取scripts部分符合条件的外部js资源
        external_scripts = re.findall('(<script src="http.*?"></script>)', scripts)

        # 将原有的script标签内容替换为带备用地址错误切换的版本
        for external_script in external_scripts:
            # 提取当前资源地址
            origin_library_src = re.findall('"(.*?)"', external_script)[0]
            # 抽取关键信息
            library_name, library_version, library_file = re.findall(
                "com/(.+)@(.+?)/(.+?)$", origin_library_src
            )[0]
            # 基于阿里cdn构建新的资源地址
            new_library_src = f"https://registry.npmmirror.com/{library_name}/{library_version}/files/{library_file}"

            scripts = scripts.replace(origin_library_src, new_library_src)

        return super(CustomDash, self).interpolate_index(scripts=scripts, **kwargs)


app = CustomDash(
    __name__,
    serve_locally=False,  # 设置为False后会自动从CDN加载相关静态资源
)
