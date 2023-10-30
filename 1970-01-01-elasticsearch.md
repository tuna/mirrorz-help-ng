---
category: help
layout: help
mirrorid: elasticstack
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
<div class="z-help"><h1>Elastic Stack 软件仓库</h1>
<h2>项目简介</h2>
<p><a href="https://www.elastic.co/cn/what-is/elasticsearch">Elasticsearch</a> 是位于 Elastic Stack 核心的分布式搜索和分析引擎。</p>
<h2>使用方法</h2>
<p>请参考 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html">elasticsearch 官方安装教程</a>。</p>
<p>以 Debian/Ubuntu 安装为例，举例如下：</p>
<div class="z-wrap"><form class="z-form" onchange="form_update(event)" onsubmit="return false"><div><label for="f925762a" title>版本</label><select id="f925762a" name="version" title><option value="8.x">8.x</option><option value="7.x">7.x</option><option value="6.x">6.x</option></select></div></form><pre class="z-code"></pre></div><tmpl z-input="version" z-lang="bash">
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | {{sudo}}gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] {{endpoint}}/{{version}}/apt/ stable main" | {{sudo}}tee /etc/apt/sources.list.d/elastic-{{version}}.list
{{sudo}}apt-get update &amp;&amp; {{sudo}}apt-get install elasticsearch
</tmpl><script id="z-config" type="application/x-mirrorz-help">eyJfIjogIkVsYXN0aWMgU3RhY2sgXHU4ZjZmXHU0ZWY2XHU0ZWQzXHU1ZTkzIiwgImJsb2NrIjogWyJpbnRybyIsICJ1c2FnZSJdLCAiaW5wdXQiOiB7InZlcnNpb24iOiB7Il8iOiAiXHU3MjQ4XHU2NzJjIiwgIm9wdGlvbiI6IHsiOC54IjogbnVsbCwgIjcueCI6IG51bGwsICI2LngiOiBudWxsfX19LCAicGVybWFsaW5rIjogImVsYXN0aWNzZWFyY2giLCAibmFtZSI6ICJlbGFzdGljc3RhY2sifQ==</script>
</div>

{% endraw %}

<script src="/static/js/mustache.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
