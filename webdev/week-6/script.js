// ===========================
// 1. Custom form validation
// ===========================
document.getElementById("signupForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form submission

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const message = document.getElementById("formMessage");

  if (username === "" || password === "") {
    message.textContent = "⚠️ All fields are required!";
    message.style.color = "red";
  } else if (password.length < 6) {
    message.textContent = "⚠️ Password must be at least 6 characters long!";
    message.style.color = "red";
  } else {
    message.textContent = "✅ Form submitted successfully!";
    message.style.color = "green";
  }
});

// ===========================
// 2. Password visibility toggle (inside the form)
// ===========================
document.getElementById("toggleBtn").addEventListener("click", function() {
  const passwordField = document.getElementById("password");
  if (passwordField.type === "password") {
    passwordField.type = "text"; // show password
  } else {
    passwordField.type = "password"; // hide password
  }
});

// ===========================
// 3. Click counter
// ===========================
let count = 0;
document.getElementById("countBtn").addEventListener("click", function() {
  count++;
  document.getElementById("countDisplay").textContent = count;
});

// ===========================
// 4. Background + form color changer
// ===========================
document.querySelectorAll(".colorBtn").forEach(button => {
  button.addEventListener("click", function() {
    const colorChoice = this.getAttribute("data-color");

    // Change background
    if (colorChoice === "white") {
      document.body.style.backgroundColor = "white";
      document.body.style.color = "black";
      document.querySelectorAll("section").forEach(sec => sec.style.backgroundColor = "white");
    } else if (colorChoice === "black") {
      document.body.style.backgroundColor = "black";
      document.body.style.color = "white";
      document.querySelectorAll("section").forEach(sec => sec.style.backgroundColor = "#333");
    } else if (colorChoice === "cream") {
      document.body.style.backgroundColor = "#fffdd0"; // cream
      document.body.style.color = "black";
      document.querySelectorAll("section").forEach(sec => sec.style.backgroundColor = "#fffdd0");
    }
  });
});
