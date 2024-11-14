Jenkins 是一个开源 CI&CD 平台，主要用于持续、自动的构建/测试软件项目、监控外部任务的运行。Jenkins 可以运行为系统软件包、Docker 或独立的 Java 程序。

Jenkins 插件通过升级中心（Update Center）进行发布。可以按以下步骤将 Jenkins 升级中心更改为 TUNA 镜像：

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
      url: "https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json"
</tmpl>

- 如果你需要在 Docker 构建时使用以便安装自定义插件，可以在 Dockerfile 中设置下列环境变量：

<tmpl>
ENV JENKINS_UC {{endpoint}}/updates
ENV JENKINS_UC_EXPERIMENTAL {{endpoint}}/updates/experimental
ENV JENKINS_UC_DOWNLOAD {{endpoint}}
ENV JENKINS_PLUGIN_INFO {{endpoint}}/updates/current/plugin-versions.json
</tmpl>

注意 TUNA 源的布局与官方源不同，因此若保留默认的 `JENKINS_UC_DOWNLOAD=$JENKINS_UC/download` 会导致插件下载失败。

注意这只会影响 Docker 构建时的插件更新，不会影响 Jenkins 运行时的插件更新。

参考文档：https://github.com/jenkinsci/docker/?tab=readme-ov-file#setting-update-centers
