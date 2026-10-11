document.getElementById('contactForm').addEventListener('submit', async function (event) {
  event.preventDefault();

  const email = document.getElementById('email').value.trim();
  const code = document.getElementById('code').value.trim();
  const status = document.getElementById('statusMessage');

  if (!email || !code) {
    status.textContent = 'Please enter both your email and code.';
    return;
  }

  status.textContent = 'Submitting securely...';

  try {
    const response = await fetch('/api/contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, code })
    });

    const data = await response.json();

    if (data.status === 'success') {
      status.textContent = 'Your code was submitted successfully.';
    } else {
      status.textContent = data.message || 'Your message was received.';
    }
  } catch (error) {
    status.textContent = 'Unable to submit right now. Please try again later.';
  }
});
