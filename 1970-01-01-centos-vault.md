---
category: help
layout: help
mirrorid: centos-vault
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
<div class="z-help"><h1>CentOS Vault 软件仓库</h1>
<h2>收录范围</h2>
<p>该文件夹提供较早版本的 CentOS，例如 CentOS 6；同时提供当前 CentOS 大版本的历史小版本的归档；</p>
<p>还提供 CentOS 各个版本的源代码和调试符号。</p>
<h2>使用方法</h2>
<p>需要确定您所需要的小版本，如无特殊需要则使用该大版本的最后一个小版本，比如 6.10，5.11，填入下方的文本框。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"><div><label for="ca6e5b51" title>使用的小版本</label><input id="ca6e5b51" name="minorver" title type="text" value="6.10"/></div></form><pre class="z-code"></pre></div><tmpl z-input="minorver" z-lang="bash">
{{sudo}}sed -e "s|^mirrorlist=|#mirrorlist=|g" \
    -e "s|^#baseurl=http://mirror.centos.org/centos/\$releasever|baseurl={{endpoint}}/{{minorver}}|g" \
    -e "s|^#baseurl=http://mirror.centos.org/\$contentdir/\$releasever|baseurl={{endpoint}}/{{minorver}}|g" \
    -i.bak \
    /etc/yum.repos.d/CentOS-*.repo
</tmpl>
<p>注意其中的<code>*</code>通配符，如果只需要替换一些文件中的源，请自行增删。</p>
<p>注意，如果需要启用其中一些 repo，需要将其中的 <code>enabled=0</code> 改为 <code>enabled=1</code>。</p>
<p>最后，更新软件包缓存</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
{{sudo}}yum makecache
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkNlbnRPUyBWYXVsdCBcdThmNmZcdTRlZjZcdTRlZDNcdTVlOTMiLCAiYmxvY2siOiBbImNvdmVyIiwgInVzYWdlIl0sICJpbnB1dCI6IHsibWlub3J2ZXIiOiB7Il8iOiAiXHU0ZjdmXHU3NTI4XHU3Njg0XHU1YzBmXHU3MjQ4XHU2NzJjIiwgImRlZmF1bHQiOiAiNi4xMCJ9fSwgIm5hbWUiOiAiY2VudG9zLXZhdWx0In0=</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
