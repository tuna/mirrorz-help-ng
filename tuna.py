import os
from pathlib import Path
import bs4


outdir = Path(os.environ.get('TUNA_TEMP_DIR', './tuna/'))
os.makedirs(outdir, exist_ok=True)


def process(html, config, project, *_):
    doc = bs4.BeautifulSoup(html, 'html.parser')
    for tmpl in doc.find_all('tmpl'):
        tmpl.name = "pre"
        tmpl.attrs["class"] = tmpl.attrs.get("class", []) + ["z-tmpl"]
    html = str(doc)
    md = f"""---
category: help
layout: help
mirrorid: {config.get('mirrorid', project)}
excerpt_separator: ""
---
""" + """
<!-- 本页面从 tuna/mirrorz-help-ng 自动生成，如需修改请参阅该仓库 -->
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
            <input id="a44d763c" name="_scheme" type="checkbox" checked>
            <label for="a44d763c">是否使用 HTTPS</label>
        </div>
        <div>
            <input id="a659e7da" name="_sudo" type="checkbox">
            <label for="a659e7da">是否使用 sudo</label>
        </div>
    </form>
</div>
{% raw %}
""" + html + """
{% endraw %}

<script src="/static/js/mustache.min.js?{{ site.data['hash'] }}"></script>
<script src="/static/js/zdocs.js?{{ site.data['hash'] }}"></script>
"""
    with open(outdir/f'1970-01-01-{config.get("permalink", project)}.html', 'w') as f:
        f.write(md)
    return html
