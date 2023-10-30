---
category: help
layout: help
mirrorid: raspberrypi
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
<div class="z-help"><h1>Raspberrypi 软件仓库</h1>
<p>主要参考 <a href="../raspbian/">Raspbian 帮助</a></p>
<p>编辑 <code>/etc/apt/sources.list.d/raspi.list</code> 文件。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"><div><label for="83a072ff" title>选择你的 Raspbian 对应的 Debian 版本</label><select id="83a072ff" name="release" title><option value="bookworm">Debian 12 (bookworm)</option><option value="bullseye">Debian 11 (bullseye)</option><option value="buster">Debian 10 (buster)</option><option value="stretch">Debian 9 (stretch) (EOL)</option></select></div></form><pre class="z-code"></pre></div><tmpl z-input="release" z-path="/etc/apt/sources.list.d/raspi.list">
deb {{endpoint}}/ {{release}} main
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIlJhc3BiZXJyeXBpIFx1OGY2Zlx1NGVmNlx1NGVkM1x1NWU5MyIsICJibG9jayI6IFsicmFzcGJlcnJ5cGkiXSwgImlucHV0IjogeyJyZWxlYXNlIjogeyJfIjogIlx1OTAwOVx1NjJlOVx1NGY2MFx1NzY4NCBSYXNwYmlhbiBcdTViZjlcdTVlOTRcdTc2ODQgRGViaWFuIFx1NzI0OFx1NjcyYyIsICJvcHRpb24iOiB7ImJvb2t3b3JtIjogeyJfIjogIkRlYmlhbiAxMiAoYm9va3dvcm0pIn0sICJidWxsc2V5ZSI6IHsiXyI6ICJEZWJpYW4gMTEgKGJ1bGxzZXllKSJ9LCAiYnVzdGVyIjogeyJfIjogIkRlYmlhbiAxMCAoYnVzdGVyKSJ9LCAic3RyZXRjaCI6IHsiXyI6ICJEZWJpYW4gOSAoc3RyZXRjaCkgKEVPTCkifX19fSwgIm5hbWUiOiAicmFzcGJlcnJ5cGkifQ==</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
