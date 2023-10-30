---
category: help
layout: help
mirrorid: voidlinux
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
<div class="z-help"><h1>Void Linux 软件仓库</h1>
<p>使用如下命令替换为本镜像：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
mkdir -p /etc/xbps.d
cp /usr/share/xbps.d/*-repository-*.conf /etc/xbps.d/
sed -i 's|https://repo-default.voidlinux.org|{{endpoint}}|g' /etc/xbps.d/*-repository-*.conf
</tmpl>
<p>若报错可尝试</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
sed -i 's|https://alpha.de.repo.voidlinux.org|{{endpoint}}|g' /etc/xbps.d/*-repository-*.conf
</tmpl>
<p>之后可用 <code>xbps-query -L</code> 检查是否正确替换。</p>
<p>参考<a href="https://docs.voidlinux.org/xbps/repositories/mirrors/changing.html">官方教程</a>。</p><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIlZvaWQgTGludXggXHU4ZjZmXHU0ZWY2XHU0ZWQzXHU1ZTkzIiwgImJsb2NrIjogWyJ2b2lkbGludXgiXSwgImlucHV0Ijoge30sICJuYW1lIjogInZvaWRsaW51eCJ9</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
