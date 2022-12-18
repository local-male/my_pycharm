# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/6/18 20:34
import pytest
import yaml

class Test_yaml:
    @pytest.mark.parametrize('env',yaml.safe_load(open('./env.yaml',encoding='utf-8')))
    def test_yaml(self,env):
        if 'test' in env:
            print('测试环境')
            print('ip是：{}'.format(env['test']))
        elif 'develop' in env:
            print('开发环境')
            print('ip是：{}'.format(env['develop']))
            print(env)
        else:
            print('正式环境')

    def test_yaml_file(self):
        print(yaml.safe_load(open('./env.yaml',encoding='utf-8')))