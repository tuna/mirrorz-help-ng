Jenkins 是一个开源 CI&CD 平台，主要用于持续、自动的构建/测试软件项目、监控外部任务的运行。Jenkins 可以运行为系统软件包、Docker 或独立的 Java 程序。

Jenkins 插件通过升级中心（Update Center）进行发布。

在 2025 年 3 月 30 日镜像站更新后，Jenkins 镜像源删除了 `update` 目录和 `update-center.json` 文件。Jenkins 通过官方维护的 Redirector 来将用户跳转到合适的镜像站，无需手动配置升级中心地址。

如果因为网络原因无法访问 Jenkins 官方升级中心，可以参考 https://github.com/lework/jenkins-update-center 生成特定镜像站点的 `update-center.json` 文件，并按先前的步骤修改 Jenkins 升级中心：

- 如果你已经安装了 Jenkins，可以在 系统管理->插件管理->高级设置 中更改升级中心地址为

<tmpl>
{{endpoint}}/updates/update-center.json
</tmpl>

- 如果你使用 Jenkins Configuration as Code（JCasC）进行配置，可以在配置文件中添加如下内容：

<tmpl z-lang="yaml">
jenkins:
  updateCenter:
    sites:
    - id: "default"
      url: "{{endpoint}}/updates/update-center.json"
</tmpl>

- 如果你需要在 Docker 构建时使用以便安装自定义插件，可以在 Dockerfile 中设置下列环境变量：

<tmpl>
ENV JENKINS_UC_DOWNLOAD {{endpoint}}
ENV JENKINS_PLUGIN_INFO {{endpoint}}/updates/current/plugin-versions.json
</tmpl>

注意，环境变量只会影响 Docker 构建时的插件更新，不会影响 Jenkins 运行时的插件更新。

参考文档：https://github.com/jenkinsci/docker/?tab=readme-ov-file#setting-update-centers
