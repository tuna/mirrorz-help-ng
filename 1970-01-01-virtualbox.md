---
category: help
layout: help
mirrorid: virtualbox
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
<div class="z-help"><h1>VirtualBox 软件仓库</h1>
<p><a href="https://www.virtualbox.org/">Oracle Virtualbox</a> VirtualBox 是一款开源虚拟机软件。由德国 Innotek 公司开发，Sun Microsystems 公司出品。使用 Qt 编写，在 Sun 被 Oracle 收购后正式更名成 Oracle VM VirtualBox。采用 GPL 协议开源。</p>
<h2>Microsoft Windows</h2>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl>
# Windows 最新版
{{endpoint}}/virtualbox-Win-latest.exe
</tmpl>
<h2>Macintosh OS X</h2>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl>
# OS X 最新版
{{endpoint}}/virtualbox-osx-latest.dmg
</tmpl>
<h1>Linux</h1>
<h2>通过编译好的二进制包安装</h2>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl>
{{endpoint}}
</tmpl>
<p>访问该镜像下最新的目录（例如<code>5.0.24</code>），找到名为 发行版名称~发行代号~架构 的文件。</p>
<p>如 <code>virtualbox-5.0_5.0.24-108355~Ubuntu~xenial_i386.deb</code> 下载安装即可。</p>
<p>目前支持的系统有：</p>
<ul>
<li>Ubuntu</li>
<li>Debian</li>
<li>Fedora</li>
<li>openSUSE</li>
<li>SUSE Linux Enterprise Server</li>
<li>Oracle Linux / Red Hat Enterprise Linux / CentOS</li>
</ul>
<p>如果您所使用的发行版不在上述列表之内，请下载通用的<code>run</code>文件（例如<code>VirtualBox-5.0.24-108355-Linux_x86.run</code>），然后使用 <code>chmod +x</code> 给予执行权限后，直接安装即可。</p>
<h3>通过包管理器安装</h3>
<h4>Debian / Ubuntu 用户</h4>
<p>首先信任 Virtualbox 的 GPG 公钥：</p>
<p>对于 Debian 8 和 Ubuntu 16.04 及以上：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | {{sudo}}apt-key add -
</tmpl>
<p>其他版本</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | {{sudo}}apt-key add -
</tmpl>
<p>再选择你的 Debian/Ubuntu 版本，将文本框中内容写进<code>/etc/apt/sources.list.d/virtualbox.list</code></p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"><div><label for="491c8709" title>发行版</label><select id="491c8709" name="release" title><option value="bullseye">Debian 11 (bullseye)</option><option value="buster">Debian 10 (buster)</option><option value="stretch">Debian 9 (stretch) (EOL)</option><option value="jessie">Debian 8 (jessie) (EOL)</option><option value="jammy">Ubuntu 22.04 LTS (jammy)</option><option value="focal">Ubuntu 20.04 LTS (focal)</option><option value="bionic">Ubuntu 18.04 LTS (bionic)</option><option value="xenial">Ubuntu 16.04 LTS (xenial) (EOL)</option><option value="trusty">Ubuntu 14.04 LTS (trusty) (EOL)</option></select></div></form><pre class="z-code"></pre></div><tmpl z-input="release" z-path="/etc/apt/sources.list.d/virtualbox.list">
deb {{endpoint}}/apt/ {{release}} contrib
</tmpl>
<p>安装 VirtualBox:</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}apt-get update
{{sudo}}apt-get install virtualbox
# 此时会列出具体可用版本，选择所需版本安装
</tmpl>
<h3>RHEL/CentOS 用户</h3>
<p>新建 <code>/etc/yum.repos.d/virtualbox.repo</code>，内容为</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="ini" z-path="/etc/yum.repos.d/virtualbox.repo">
[virtualbox]
name=Virtualbox Repository
baseurl={{endpoint}}/rpm/el$releasever/
gpgcheck=0
enabled=1
</tmpl>
<p>刷新缓存并安装 <code>virtualbox</code> 即可。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}yum makecache
{{sudo}}yum search VirtualBox
# 此时会列出具体可用版本，选择所需版本安装即可
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIlZpcnR1YWxCb3ggXHU4ZjZmXHU0ZWY2XHU0ZWQzXHU1ZTkzIiwgImJsb2NrIjogWyJ2aXJ0dWFsYm94Il0sICJpbnB1dCI6IHsicmVsZWFzZSI6IHsiXyI6ICJcdTUzZDFcdTg4NGNcdTcyNDgiLCAib3B0aW9uIjogeyJidWxsc2V5ZSI6IHsiXyI6ICJEZWJpYW4gMTEgKGJ1bGxzZXllKSJ9LCAiYnVzdGVyIjogeyJfIjogIkRlYmlhbiAxMCAoYnVzdGVyKSJ9LCAic3RyZXRjaCI6IHsiXyI6ICJEZWJpYW4gOSAoc3RyZXRjaCkgKEVPTCkifSwgImplc3NpZSI6IHsiXyI6ICJEZWJpYW4gOCAoamVzc2llKSAoRU9MKSJ9LCAiamFtbXkiOiB7Il8iOiAiVWJ1bnR1IDIyLjA0IExUUyAoamFtbXkpIn0sICJmb2NhbCI6IHsiXyI6ICJVYnVudHUgMjAuMDQgTFRTIChmb2NhbCkifSwgImJpb25pYyI6IHsiXyI6ICJVYnVudHUgMTguMDQgTFRTIChiaW9uaWMpIn0sICJ4ZW5pYWwiOiB7Il8iOiAiVWJ1bnR1IDE2LjA0IExUUyAoeGVuaWFsKSAoRU9MKSJ9LCAidHJ1c3R5IjogeyJfIjogIlVidW50dSAxNC4wNCBMVFMgKHRydXN0eSkgKEVPTCkifX19fSwgIm5hbWUiOiAidmlydHVhbGJveCJ9</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
