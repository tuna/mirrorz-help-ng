---
category: help
layout: help
mirrorid: gitlab-runner
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
<div class="z-help"><h1>GitLab Runner 软件仓库</h1>
<h2>收录范围</h2>
<p>gitlab-runner 镜像支持 x86-64 和 ARM64(aarch64) 架构。</p>
<h3>Debian/Ubuntu 用户</h3>
<p>首先信任 GitLab 的 GPG 公钥：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
curl https://packages.gitlab.com/gpg.key 2&gt; /dev/null | {{sudo}}apt-key add - &amp;&gt;/dev/null
</tmpl>
<p>再选择你的 Debian/Ubuntu 版本，将下方内容写入 <code>/etc/apt/sources.list.d/gitlab-runner.list</code></p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"><div><label for="79a46d2a" title>操作系统版本</label><select id="79a46d2a" name="release" title><option value="bullseye">Debian 11 (bullseye)</option><option value="buster">Debian 10 (buster)</option><option value="stretch">Debian 9 (stretch) (EOL)</option><option value="jessie">Debian 8 (jessie) (EOL)</option><option value="focal">Ubuntu 20.04 LTS (focal)</option><option value="bionic">Ubuntu 18.04 LTS (bionic)</option><option value="xenial">Ubuntu 16.04 LTS (xenial) (EOL)</option></select></div></form><pre class="z-code"></pre></div><tmpl z-input="release" z-path="/etc/apt/sources.list.d/gitlab-runner.list">
deb {{endpoint}}/{{os}} {{release}} main
</tmpl>
<p>安装 gitlab-runner:</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}apt-get update
{{sudo}}apt-get install gitlab-runner
</tmpl>
<h3>CentOS/RHEL</h3>
<p>新建 <code>/etc/yum.repos.d/gitlab-runner.repo</code>，内容为</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="ini" z-path="/etc/yum.repos.d/gitlab-runner.repo">
[gitlab-runner]
name=gitlab-runner
baseurl={{endpoint}}/yum/el$releasever-$basearch/
repo_gpgcheck=0
gpgcheck=0
enabled=1
gpgkey=https://packages.gitlab.com/gpg.key
</tmpl>
<p>再执行</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}yum makecache
{{sudo}}yum install gitlab-runner
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkdpdExhYiBSdW5uZXIgXHU4ZjZmXHU0ZWY2XHU0ZWQzXHU1ZTkzIiwgImJsb2NrIjogWyJjb3ZlciIsICJkZWIiLCAicnBtIl0sICJpbnB1dCI6IHsicmVsZWFzZSI6IHsiXyI6ICJcdTY0Y2RcdTRmNWNcdTdjZmJcdTdlZGZcdTcyNDhcdTY3MmMiLCAib3B0aW9uIjogeyJidWxsc2V5ZSI6IHsiXyI6ICJEZWJpYW4gMTEgKGJ1bGxzZXllKSIsICJvcyI6ICJkZWJpYW4ifSwgImJ1c3RlciI6IHsiXyI6ICJEZWJpYW4gMTAgKGJ1c3RlcikiLCAib3MiOiAiZGViaWFuIn0sICJzdHJldGNoIjogeyJfIjogIkRlYmlhbiA5IChzdHJldGNoKSAoRU9MKSIsICJvcyI6ICJkZWJpYW4ifSwgImplc3NpZSI6IHsiXyI6ICJEZWJpYW4gOCAoamVzc2llKSAoRU9MKSIsICJvcyI6ICJkZWJpYW4ifSwgImZvY2FsIjogeyJfIjogIlVidW50dSAyMC4wNCBMVFMgKGZvY2FsKSIsICJvcyI6ICJ1YnVudHUifSwgImJpb25pYyI6IHsiXyI6ICJVYnVudHUgMTguMDQgTFRTIChiaW9uaWMpIiwgIm9zIjogInVidW50dSJ9LCAieGVuaWFsIjogeyJfIjogIlVidW50dSAxNi4wNCBMVFMgKHhlbmlhbCkgKEVPTCkiLCAib3MiOiAidWJ1bnR1In19fX0sICJuYW1lIjogImdpdGxhYi1ydW5uZXIifQ==</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
