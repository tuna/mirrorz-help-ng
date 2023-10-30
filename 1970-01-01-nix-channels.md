---
category: help
layout: help
mirrorid: nix-channels
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
<div class="z-help"><h1>Nix Channels</h1>
<h3>Nixpkgs binary cache</h3>
<p>目前并未提供 nix-darwin 的 binary cache，请使用官方源或 SJTUG。</p>
<h4>持久配置</h4>
<p>以优先选择镜像，备选源站为例，选择以下配置之一：</p>
<ul>
<li>
<p>单独安装的 Nix：编辑配置文件添加或修改如下项（多用户安装修改 <code>/etc/nix/nix.conf</code>，单用户安装修改 <code>~/.config/nix/nix.conf</code>）：<br/>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl><br/>
substituters = {{endpoint}}/store https://cache.nixos.org/<br/>
</tmpl></p>
</li>
<li>
<p>NixOS 21.11 及之前的版本在 <code>configuration.nix</code> 中使用如下配置（https://cache.nixos.org 会被自动添加）<br/>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="nix"><br/>
    nix.binaryCaches = [ "{{endpoint}}/store" ];<br/>
</tmpl></p>
</li>
<li>
<p>NixOS 22.05 及之后的版本在 <code>configuration.nix</code> 中使用如下配置（https://cache.nixos.org 会被自动添加）：<br/>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="nix"><br/>
    nix.settings.substituters = [ "{{endpoint}}/store" ];<br/>
</tmpl></p>
</li>
</ul>
<p>如果因为无法访问 https://cache.nixos.org 等原因，希望避免自动添加该默认地址，请在配置中使用<code>lib.mkForce</code>。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="nix">
# load `lib` into namespace at the file head with `{ config, pkgs, lib, ... }:`
nix.settings.substituters = lib.mkForce [ "{{endpoint}}/store" ];
</tmpl>
<h4>临时使用</h4>
<p>在安装 NixOS 时临时使用：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
nixos-install --option substituters "{{endpoint}}/store"
</tmpl>
<p>在 NixOS 切换配置时临时使用：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
nixos-rebuild --option substituters "{{endpoint}}/store"
</tmpl>
<p>临时关闭可以通过清空 substituters 实现：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
nixos-rebuild --options substituters ""
</tmpl>
<h3>Nixpkgs channel</h3>
<p>单独安装的 Nix 替换 <code>nixpkgs-unstable</code> 命令如下：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
nix-channel --add {{endpoint}}/nixpkgs-unstable nixpkgs
nix-channel --update
</tmpl>
<p>替换 NixOS channel 命令如下（以 root 执行）：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"><div><label for="a2c11c40" title>系统版本</label><select id="a2c11c40" name="version" title><option value="22.11">22.11</option><option value="unstable">unstable</option><option value="22.05">22.05</option><option value="21.11">21.11</option></select></div></form><pre class="z-code"></pre></div><tmpl z-input="version" z-lang="bash">
nix-channel --add {{endpoint}}/nixos-{{version}} nixos
nix-channel --update
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIk5peCBDaGFubmVscyIsICJibG9jayI6IFsibml4LWNoYW5uZWxzIl0sICJpbnB1dCI6IHsidmVyc2lvbiI6IHsiXyI6ICJcdTdjZmJcdTdlZGZcdTcyNDhcdTY3MmMiLCAib3B0aW9uIjogeyIyMi4xMSI6IG51bGwsICJ1bnN0YWJsZSI6IG51bGwsICIyMi4wNSI6IG51bGwsICIyMS4xMSI6IG51bGx9fX0sICJuYW1lIjogIm5peC1jaGFubmVscyJ9</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
