const toggleButton = document.getElementById('toggleButton');
const inputs = document.querySelectorAll('#myForm input, #myForm select, #myForm textarea');

toggleButton.addEventListener('click', function() {
    const buttonText = toggleButton.textContent;

    for (let i = 0; i < inputs.length; i++) {
        inputs[i].disabled = !inputs[i].disabled;
    }

    if (buttonText === 'Edit') {
        toggleButton.textContent = 'Save';
    } else {
        toggleButton.textContent = 'Edit';
    }
});