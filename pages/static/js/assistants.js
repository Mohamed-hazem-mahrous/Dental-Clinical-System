let arrow = document.querySelectorAll(".arrow");
  for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e)=>{
   let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
   arrowParent.classList.toggle("showMenu");
    });
  }
  let sidebar = document.querySelector(".sidebar");
  let sidebarBtn = document.querySelector(".bx-menu");
  console.log(sidebarBtn);
  sidebarBtn.addEventListener("click", ()=>{
    sidebar.classList.toggle("close");
  });








//
function togglePopup(){
    document.getElementById("assistant-popup").classList.toggle("active");
    }

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