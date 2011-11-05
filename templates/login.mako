<%inherit file="base.mako"/>

<%def name="title()">
Login
</%def>

<h1>Login</h1>

% if message:
<p>${message}</p>
% endif

<form action="${url}" method="post">
    <input type="hidden" name="came_from" value="${came_from}"/>
    <input type="text" name="login" value="${login}"/><br/>
    <input type="password" name="password" value="${password}"/><br/>
    <input type="submit" name="form.submitted" value="Log In"/>
</form>
