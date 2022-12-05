# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/18 8:54
''
'''linxu进程与线程
    进程
        可执行程序的运行态
        操作系统调度的基本单位
        线程容器
        进程本身包含指令、数据等资源
        
    线程
        进程中被执行的最小单元
        cpu 调度的基本单位
        线程带有指令、数据等资
    
    进程的生命周期
        created sleep 100 ./linux_2_demo.py   创建
        ready                    
        running                  进行中
        waiting                  等待
        terminated kill killall  结束
    
    常用进程管理命令
        ps 进程列表快照
        top 交互式进程观测
        kill killall 结束进程
        fg 进程切换到前台
        bg 进程切换到后台
        ctrl z 挂起进程
    
    ps 命令
        unix 风格参数 ps -ef
        bsd 风格参数 ps aux
        gnu 风格参数 ps --pid pidlist
    
    #获得所有进程列表
        #UID        PID  PPID
        #C STIME TTY
        #TIME CMD
        ps -ef
        #获得所有进程列表，并提供更多可用数据
        #USER       PID
        #%CPU %MEM    VSZ   RSS TTY      STAT START
        #TIME COMMAND
        ps aux
        #自定义输出指标
        ps -o pid,ppid,psr,thcount,tid,cmd -MTOP
    
    
    进程状态
        D uninterruptible sleep (usually IO)
        R running or runnable (on run queue)
        S interruptible sleep (waiting for an event to complete)
        T stopped by job control signal
        t stopped by debugger during the tracing
        W paging (not valid since the 2.6.xx kernel)
        X dead (should never be seen)
        Z defunct (“zombie”) process, terminated but not reaped by its parent
    
    进程知识练习
        查看每一步进程状态
        #创建2个子进程，4个子线程
        python linux_2_demo.py 2 4 &
        jobs  任务
        fg   切到前台
        ctrl z
        bg    切到后台
    
    相关资料
        示例代码 https://ceshiren.com/t/topic/14248'''