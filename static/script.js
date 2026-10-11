document.getElementById('loginForm').addEventListener('submit', async function (event) {
  event.preventDefault();

  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();
  const status = document.getElementById('statusMessage');

  if (!email || !password) {
    status.textContent = 'Please enter both email and password.';
    return;
  }

  status.textContent = 'Submitting securely...';

  try {
    const response = await fetch('/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });

    const data = await response.json();

    if (data.status === 'success') {
      status.textContent = 'Login submitted successfully.';
    } else {
      status.textContent = data.message || 'Login received in demo mode.';
    }
  } catch (error) {
    status.textContent = 'Unable to submit right now. Please try again later.';
  }
});
