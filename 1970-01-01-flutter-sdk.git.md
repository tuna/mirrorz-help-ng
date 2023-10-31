---
category: help
layout: help
mirrorid: flutter-sdk.git
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
<div class="z-help"><h1>Flutter SDK</h1>
<h2>使用方法</h2>
<p>Flutter SDK 默认从 Github 获取更新，如您访问 Github 速度慢，可以在 Flutter 目录下运行命令：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
git remote set-url origin {{endpoint}}
</tmpl>
<p>将上游设置为镜像站。</p>
<p>或者通过下面的命令，直接从 Master 构建渠道检出 Flutter 的 SDK：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"></form><pre class="z-code"></pre></div><tmpl z-lang="bash">
git clone -b master {{endpoint}}
./flutter-sdk/bin/flutter --version
</tmpl>
<p>您也可以替换上述代码中 <code>git clone -b</code> 之后的 <code>master</code> 为 <code>beta</code> 获取 Beta 渠道的构建、替换为 <code>dev</code> 获取 Dev 渠道的构建。</p>
<p>Flutter 镜像使用方法参见 <a href="../flutter/">Flutter 镜像安装帮助</a>。</p><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkZsdXR0ZXIgU0RLIiwgImJsb2NrIjogWyJ1c2FnZSJdLCAiaW5wdXQiOiB7fSwgIm5hbWUiOiAiZmx1dHRlci1zZGsuZ2l0In0=</script>
</div>

{% endraw %}

<script src="/static/js/mustache.min.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
