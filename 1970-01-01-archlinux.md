---
category: help
layout: help
mirrorid: archlinux
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
<div class="z-help"><h1>Arch Linux 软件仓库</h1>
<h2>项目简介</h2>
<p>Arch Linux 是通用 x86-64 GNU/Linux 发行版。Arch 采用滚动升级模式，尽全力提供最新的稳定版软件。初始安装的 Arch 只是一个基本系统，随后用户可以根据自己的喜好安装需要的软件并配置成符合自己理想的系统。</p>
<h2>使用方法</h2>
<p>Pacman 以 <code>mirrorlist</code> 中 Server 的顺序作为优先级，因此添加镜像需要在文件的最顶端添加；您可以同时注释掉其它所有镜像。</p>
<p>有关 Arch Linux 使用镜像的详细说明请见<a href="https://wiki.archlinux.org/title/mirrors">官方文档</a></p>
<p>编辑 <code>/etc/pacman.d/mirrorlist</code>，在文件的最顶端添加：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="ini" z-path="/etc/pacman.d/mirrorlist">
Server = {{endpoint}}/$repo/os/$arch
</tmpl>
<p>更新软件包缓存：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}pacman -Syyu
</tmpl>
<p>两次 <code>y</code> 能避免从<strong>损坏的</strong>镜像切换到<strong>正常的</strong>镜像时出现的问题。</p>
<p>如果您从一个较新的镜像切换到较旧的镜像，以下命令可以降级部分包，以避免系统的部分更新。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}pacman -Syyuu
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkFyY2ggTGludXggXHU4ZjZmXHU0ZWY2XHU0ZWQzXHU1ZTkzIiwgImJsb2NrIjogWyJpbnRybyIsICJ1c2FnZSJdLCAiaW5wdXQiOiB7fSwgIm5hbWUiOiAiYXJjaGxpbnV4In0=</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
