<%inherit file="base.mako"/>

<table border=0 cellpadding=0 cellspacing=0>
    % for num, item in enumerate(items, start=1):
    <tr>
        <td align=right valign=top class="title">${num}.</td>
        <td><center><a id=up_3197798 onclick="return vote(this)" href="vote?for=3197798&dir=up&by=snippyhollow&auth=c748af3cf2a1e5737684a5062e6597b3cf7cf529&whence=%6e%65%77%73"><img src="http://ycombinator.com/images/grayarrow.gif" border=0 vspace=3 hspace=2></a><span id=down_3197798></span></center></td>
        <td class="title"><a href="frame?url=${item['url'] | u}" target="_blank">${item['title']}</a><span class="comhead"> (${item['domain']}) </span></td>
    </tr>
    <tr>
        <td colspan=2></td>
        <td class="subtext"><span id=score_3197798>${item['points']}</span> by <a href="user?id=dnene">${item['author']}</a> ${item['age']} ago  | <a href="/r?fnid=PWSgr5bvS9">flag</a> | <a href="item?id=3197798">${item['num_comments']} comments</a></td>
    </tr>
    <tr style="height:5px"></tr>

    % endfor

    <tr style="height:10px"></tr>
    <tr>
        <td colspan=2></td>
        <td class="title"><a href="/x?fnid=AF2YkJqkKm" rel="nofollow">More</a></td>
    </tr>
</table>
