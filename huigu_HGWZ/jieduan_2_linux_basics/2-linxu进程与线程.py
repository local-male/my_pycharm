# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script �����Լ���ģ��
# ��ѯ���� type check �ɶ�Ӧ�޸Ĵ���ȼ� ����error warning
# ��ǰʱ�� 2022/11/18 8:54
''
'''linxu�������߳�
    ����
        ��ִ�г��������̬
        ����ϵͳ���ȵĻ�����λ
        �߳�����
        ���̱������ָ����ݵ���Դ
        
    �߳�
        �����б�ִ�е���С��Ԫ
        cpu ���ȵĻ�����λ
        �̴߳���ָ����ݵ���
    
    ���̵���������
        created sleep 100 ./linux_2_demo.py   ����
        ready                    
        running                  ������
        waiting                  �ȴ�
        terminated kill killall  ����
    
    ���ý��̹�������
        ps �����б����
        top ����ʽ���̹۲�
        kill killall ��������
        fg �����л���ǰ̨
        bg �����л�����̨
        ctrl z �������
    
    ps ����
        unix ������ ps -ef
        bsd ������ ps aux
        gnu ������ ps --pid pidlist
    
    #������н����б�
        #UID        PID  PPID
        #C STIME TTY
        #TIME CMD
        ps -ef
        #������н����б����ṩ�����������
        #USER       PID
        #%CPU %MEM    VSZ   RSS TTY      STAT START
        #TIME COMMAND
        ps aux
        #�Զ������ָ��
        ps -o pid,ppid,psr,thcount,tid,cmd -MTOP
    
    
    ����״̬
        D uninterruptible sleep (usually IO)
        R running or runnable (on run queue)
        S interruptible sleep (waiting for an event to complete)
        T stopped by job control signal
        t stopped by debugger during the tracing
        W paging (not valid since the 2.6.xx kernel)
        X dead (should never be seen)
        Z defunct (��zombie��) process, terminated but not reaped by its parent
    
    ����֪ʶ��ϰ
        �鿴ÿһ������״̬
        #����2���ӽ��̣�4�����߳�
        python linux_2_demo.py 2 4 &
        jobs  ����
        fg   �е�ǰ̨
        ctrl z
        bg    �е���̨
    
    �������
        ʾ������ https://ceshiren.com/t/topic/14248'''