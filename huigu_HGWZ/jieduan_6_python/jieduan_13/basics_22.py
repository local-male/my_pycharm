# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script �����Լ���ģ��
# ��ѯ���� type check �ɶ�Ӧ�޸Ĵ���ȼ� ����error warning
# ��ǰʱ�� 2022/10/22 13:19
''
'''���ÿ� sys
    sys ����
    �� Python �Դ�������ģ��
    ���� Python ����������������'''

# ����sysģ��
import sys
# �鿴sysģ������ĵ�
#help(sys)
# �鿴sysģ������Ժͷ���
#print(dir(sys))

#���ӣ�https://peps.python.org/pep-0263/

'''sys ��������
    sys.version������ Python �������汾
    sys.platform�����ز���ϵͳƽ̨����
    sys.argv�������ⲿ����򴫵ݵĲ���
    sys.modules�������ѵ����ģ����Ϣ
    sys.path�����ص���������·���б�'''

"""sysģ�鳣������"""
# ����Python �������汾
print(sys.version)
# ���ز���ϵͳƽ̨����
print(sys.platform)
# �����ⲿ����򴫵ݵĲ���
print(sys.argv)
# �����ѵ����ģ����Ϣ
print(sys.modules)
print(sys.modules.keys())
# ���ص���������·���б�
print(sys.path)