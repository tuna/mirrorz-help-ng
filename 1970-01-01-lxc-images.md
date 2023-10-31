---
category: help
layout: help
mirrorid: lxc-images
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
<div class="z-help"><h1>LXC Images 软件仓库</h1>
<p>LXC 1.0 以上版本增加了 <code>download</code> 模版，支持下载定义好的系统镜像。</p>
<p>欲使用镜像站进行下载加速，可以在 <code>lxc-create -t download</code> 的选项部分，<br/>
增加 <code>--server</code> 即可，例如：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
lxc-create -t download -n my-container -- --server {{host}}{{path}}
</tmpl>
<p><strong>LXD/LXC 2.0 及以上版本使用镜像加速的方法</strong>:</p>
<p>创建一个 remote 链接，指向镜像站即可，或替换掉默认的 images 链接。</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
lxc remote add mirror-images {{endpoint}}/ --protocol=simplestreams --public
lxc image list mirror-images:
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkxYQyBJbWFnZXMgXHU4ZjZmXHU0ZWY2XHU0ZWQzXHU1ZTkzIiwgImJsb2NrIjogWyJseGMtaW1hZ2VzIl0sICJpbnB1dCI6IHt9LCAibmFtZSI6ICJseGMtaW1hZ2VzIn0=</script>
</div>

{% endraw %}

<script src="/static/js/mustache.min.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
