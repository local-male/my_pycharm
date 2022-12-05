# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 查询输入 type check 可对应修改错误等级 例：error warning
# 当前时间 2022/12/4 8:23
''
'''git基本命令
        查看git版本
            windows：cmd中输入命令  git --version
            mac：终端输入命令  git  --version
        
        git环境配置
            先到github或者gitee上注册一个账号
            配置全局账号
                配置用户名：git config --global user.name '用户名'
                配置邮箱：git config --global user.email '邮箱'
            验证配置结果：git config --global --list
            
        生成ssh key
            ssh-keygen -t rsa -C '邮箱'
            连敲三次回车
            到对应的目录下找到生成的公钥（id_rsa.pub）和私钥（id_rsa）
        
        pycharm配置git：在file->setting中搜索git，在git路径点击test，
            出现版本号即可，保存退出；（未出现需手动输入git路径）
        
        '''
'''大纲
    git常用命令
    git log 分析与检索
    git分支管理
    分支开发主干发布模式
    
    git安装
        linux:sudo apt-get install git
        mac:brew install git
        windows:https://git-scm.com/downloads
    配置用户名：
        git config --global user.name '用户名'
        配置邮箱：git config --global user.email '邮箱'
        git config -l 查看配置信息
    创建仓库：在文件根目录下（可自己任选） 执行： git init 
        提交文件至临时仓库：git  add  文件
            查看操作结果：  git status
            查看修改内容：  git diff
        提交至仓库： git commit -m '注释'
    git log 文件上传记录（从哪个区到哪个区）
    cd ~/.ssh  切换至ssh目录,查看密钥
    git rebase 合并分支   git rebase -i 文件名
        pick:保留该commit,缩写p
        reword:保留该commit，但我需要修改该commit的注释 ，缩写r
        edit:保留该commit，但我要停下来修改该提交（不仅仅是修改注释），缩写e
        squash：将该commit和前一个commit合并，缩写s
        fixup:将该commit和前一个commit合并，但我不要保留该提交的注释信息，缩写f
        exec:执行shell命令，缩写：x
        drop：我要丢弃该commit，缩写d
    '''
'''
            ------------------------------本地---------------------       - ---云端-----
                 git add 文件        git commit -m '注释'      git push
            工作区------------>临时仓库------------------->仓库------------>github/gitlab/gitee
                <-----------  stage <-----------------master<-----------
                                        git reset --head HEAD^  git pull
git checkout<--git reset HEAD <文件>     直接全部还原带上一次的记录     
还原到上一次     从临时仓库还原到上一次
的记录           的记录，工作区不变
            
'''
'''分支管理原则
        创建分支
            git branch  分支名称
        切换分支
            git checkout 分支名称
        查看当前分支
            git branch
        分支合并
            切换到master分支，git merge dev 将dev分支合并到master分支
        删除分支
            git branch -d 分支名称
           
'''
'''pycharm git配置及使用
    配置公钥
        找到id_rsa.pub,复制内容
        github->我的头像->settings
        ssh and gpg keys
        new ssh key
        粘贴公钥，点击add ssh key
        
    pycharm中github添加token认证，从github-》setting-》developer setting->new新建 全选--》保存
    
    git add 文件 后，在log中点击对应存档右键，选择resetxx,选择hard 返回；
    切换分支，右下角直接点击切换；合并分支，先切换分支，在选择checkout；
    不要push .idea，每个人的环境不一样
'''