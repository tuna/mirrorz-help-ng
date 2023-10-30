---
category: help
layout: help
mirrorid: erlang-solutions
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
<div class="z-help"><h1>Erlang Solutions 软件仓库</h1>
<h3>Debian/Ubuntu 用户</h3>
<p>选择你的系统版本</p>
<div class="z-wrap"><form class="z-form z-global" onchange="form_update(event)" onsubmit="return false"><div><label for="9ee94a36" title>操作系统版本</label><select id="9ee94a36" name="release" title><option value="bullseye">Debian 11 (bullseye)</option><option value="buster">Debian 10 (buster)</option><option value="stretch">Debian 9 (stretch) (EOL)</option><option value="jessie">Debian 8 (jessie) (EOL)</option><option value="focal">Ubuntu 20.04 LTS (focal)</option><option value="bionic">Ubuntu 18.04 LTS (bionic)</option><option value="xenial">Ubuntu 16.04 LTS (xenial) (EOL)</option></select></div></form></div>
<p>首先信任 erlang-solutions 的 GPG 公钥：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
curl -s https://packages.erlang-solutions.com/{{os}}/erlang_solutions.asc | {{sudo}}apt-key add -
</tmpl>
<p>新建 <code>/etc/apt/sources.list.d/erlang-solutions.list</code></p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-path="/etc/apt/sources.list.d/erlang-solutions.list">
deb {{endpoint}}/{{os}} {{release}} contrib
</tmpl>
<p>安装 <code>erlang</code> 即可</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}apt-get update
{{sudo}}apt-get install -y erlang
</tmpl>
<h3>CentOS 用户</h3>
<p>首先信任 erlang-solutions 的 GPG 公钥：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}rpm --import https://packages.erlang-solutions.com/rpm/erlang_solutions.asc
</tmpl>
<p>新建 <code>/etc/yum.repos.d/erlang-solutions.repo</code>，内容为</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="ini" z-path="/etc/yum.repos.d/erlang-solutions.repo">
[erlang-solutions]
name=CentOS $releasever - Erlang Solutions
baseurl={{endpoint}}/centos/$releasever/
gpgcheck=1
gpgkey=https://packages.erlang-solutions.com/rpm/erlang_solutions.asc
enabled=1
</tmpl>
<p>刷新缓存并安装 <code>erlang</code> 即可。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}yum makecache
{{sudo}}yum install erlang
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkVybGFuZyBTb2x1dGlvbnMgXHU4ZjZmXHU0ZWY2XHU0ZWQzXHU1ZTkzIiwgImJsb2NrIjogWyJkZWIiLCAicnBtIl0sICJpbnB1dCI6IHsicmVsZWFzZSI6IHsiXyI6ICJcdTY0Y2RcdTRmNWNcdTdjZmJcdTdlZGZcdTcyNDhcdTY3MmMiLCAib3B0aW9uIjogeyJidWxsc2V5ZSI6IHsiXyI6ICJEZWJpYW4gMTEgKGJ1bGxzZXllKSIsICJvcyI6ICJkZWJpYW4ifSwgImJ1c3RlciI6IHsiXyI6ICJEZWJpYW4gMTAgKGJ1c3RlcikiLCAib3MiOiAiZGViaWFuIn0sICJzdHJldGNoIjogeyJfIjogIkRlYmlhbiA5IChzdHJldGNoKSAoRU9MKSIsICJvcyI6ICJkZWJpYW4ifSwgImplc3NpZSI6IHsiXyI6ICJEZWJpYW4gOCAoamVzc2llKSAoRU9MKSIsICJvcyI6ICJkZWJpYW4ifSwgImZvY2FsIjogeyJfIjogIlVidW50dSAyMC4wNCBMVFMgKGZvY2FsKSIsICJvcyI6ICJ1YnVudHUifSwgImJpb25pYyI6IHsiXyI6ICJVYnVudHUgMTguMDQgTFRTIChiaW9uaWMpIiwgIm9zIjogInVidW50dSJ9LCAieGVuaWFsIjogeyJfIjogIlVidW50dSAxNi4wNCBMVFMgKHhlbmlhbCkgKEVPTCkiLCAib3MiOiAidWJ1bnR1In19fX0sICJuYW1lIjogImVybGFuZy1zb2x1dGlvbnMifQ==</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
