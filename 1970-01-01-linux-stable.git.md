---
category: help
layout: help
mirrorid: linux-stable.git
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
<div class="z-help"><h1>Linux Stable Git</h1>
<p>如需克隆 Linux Stable 代码，使用</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
git clone {{endpoint}}
</tmpl>
<p>若要将 mirror 加入已有代码库，可在已有仓库中运行</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
git remote add mirror {{endpoint}}
</tmpl>
<p>或运行</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
git remote set-url origin {{endpoint}}
</tmpl>
<p>将默认上游设置为镜像站</p><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkxpbnV4IFN0YWJsZSBHaXQiLCAiYmxvY2siOiBbImxpbnV4LXN0YWJsZS5naXQiXSwgImlucHV0Ijoge30sICJuYW1lIjogImxpbnV4LXN0YWJsZS5naXQifQ==</script>
</div>

{% endraw %}

<script src="/static/js/mustache.min.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
