---
category: help
layout: help
mirrorid: archlinuxcn
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
<div class="z-help"><h1>Arch Linux CN 软件仓库</h1>
<h2>项目简介</h2>
<p>Arch Linux 中文社区仓库 是由 Arch Linux 中文社区驱动的非官方用户仓库。包含中文用户常用软件、工具、字体/美化包等。</p>
<h2>使用方法</h2>
<p>完整的包信息列表（包名称/架构/维护者/状态）请<a href="https://github.com/archlinuxcn/repo">点击这里</a>查看。</p>
<ul>
<li>官方仓库地址：https://repo.archlinuxcn.org</li>
</ul>
<p>使用方法：在 <code>/etc/pacman.conf</code> 文件末尾添加以下两行：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-append="" z-lang="ini" z-path="/etc/pacman.conf">
[archlinuxcn]
Server = {{endpoint}}/$arch
</tmpl>
<p>之后通过以下命令安装 <code>archlinuxcn-keyring</code> 包导入 GPG key。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}pacman -Sy archlinuxcn-keyring
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkFyY2ggTGludXggQ04gXHU4ZjZmXHU0ZWY2XHU0ZWQzXHU1ZTkzIiwgImJsb2NrIjogWyJpbnRybyIsICJ1c2FnZSJdLCAiaW5wdXQiOiB7fSwgIm5hbWUiOiAiYXJjaGxpbnV4Y24ifQ==</script>
</div>

{% endraw %}

<script src="/static/js/mustache.min.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
