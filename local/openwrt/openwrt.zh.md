OpenWRT（曾用名 LEDE）是一款广泛应用于路由器的嵌入式操作系统。本站提供 OpenWRT 的包管理器 `opkg` 的 release 部分镜像。

本站不包含 snapshots 镜像，如果需要 snapshots，可以前往[校园网联合镜像站](https://mirrors.cernet.edu.cn/list/openwrt)寻找替代。

### 手工替换

登录到路由器，并编辑 `/etc/opkg/distfeeds.conf` 文件，将其中的 `http://downloads.openwrt.org` 替换为

<tmpl>
{{endpoint}}
</tmpl>

即可。

### 自动替换

执行如下命令自动替换

<tmpl z-lang="bash">
sed -i 's_https\?://downloads.openwrt.org_{{endpoint}}_' /etc/opkg/distfeeds.conf
</tmpl>

注：使用 HTTPS 可以有效避免国内运营商的缓存劫持，但需要另行安装 `libustream-openssl ca-bundle ca-certificates` 。
