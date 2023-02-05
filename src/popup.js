const form = document.forms.registrationForm;

form.addEventListener("submit", event => {
  event.preventDefault();

  const email = form.elements.emailInput.value;
  const username = form.elements.usernameInput.value;
  const password = form.elements.passwordInput.value;

  const data = { email, username, password };

  document.getElementById("loginButton").addEventListener("click", function(){
    var username = document.getElementById("usernameInput").value;
    var password = document.getElementById("passwordInput").value;
    var errorMessage = document.getElementById("errorMessage");
  
    // Make API request to get user_details
    document.getElementById("loginButton").addEventListener("click", function() {
      let username = document.getElementById("usernameInput").value;
      let password = document.getElementById("passwordInput").value;
      let errorMessage = document.getElementById("errorMessage");
    
      fetch("http://localhost/demo/users.json")
        .then(response => response.json())
        .then(data => {
          let userExists = false;
          data.user_details.forEach(user => {
            if (user.username === username && user.password === password) {
              userExists = true;
            }
          });
    
          if (userExists) {
            window.location.href = "friendpage.html";
          } else {
            errorMessage.style.display = "block";
          }
        })
        .catch(error => console.error(error));


        const form = document.forms[0];
        const chatDisplay = document.getElementById("chat-display");
        const usernameInput = document.getElementById("username-input");
        const inputMessage = document.getElementById("input-message");
        
        form.addEventListener("submit", event => {
          event.preventDefault();
        
          const username = usernameInput.value;
          const message = inputMessage.value;
        
          const messageDisplay = document.createElement("div");
          messageDisplay.innerHTML = `${username}: ${message}`;
          chatDisplay.appendChild(messageDisplay);
        
          chatDisplay.scrollTop = chatDisplay.scrollHeight;
        
          inputMessage.value = "";
        });
        
  });}); });