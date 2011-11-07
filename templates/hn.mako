<%inherit file="base.mako"/>

<table border=0 cellpadding=0 cellspacing=0>
    % for num, item in enumerate(items, start=1):
    <tr>
        <td align=right valign=top class="title">${num}.</td>
        <td><center><a id="up_${item['id']} onclick="return vote(this)" href="vote?for=${item['id']}&dir=up&by=${username}&auth=42&whence=%6e%65%77%73">
<!-- <img src="http://ycombinator.com/images/grayarrow.gif" border=0 vspace=3 hspace=2> -->
</a><span id="down_${item['id']}"></span></center></td> 
        <td class="title"><a href="frame?url=${item['url'] | u}" target="_blank">
% if item['titlebig'] == 1:
<big><b>${item['title']}</b></big>
% elif item['titlebig'] == -1:
<small>${item['title']}</small>
% else:
${item['title']}
% endif
</a><span class="comhead"> (${item['domain']}) </span></td>
    </tr>
    <tr>
        <td colspan=2></td>
        <td class="subtext"><span id="score_${item['id']}">${item['points']}</span> by <a href="http://news.ycombinator.com/user?id=dnene">${item['postedBy']}</a> ${item['postedAgo']} | <a href="http://news.ycombinator.com/item?id=${item['id']}">${item['commentCount']} comments</a></td>
    </tr>
    <tr style="height:5px"></tr>

    % endfor

    <tr style="height:10px"></tr>
    <tr>
        <td colspan=2></td>
        <td class="title"><a href="/x?fnid=AF2YkJqkKm" rel="nofollow">More</a></td>
    </tr>
</table>
