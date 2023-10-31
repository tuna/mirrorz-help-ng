---
category: help
layout: help
mirrorid: ubuntu-ports
---

<!-- 本 markdown 从 tuna/mirrorz-help-ng 自动生成，如需修改请参阅该仓库 -->

<style>.z-help tmpl { display: none }</style>

<div class="z-wrap">
    <form class="z-form z-global" onchange="form_update(null)" onsubmit="return false">
        <div>
            <label for="e0a5cecb">线路选择</label>
            <select id="e0a5cecb" name="host">
                <option selected="selected" value="{{ site.url }}">自动</option>
                <option value="{{ site.urlv4 }}">IPv4</option>
                <option value="{{ site.urlv6 }}">IPv6</option>
            </select>
        </div>
        <div>
            <input id="144d763c" name="_scheme" type="checkbox" checked>
            <label for="144d763c">是否使用 HTTPS</label>
        </div>
        <div>
            <input id="4659e7da" name="_sudo" type="checkbox">
            <label for="4659e7da">是否使用 sudo</label>
        </div>
    </form>
</div>
{% raw %}
<div class="z-help"><h1>Ubuntu Ports 软件仓库</h1>
<p>对于 Ubuntu 不再支持的版本，请参考 <a href="../ubuntu-old-releases/">Ubuntu 旧版本帮助</a>。</p>
<p>Ubuntu 的软件源配置文件是 <code>/etc/apt/sources.list</code>。将系统自带的该文件做个备份，将该文件替换为下面内容，即可使用选择的软件源镜像。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"><div><label for="bLbwTE3B" title>Ubuntu 版本</label><select id="bLbwTE3B" name="release" title><option value="jammy">Ubuntu 22.04 LTS (jammy)</option><option value="lunar">Ubuntu 23.04 (lunar)</option><option value="kinetic">Ubuntu 22.10 (kinetic)</option><option value="focal">Ubuntu 20.04 LTS (focal)</option><option value="bionic">Ubuntu 18.04 LTS (bionic)</option><option value="xenial">Ubuntu 16.04 LTS (xenial) (EOL)</option><option value="trusty">Ubuntu 14.04 LTS (trusty) (EOL)</option></select></div><div><input id="xVob1Hss" name="src" title="源码源通常用于构建和调试，开启后影响更新速度" type="checkbox"/><label for="xVob1Hss" title="源码源通常用于构建和调试，开启后影响更新速度">启用源码源</label></div><div><input id="JTmIQR4q" name="proposed" title type="checkbox"/><label for="JTmIQR4q" title>启用 proposed</label></div><div><input id="2yqr0nT6" name="mirror_security" title="为了更及时地获得安全更新，不推荐使用镜像站安全更新软件源" type="checkbox"/><label for="2yqr0nT6" title="为了更及时地获得安全更新，不推荐使用镜像站安全更新软件源">强制安全更新使用镜像</label></div></form><pre class="z-code"></pre></div><tmpl z-input="release src proposed mirror_security" z-path="/etc/apt/sources.list">
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb {{endpoint}}/ {{release}} main restricted universe multiverse
{{src}}deb-src {{endpoint}}/ {{release}} main restricted universe multiverse
deb {{endpoint}}/ {{release}}-updates main restricted universe multiverse
{{src}}deb-src {{endpoint}}/ {{release}}-updates main restricted universe multiverse
deb {{endpoint}}/ {{release}}-backports main restricted universe multiverse
{{src}}deb-src {{endpoint}}/ {{release}}-backports main restricted universe multiverse

{{#mirror_security}}
deb {{endpoint}}/ {{release}}-security main restricted universe multiverse
{{src}}deb-src {{endpoint}}/ {{release}}-security main restricted universe multiverse
{{/mirror_security}}
{{^mirror_security}}
deb http://ports.ubuntu.com/ubuntu-ports/ {{release}}-security main restricted universe multiverse
{{src}}deb-src http://ports.ubuntu.com/ubuntu-ports/ {{release}}-security main restricted universe multiverse
{{/mirror_security}}

# 预发布软件源，不建议启用
{{proposed}}deb {{endpoint}}/ {{release}}-proposed main restricted universe multiverse
{{proposed}}{{src}}deb-src {{endpoint}}/ {{release}}-proposed main restricted universe multiverse
</tmpl>
<p>因镜像站同步有延迟，可能会导致生产环境系统不能及时检查、安装上最新的安全更新，不建议替换 security 源。</p><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIlVidW50dSBQb3J0cyBcdThmNmZcdTRlZjZcdTRlZDNcdTVlOTMiLCAiYmxvY2siOiBbInVidW50dS1wb3J0cyJdLCAiaW5wdXQiOiB7InJlbGVhc2UiOiB7Il8iOiAiVWJ1bnR1IFx1NzI0OFx1NjcyYyIsICJvcHRpb24iOiB7ImphbW15IjogeyJfIjogIlVidW50dSAyMi4wNCBMVFMgKGphbW15KSJ9LCAibHVuYXIiOiB7Il8iOiAiVWJ1bnR1IDIzLjA0IChsdW5hcikifSwgImtpbmV0aWMiOiB7Il8iOiAiVWJ1bnR1IDIyLjEwIChraW5ldGljKSJ9LCAiZm9jYWwiOiB7Il8iOiAiVWJ1bnR1IDIwLjA0IExUUyAoZm9jYWwpIn0sICJiaW9uaWMiOiB7Il8iOiAiVWJ1bnR1IDE4LjA0IExUUyAoYmlvbmljKSJ9LCAieGVuaWFsIjogeyJfIjogIlVidW50dSAxNi4wNCBMVFMgKHhlbmlhbCkgKEVPTCkifSwgInRydXN0eSI6IHsiXyI6ICJVYnVudHUgMTQuMDQgTFRTICh0cnVzdHkpIChFT0wpIn19fSwgInNyYyI6IHsiXyI6ICJcdTU0MmZcdTc1MjhcdTZlOTBcdTc4MDFcdTZlOTAiLCAibm90ZSI6ICJcdTZlOTBcdTc4MDFcdTZlOTBcdTkwMWFcdTVlMzhcdTc1MjhcdTRlOGVcdTY3ODRcdTVlZmFcdTU0OGNcdThjMDNcdThiZDVcdWZmMGNcdTVmMDBcdTU0MmZcdTU0MGVcdTVmNzFcdTU0Y2RcdTY2ZjRcdTY1YjBcdTkwMWZcdTVlYTYiLCAidHJ1ZSI6ICIiLCAiZmFsc2UiOiAiIyAifSwgInByb3Bvc2VkIjogeyJfIjogIlx1NTQyZlx1NzUyOCBwcm9wb3NlZCIsICJ0cnVlIjogIiIsICJmYWxzZSI6ICIjICJ9LCAibWlycm9yX3NlY3VyaXR5IjogeyJfIjogIlx1NWYzYVx1NTIzNlx1NWI4OVx1NTE2OFx1NjZmNFx1NjViMFx1NGY3Zlx1NzUyOFx1OTU1Y1x1NTBjZiIsICJub3RlIjogIlx1NGUzYVx1NGU4Nlx1NjZmNFx1NTNjYVx1NjVmNlx1NTczMFx1ODNiN1x1NWY5N1x1NWI4OVx1NTE2OFx1NjZmNFx1NjViMFx1ZmYwY1x1NGUwZFx1NjNhOFx1ODM1MFx1NGY3Zlx1NzUyOFx1OTU1Y1x1NTBjZlx1N2FkOVx1NWI4OVx1NTE2OFx1NjZmNFx1NjViMFx1OGY2Zlx1NGVmNlx1NmU5MCIsICJ0cnVlIjogbnVsbH19LCAibmFtZSI6ICJ1YnVudHUtcG9ydHMifQ==</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>