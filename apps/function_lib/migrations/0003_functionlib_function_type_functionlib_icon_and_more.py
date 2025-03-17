# Generated by Django 4.2.15 on 2025-03-13 07:21

from django.db import migrations, models

function_template = '''
INSERT INTO function_lib (create_time, update_time, id, name, "desc", code, input_field_list, user_id, is_active, permission_type, function_type, icon, init_field_list, init_params, template_id) VALUES ('2025-03-10 06:20:35.945414 +00:00', '2025-03-10 09:19:23.608026 +00:00', 'c75cb48e-fd77-11ef-84d2-5618c4394482', '博查AI', '从博查搜索任何信息和网页URL', e'def bocha_search(query, apikey):
    import requests
    import json
    url = "https://api.bochaai.com/v1/web-search"
    payload = json.dumps({
        "query": query,
        "Boolean": "true",
        "count": 8
    })

    headers = {
        "Authorization": "Bearer " + apikey, #鉴权参数，示例：Bearer xxxxxx，API KEY请先前往博查AI开放平台（https://open.bochaai.com）> API KEY 管理中获取。
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API请求失败: {response.status_code}, 错误信息: {response.text}")
        return (response.text)', '{"{\\"name\\": \\"query\\", \\"type\\": \\"string\\", \\"source\\": \\"reference\\", \\"is_required\\": true}"}', 'f0dd8f71-e4ee-11ee-8c84-a8a1595801ab', TRUE, 'PUBLIC', 'INTERNAL', '/src/assets/fx/bochaai/icon.png', '[{"attrs": {"type": "password", "maxlength": 200, "minlength": 1, "show-password": true, "show-word-limit": true}, "field": "apikey", "label": "apikey", "required": true, "input_type": "PasswordInput", "props_info": {"rules": [{"message": "apikey 为必填属性", "required": true}, {"max": 200, "min": 1, "message": "apikey长度在 1 到 200 个字符", "trigger": "blur"}]}, "default_value": "x", "show_default_value": false}]', '', NULL);
INSERT INTO function_lib (create_time, update_time, id, name, "desc", code, input_field_list, user_id, is_active, permission_type, function_type, icon, init_field_list, init_params, template_id) VALUES ('2025-02-26 03:36:48.187286 +00:00', '2025-03-11 07:23:46.123972 +00:00', 'e89ad2ae-f3f2-11ef-ad09-0242ac110002', 'Google Search', 'Google Web Search', e'def google_search(query, apikey, cx):
    import requests
    import json
    url = "https://customsearch.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": apikey,
        "cx": cx,
        "num": 10,  # 每次最多返回10条
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API请求失败: {response.status_code}, 错误信息: {response.text}")
        return (response.text)', '{"{\\"name\\": \\"query\\", \\"type\\": \\"string\\", \\"source\\": \\"reference\\", \\"is_required\\": true}"}', 'f0dd8f71-e4ee-11ee-8c84-a8a1595801ab', TRUE, 'PUBLIC', 'INTERNAL', '/src/assets/fx/google_search/icon.png', '[{"attrs": {"type": "password", "maxlength": 200, "minlength": 1, "show-password": true, "show-word-limit": true}, "field": "apikey", "label": "apikey", "required": true, "input_type": "PasswordInput", "props_info": {"rules": [{"message": "apikey 为必填属性", "required": true}, {"max": 200, "min": 1, "message": "apikey长度在 1 到 200 个字符", "trigger": "blur"}]}, "default_value": "x", "show_default_value": false}, {"attrs": {"maxlength": 200, "minlength": 1, "show-word-limit": true}, "field": "cx", "label": "cx", "required": true, "input_type": "TextInput", "props_info": {"rules": [{"message": "cx 为必填属性", "required": true}, {"max": 200, "min": 1, "message": "cx长度在 1 到 200 个字符", "trigger": "blur"}]}, "default_value": "x", "show_default_value": false}]', '', NULL);
INSERT INTO function_lib (create_time, update_time, id, name, "desc", code, input_field_list, user_id, is_active, permission_type, function_type, icon, init_field_list, init_params, template_id) VALUES ('2025-02-25 07:44:40.141515 +00:00', '2025-03-11 06:33:53.248495 +00:00', '5e912f00-f34c-11ef-8a9c-5618c4394482', 'LangSearch API', e'A Web Search API supporting natural language search
', e'
def langsearch(query, apikey):
    import json
    import requests
    
    url = "https://api.langsearch.com/v1/web-search"
    payload = json.dumps({
        "query": query,
        "summary": True,
        "freshness": "noLimit",
        "livecrawl": True,
        "count": 20
    })
    headers = {
        "Authorization": apikey,
        "Content-Type": "application/json"
    }
    # key从官网申请 https://langsearch.com/
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API请求失败: {response.status_code}, 错误信息: {response.text}")
        return (response.text)', '{"{\\"name\\": \\"query\\", \\"type\\": \\"string\\", \\"source\\": \\"reference\\", \\"is_required\\": true}"}', 'f0dd8f71-e4ee-11ee-8c84-a8a1595801ab', TRUE, 'PUBLIC', 'INTERNAL', '/src/assets/fx/langsearch/icon.png', '[{"attrs": {"type": "password", "maxlength": 200, "minlength": 1, "show-password": true, "show-word-limit": true}, "field": "apikey", "label": "apikey", "required": true, "input_type": "PasswordInput", "props_info": {"rules": [{"message": "apikey 为必填属性", "required": true}, {"max": 200, "min": 1, "message": "apikey长度在 1 到 200 个字符", "trigger": "blur"}]}, "default_value": "x", "show_default_value": false}]', '', NULL);
INSERT INTO function_lib (create_time, update_time, id, name, "desc", code, input_field_list, user_id, is_active, permission_type, function_type, icon, init_field_list, init_params, template_id) VALUES ('2025-03-17 07:37:54.620836 +00:00', '2025-03-17 07:37:54.620887 +00:00', 'bd1e8b88-0302-11f0-87bb-5618c4394482', 'PostgreSQL 查询', '', e'def queryPgSQL(dbname, user, password, host, port, query):
    import psycopg2
    import json
    from datetime import datetime

    # 自定义 JSON 序列化函数
    def default_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # 将 datetime 转换为 ISO 格式字符串
        raise TypeError(f"Type {type(obj)} not serializable")

    # 数据库连接信息
    conn_params = {
        "dbname": dbname,
        "user": user,
        "password": password,
        "host": host,
        "port": port
    }
    try:
        # 建立连接
        conn = psycopg2.connect(**conn_params)
        print("连接成功！")
        # 创建游标对象
        cursor = conn.cursor()
        # 执行查询语句
        cursor.execute(query)
        # 获取查询结果
        rows = cursor.fetchall()
        # 如果能查到数据代表不是第一次提问，或者用户名为“请稍等”代表是企业微信不请求接口
        if rows is None:
            return json.dumps({"status": "no", "data": []})
        else:
            columns = [desc[0] for desc in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
            # 转换为 JSON 格式
            json_result = json.dumps({"status": "yes", "data": result}, default=default_serializer,
                                     ensure_ascii=False)
            return json_result
    except Exception as e:
        print(f"发生错误：{e}")
        raise e
    finally:
        # 关闭游标和连接
        if cursor:
            cursor.close()
        if conn:
            conn.close()
', '{"{\"name\": \"query\", \"type\": \"string\", \"source\": \"reference\", \"is_required\": true}"}', 'f0dd8f71-e4ee-11ee-8c84-a8a1595801ab', true, 'PUBLIC', 'INTERNAL', '/src/assets/fx/postgresql/icon.png', '[{"attrs": {"maxlength": 200, "minlength": 1, "show-word-limit": true}, "field": "dbname", "label": "dbname", "required": true, "input_type": "TextInput", "props_info": {"rules": [{"message": "dbname 为必填属性", "required": true}, {"max": 200, "min": 1, "message": "dbname长度在 1 到 200 个字符", "trigger": "blur"}]}, "default_value": "x", "show_default_value": false}, {"attrs": {"maxlength": 200, "minlength": 1, "show-word-limit": true}, "field": "user", "label": "user", "required": true, "input_type": "TextInput", "props_info": {"rules": [{"message": "user 为必填属性", "required": true}, {"max": 200, "min": 1, "message": "user长度在 1 到 200 个字符", "trigger": "blur"}]}, "default_value": "x", "show_default_value": false}, {"attrs": {"type": "password", "maxlength": 200, "minlength": 1, "show-password": true, "show-word-limit": true}, "field": "password", "label": "password", "required": true, "input_type": "PasswordInput", "props_info": {"rules": [{"message": "password 为必填属性", "required": true}, {"max": 200, "min": 1, "message": "password长度在 1 到 200 个字符", "trigger": "blur"}]}, "default_value": "x", "show_default_value": false}, {"attrs": {"maxlength": 200, "minlength": 1, "show-word-limit": true}, "field": "host", "label": "host", "required": true, "input_type": "TextInput", "props_info": {"rules": [{"message": "host 为必填属性", "required": true}, {"max": 200, "min": 1, "message": "host长度在 1 到 200 个字符", "trigger": "blur"}]}, "default_value": "x", "show_default_value": false}, {"attrs": {"maxlength": 20, "minlength": 1, "show-word-limit": true}, "field": "port", "label": "port", "required": true, "input_type": "TextInput", "props_info": {"rules": [{"message": "port 为必填属性", "required": true}, {"max": 20, "min": 1, "message": "port长度在 1 到 20 个字符", "trigger": "blur"}]}, "default_value": "x", "show_default_value": false}]', null, null);

'''


class Migration(migrations.Migration):
    dependencies = [
        ('function_lib', '0002_functionlib_is_active_functionlib_permission_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='functionlib',
            name='function_type',
            field=models.CharField(choices=[('INTERNAL', '内置'), ('PUBLIC', '公开')],
                                   default='PUBLIC', max_length=20, verbose_name='函数类型'),
        ),
        migrations.AddField(
            model_name='functionlib',
            name='icon',
            field=models.CharField(default='/ui/favicon.ico', max_length=256,
                                   verbose_name='函数库icon'),
        ),
        migrations.AddField(
            model_name='functionlib',
            name='init_field_list',
            field=models.JSONField(default=list, verbose_name='启动字段列表'),
        ),
        migrations.AddField(
            model_name='functionlib',
            name='init_params',
            field=models.CharField(max_length=102400, null=True, verbose_name='初始化参数'),
        ),
        migrations.AddField(
            model_name='functionlib',
            name='template_id',
            field=models.UUIDField(default=None, null=True, verbose_name='模版id'),
        ),
        migrations.RunSQL(function_template)
    ]
