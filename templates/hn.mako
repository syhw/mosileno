# -*- coding: utf-8 -*-
<!DOCTYPE html>

<head>
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="http://ycombinator.com/news.css">
<link rel="shortcut icon" href="http://ycombinator.com/favicon.ico">

<script>
function byId(id) {
  return document.getElementById(id);
}

function vote(node) {
  var v = node.id.split(/_/);   // {'up', '123'}
  var item = v[1]; 

  // hide arrows
  byId('up_'   + item).style.visibility = 'hidden';
  byId('down_' + item).style.visibility = 'hidden';

  // ping server
  var ping = new Image();
  ping.src = node.href;

  return false; // cancel browser nav
} 
</script>

<title>Hacker Noise</title>
</head>

<body>

<center><table border=0 cellpadding=0 cellspacing=0 width="85%" bgcolor=#f6f6ef><tr><td bgcolor=#ff6600><table border=0 cellpadding=0 cellspacing=0 width="100%" style="padding:2px"><tr><td style="width:18px;padding-right:4px"><a href="http://ycombinator.com"><img src="http://ycombinator.com/images/y18.gif" width=18 height=18 style="border:1px #ffffff solid;"></img></a></td><td style="line-height:12pt; height:10px;"><span class="pagetop"><b><a href="news">Hacker Noise</a></b><img src="http://ycombinator.com/images/s.gif" height=1 width=10><a href="newest">new</a> | <a href="threads?id=snippyhollow">threads</a> | <a href="newcomments">comments</a> | <a href="ask">ask</a> | <a href="jobs">jobs</a> | <a href="submit">submit</a></span></td><td style="text-align:right;padding-right:4px;"><span class="pagetop"><a href="user?id=snippyhollow">snippyhollow</a>&nbsp;(450)&nbsp;|&nbsp;<a href="/r?fnid=4884svt0Wx">logout</a></span></td></tr></table></td></tr><tr style="height:10px"></tr><tr><td><table border=0 cellpadding=0 cellspacing=0><tr><td align=right valign=top class="title">1.</td><td><center><a id=up_3197798 onclick="return vote(this)" href="vote?for=3197798&dir=up&by=snippyhollow&auth=c748af3cf2a1e5737684a5062e6597b3cf7cf529&whence=%6e%65%77%73"><img src="http://ycombinator.com/images/grayarrow.gif" border=0 vspace=3 hspace=2></a><span id=down_3197798></span></center></td>

% for item in items:
<td class="title"><a href="frame?url=${item['url'] | u}" target="_blank">${item['title']}</a><span class="comhead"> (${item['domain']}) </span></td>
</tr><tr><td colspan=2></td>
<td class="subtext"><span id=score_3197798>${item['points']}</span> by <a href="user?id=dnene">${item['author']}</a> ${item['age']} ago  | <a href="/r?fnid=PWSgr5bvS9">flag</a> | <a href="item?id=3197798">${item['num_comments']} comments</a></td></tr>
% endfor


<tr style="height:10px"></tr>

<tr><td colspan=2></td><td class="title"><a href="/x?fnid=AF2YkJqkKm" rel="nofollow">More</a></td>
</tr></table></td>
</tr><tr><td><img src="http://ycombinator.com/images/s.gif" height=10 width=0><table width="100%" cellspacing=0 cellpadding=1><tr><td bgcolor=#ff6600></td>
</tr></table><br>
<center><span class="yclinks"><a href="lists">Lists</a> | <a href="rss">RSS</a> | <a href="http://ycombinator.com/bookmarklet.html">Bookmarklet</a> | <a href="http://ycombinator.com/newsguidelines.html">Guidelines</a> | <a href="http://ycombinator.com/newsfaq.html">FAQ</a> | <a href="http://ycombinator.com/newsnews.html">News News</a> | <a href="item?id=363">Feature Requests</a> | <a href="http://ycombinator.com">Y Combinator</a> | <a href="http://ycombinator.com/apply.html">Apply</a> | <a href="http://ycombinator.com/lib.html">Library</a></span><br><br>
<form method=get action="http://www.hnsearch.com/search#request/all">Search: <input type=text name="q" value="" size=17></form><br>
</center></td></tr></table></center>
</body>
</html>
