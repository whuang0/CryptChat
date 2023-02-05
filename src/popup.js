loginBtn.addEventListener('click', function() {
  const username = document.querySelector('#username').value;
  const password = document.querySelector('#password').value;

  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'login.php', true);
  xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      const response = JSON.parse(xhr.responseText);
      if (response.success) {
        window.location.href = 'friendpage.html';
      } else {
        error.style.display = 'block';
        error.innerHTML = 'Login failed. Please check your username and password.';
      }
    }
  }

  xhr.send(`username=${username}&password=${password}`);
});
