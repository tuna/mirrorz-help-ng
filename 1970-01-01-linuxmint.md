---
category: help
layout: help
mirrorid: linuxmint
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
<div class="z-help"><h1>Linux Mint 软件仓库</h1>
<p>Linux Mint 也采用 apt 作为包管理器，与 Ubuntu 和 Debian 类似，你需要编辑 <code>/etc/apt/sources.list</code> 和 <code>/etc/apt/sources.list.d/*</code> 中的路径。对于来自 Ubuntu 与 Debian 的部分源，可以参考 <a href="../ubuntu/">Ubuntu 帮助</a>与 <a href="../debian/">Debian 帮助</a>进行修改。</p>
<p>需要修改 <code>/etc/apt/sources.list.d/official-package-repositories.list</code>（注意备份），把 <code>packages.linuxmint.com</code> 替换为镜像源</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"><div><label for="a804dd7c" title>Linux Mint 版本</label><select id="a804dd7c" name="release" title><option value="victoria">21.2 (victoria)</option><option value="vera">21.1 (vera)</option><option value="vanessa">21 (vanessa)</option><option value="una">20.3 (una)</option><option value="uma">20.2 (uma)</option><option value="ulyssa">20.1 (ulyssa)</option></select></div></form><pre class="z-code"></pre></div><tmpl z-input="release">
deb {{endpoint}}/ {{release}} main upstream import backport
</tmpl>
<p>然后运行 <code>apt update</code> 即可。</p>
<p>注：完成后请不要再使用 mintsources（自带的图形化软件源设置工具）进行任何操作，因为在操作后，无论是否有按“确定”，mintsources 均会复写 <code>/etc/apt/sources.list.d/official-package-repositories.list</code>。</p><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkxpbnV4IE1pbnQgXHU4ZjZmXHU0ZWY2XHU0ZWQzXHU1ZTkzIiwgImJsb2NrIjogWyJsaW51eG1pbnQiXSwgImlucHV0IjogeyJyZWxlYXNlIjogeyJfIjogIkxpbnV4IE1pbnQgXHU3MjQ4XHU2NzJjIiwgIm9wdGlvbiI6IHsidmljdG9yaWEiOiB7Il8iOiAiMjEuMiAodmljdG9yaWEpIn0sICJ2ZXJhIjogeyJfIjogIjIxLjEgKHZlcmEpIn0sICJ2YW5lc3NhIjogeyJfIjogIjIxICh2YW5lc3NhKSJ9LCAidW5hIjogeyJfIjogIjIwLjMgKHVuYSkifSwgInVtYSI6IHsiXyI6ICIyMC4yICh1bWEpIn0sICJ1bHlzc2EiOiB7Il8iOiAiMjAuMSAodWx5c3NhKSJ9fX19LCAibmFtZSI6ICJsaW51eG1pbnQifQ==</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
