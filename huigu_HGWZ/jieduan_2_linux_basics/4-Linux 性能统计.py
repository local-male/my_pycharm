# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/11/19 11:34
''
'''Linux 性能统计
    性能测试
    性能分析
    
    性能统计知识
        系统级性能数据分析
        进程级别性能数据分析
    
    常用性能指标
        cpu 代表算法的高效性
        mem 代表数据结构的使用合理性
        net io 等更多指标
        net io 的不合理使用同样会在 cpu 和 mem 上体现出影响，所以我们今天重点介绍 3 个指标，cpu mem 与 net
    
    统计方法
        临时性分析 命令交互
        系统性分析 promethus grafana
        
    cpu 的关键指标
        cat /proc/cpuinfo  cpu信息
        cpu 利用率 进程的 cpu 利用情况
        load average 系统负载情况
        ps 命令的 cpu 是平均 cpu 利用率，不适合做性能分析
    
    常用命令
        free -m  -h
        ps
        top
    
    内存使用数据缓存：cat /proc/meminfo
    进程级别的内存分析：ps -e -o uid,pid,ppid,pcpu,pmem,rss,vsz,comm  --sort -%mem | head -10
    查看网络连接：netstat -tnp | head -10
    数据统计：netstat -tlnp | awk 'NR>2{print $NF}'| sort | uniq -c | sort -nr
    '''