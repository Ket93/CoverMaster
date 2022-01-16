document.querySelectorAll('INPUT[Type="BUTTON"]').forEach(button =>
  button.addEventListener('click', event => {
    window.location.href = event.target.dataset.location
  })
)