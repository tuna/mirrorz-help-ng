---
category: help
layout: help
mirrorid: archlinuxarm
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
<div class="z-help"><h1>Arch Linux ARM 软件仓库</h1>
<h2>软件源使用方法</h2>
<p>编辑 <code>/etc/pacman.d/mirrorlist</code>，在文件的最顶端添加以下配置；您可以同时注释掉其它所有镜像。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="ini" z-path="/etc/pacman.d/mirrorlist">
Server = {{endpoint}}/$arch/$repo
</tmpl>
<p>更新软件包缓存：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}pacman -Syy
</tmpl>
<h2>系统镜像下载</h2>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl>
{{endpoint}}
</tmpl>
<p>请访问 <a href="https://archlinuxarm.org/platforms">https://archlinuxarm.org/platforms</a>，阅读硬件平台对应的安装指引并下载对应的系统镜像。</p><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkFyY2ggTGludXggQVJNIFx1OGY2Zlx1NGVmNlx1NGVkM1x1NWU5MyIsICJibG9jayI6IFsidXNhZ2UiLCAiaW1hZ2UiXSwgImlucHV0Ijoge30sICJuYW1lIjogImFyY2hsaW51eGFybSJ9</script>
</div>

{% endraw %}

<script src="/static/js/mustache.min.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
