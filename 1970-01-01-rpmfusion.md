---
category: help
layout: help
mirrorid: rpmfusion
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
<div class="z-help"><h1>RPMFusion 软件仓库</h1>
<h3>安装基础包</h3>
<p>首先安装提供基础配置文件和 GPG 密钥的 <code>rpmfusion-*.rpm</code>。</p>
<h4>Fedora 用户</h4>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}yum install --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
</tmpl>
<p>或者如下直接用镜像中的 rpm 包：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}yum install --nogpgcheck {{endpoint}}/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm {{endpoint}}/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
</tmpl>
<h4>CentOS/RHEL 用户</h4>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"><div><label for="1d2a8777" title>发行版</label><select id="1d2a8777" name="release" title><option value="7">CentOS/RHEL 7</option><option value="6">CentOS/RHEL 6</option><option value="8">CentOS/RHEL 8</option><option value="9">CentOS/RHEL 9</option></select></div></form><pre class="z-code"></pre></div><tmpl z-input="release" z-lang="bash">
{{sudo}}yum localinstall --nogpgcheck {{endpoint}}/free/el/rpmfusion-free-release-{{release}}.noarch.rpm {{endpoint}}/nonfree/el/rpmfusion-nonfree-release-{{release}}.noarch.rpm
</tmpl>
<p>注意：没有将当前用户设为管理员的用户，需要将 <code>sudo CMD</code> 替换为 <code>su -c 'CMD'</code>，并输入 root 密码。</p>
<h3>修改链接指向镜像站</h3>
<p>安装成功后，修改 <code>/etc/yum.repos.d/</code> 目录下以 <code>rpmfusion</code> 开头，以 <code>.repo</code> 结尾的文件。具体而言，需要将文件中的 <code>baseurl=</code> 开头的行等号后面链接中的 <code>http://download1.rpmfusion.org/</code> 替换为</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl>
{{endpoint}}/
</tmpl>
<p>替换后的文件类似如下：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="ini">
[rpmfusion-free]
name=RPM Fusion for Fedora $releasever - Free
baseurl={{endpoint}}/free/fedora/releases/$releasever/Everything/$basearch/os/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&amp;arch=$basearch
enabled=1
metadata_expire=7d
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever-$basearch

[rpmfusion-free-debuginfo]
name=RPM Fusion for Fedora $releasever - Free - Debug
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-debug-$releasever&amp;arch=$basearch
enabled=0
metadata_expire=7d
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever-$basearch

[rpmfusion-free-source]
name=RPM Fusion for Fedora $releasever - Free - Source
baseurl={{endpoint}}/free/fedora/releases/$releasever/Everything/source/SRPMS/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-source-$releasever&amp;arch=$basearch
enabled=0
metadata_expire=7d
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever-$basearch
</tmpl>
<h3>更多</h3>
<p>RHEL/CentOS 用户请参考 <a href="http://rpmfusion.org/Configuration">RPMFusion 官方指南</a>。</p><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIlJQTUZ1c2lvbiBcdThmNmZcdTRlZjZcdTRlZDNcdTVlOTMiLCAiYmxvY2siOiBbInJwbWZ1c2lvbiJdLCAiaW5wdXQiOiB7InJlbGVhc2UiOiB7Il8iOiAiXHU1M2QxXHU4ODRjXHU3MjQ4IiwgIm9wdGlvbiI6IHsiNyI6IHsiXyI6ICJDZW50T1MvUkhFTCA3In0sICI2IjogeyJfIjogIkNlbnRPUy9SSEVMIDYifSwgIjgiOiB7Il8iOiAiQ2VudE9TL1JIRUwgOCJ9LCAiOSI6IHsiXyI6ICJDZW50T1MvUkhFTCA5In19fX0sICJuYW1lIjogInJwbWZ1c2lvbiJ9</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
