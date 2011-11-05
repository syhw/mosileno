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

    <center>
        <table border=0 cellpadding=0 cellspacing=0 width="85%" bgcolor=#f6f6ef>

            <tr>
                <td bgcolor=#ff6600>
                    <table border=0 cellpadding=0 cellspacing=0 width="100%" style="padding:2px">
                        <tr>
                            <td style="width:18px;padding-right:4px"><a href="http://ycombinator.com"><img src="http://ycombinator.com/images/y18.gif" width=18 height=18 style="border:1px #ffffff solid;"></img></a></td>
                            <td style="line-height:12pt; height:10px;"><span class="pagetop"><b><a href="news">Hacker Noise</a></b><img src="http://ycombinator.com/images/s.gif" height=1 width=10><a href="newest">new</a> | <a href="threads?id=snippyhollow">threads</a> | <a href="newcomments">comments</a> | <a href="ask">ask</a> | <a href="jobs">jobs</a> | <a href="submit">submit</a></span></td>
                            % if username:
                            <td style="text-align:right;padding-right:4px;"><span class="pagetop"><a href="user?id=${username}">${username}</a>&nbsp;(xxx)&nbsp;|&nbsp;<a href="${request.route_url('logout')}">logout</a></span></td>
                            % else:
                            <td style="text-align:right;padding-right:4px;"><span class="pagetop"><a href="${request.route_url('login')}">login</a></span></td>
                            % endif
                        </tr>
                    </table>
                </td>
            </tr>

            <tr style="height:10px"></tr>

            <tr>
                <td>
                    ${self.body()}
                </td>
            </tr>

            <tr>
                <td>
                    <img src="http://ycombinator.com/images/s.gif" height=10 width=0>
                    <table width="100%" cellspacing=0 cellpadding=1>
                        <tr>
                            <td bgcolor=#ff6600></td>
                        </tr>
                    </table>
                    <br>
                    <center>
                        <span class="yclinks"><a href="lists">Lists</a> | <a href="rss">RSS</a> | <a href="http://ycombinator.com/bookmarklet.html">Bookmarklet</a> | <a href="http://ycombinator.com/newsguidelines.html">Guidelines</a> | <a href="http://ycombinator.com/newsfaq.html">FAQ</a> | <a href="http://ycombinator.com/newsnews.html">News News</a> | <a href="item?id=363">Feature Requests</a> | <a href="http://ycombinator.com">Y Combinator</a> | <a href="http://ycombinator.com/apply.html">Apply</a> | <a href="http://ycombinator.com/lib.html">Library</a></span>
                        <br>
                        <br>
                        <form method=get action="http://www.hnsearch.com/search#request/all">Search: <input type=text name="q" value="" size=17></form>
                        <br>
                    </center>
                </td>
            </tr>
        </table>
    </center>
</body>
</html>
