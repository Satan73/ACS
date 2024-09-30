// Function to validate password strength
function validatePassword() {
    const password = document.getElementById('password').value;  // Get the password input value
    const passwordStrengthText = document.getElementById('password-strength'); // Element to display strength
    const strength = checkPasswordStrength(password);  // Call the strength checking function

    // Update the strength text based on the strength score
    switch (strength) {
        case 0:
            passwordStrengthText.textContent = "Weak password";
            passwordStrengthText.style.color = "red";
            break;
        case 1:
            passwordStrengthText.textContent = "Moderate password";
            passwordStrengthText.style.color = "orange";
            break;
        case 2:
            passwordStrengthText.textContent = "Strong password";
            passwordStrengthText.style.color = "green";
            break;
        default:
            passwordStrengthText.textContent = "";
            break;
    }
}

// Function to check the strength of a password
function checkPasswordStrength(password) {
    let strengthScore = 0;

    // Check for length
    if (password.length >= 8) {
        strengthScore++;
    }
    // Check for lowercase letters
    if (/[a-z]/.test(password)) {
        strengthScore++;
    }
    // Check for uppercase letters
    if (/[A-Z]/.test(password)) {
        strengthScore++;
    }
    // Check for numbers
    if (/[0-9]/.test(password)) {
        strengthScore++;
    }
    // Check for special characters
    if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
        strengthScore++;
    }

    return strengthScore;  // Return the total strength score
}

// Function to validate form inputs
function validateForm(event) {
    event.preventDefault();  // Prevent the default form submission

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    const captchaInput = document.getElementById('captcha-input').value;

    // Check if passwords match
    if (password !== confirmPassword) {
        alert("Passwords do not match!");  // Alert if passwords don't match
        return false;
    }

    // Validate CAPTCHA input (this is a placeholder, implement server-side validation)
    if (captchaInput.trim() === "") {
        alert("Please complete the CAPTCHA.");  // Alert if CAPTCHA is empty
        return false;
    }

    // If all checks pass, submit the form
    document.getElementById('registration-form').submit();
}

// Attach event listeners
document.getElementById('password').addEventListener('input', validatePassword); // Validate password on input
document.getElementById('registration-form').addEventListener('submit', validateForm); // Validate form on submit
