# -*- coding: utf-8 -*-
<!DOCTYPE html>

<head>
<script src="static/jquery-1.7.min.js"></script>
<script>
var count_loads = 0;
var timer_id = null; 
function timer_start() 
{ 
console.log('start');/////////////////
    $.get('timer_start/test_user?url=${url | u}', function(data)
            { 
console.log('startCB');/////////////////
            timer_id = data;
            return false;
            }
         );
console.log('end'); /////////////////
};
timer_start();
function timer_stop() 
{ 
    if (count_loads > 0)
        $.get('timer_stop/' + '${id}');
    else
        count_loads++;
};
$(document).bind(onbeforeunload, timer_stop);
</script>
<meta charset="utf-8">
        <style type="text/css"> 
            html {overflow: auto;} 
            html, body, div, iframe {margin: 0px; padding: 0px; height: 100%; border: none;} 
            iframe {display: block; width: 100%; border: none; overflow-y: auto; overflow-x: hidden;} 
        </style> 
</head>
<body>
        <iframe id="frame" name="frame" src="${url}" frameborder="0" marginheight="0" marginwidth="0" width="100%" height="100%" scrolling="auto" onLoad="timer_stop();">Your browser doesn't support iFrames... <a href="${url}">Here it is</a></iframe> 
</body>
</html>
