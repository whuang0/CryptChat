// Send a message to the background script
function sendMessage(message) {
    chrome.runtime.sendMessage({ message: message });
  }
  
  // Handle messages sent from the background script
  chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.conversation) {
      // Update the conversation with the latest messages
      document.getElementById("conversation").innerHTML = request.conversation;
    }
  });
  
  // Send a message when the send button is clicked
  document.getElementById("send-button").addEventListener("click", function() {
    const message = document.getElementById("input-message").value;
    sendMessage(message);
  });
  // Execute a function when the user presses a key on the keyboard
input.addEventListener("keypress", function(event) {
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
        console.log()
      // Trigger the button element with a click
      document.getElementById("myBtn").click();
    }
  });
// background-wrapper.js
try {
    importScripts("popup.js");
  } catch (e) {
    console.error(e);
  }
  
  // background.js
  console.log("start");
  throw new Error("lol");
  console.log("end");

  var input = document.getElementById("myInput");

