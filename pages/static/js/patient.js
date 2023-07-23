let arrow = document.querySelectorAll(".arrow");
for (var i = 0; i < arrow.length; i++) {
    arrow[i].addEventListener("click", (e) => {
        let arrowParent = e.target.parentElement.parentElement;//selecting main parent of arrow
        arrowParent.classList.toggle("showMenu");
    });
}
let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
console.log(sidebarBtn);
sidebarBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
});

//buttons functions (view , remove , edit)
function DeletPatient(o) {
    //delet some row
    var p = o.parentNode.parentNode;
    p.parentNode.removeChild(p);
}

function view_patient(elem) {
    // alert("ssss")
    document.querySelector('.popup').style.display = 'block'
    view_popup = document.querySelector('#popup')
    id = elem.parentElement.parentElement.children[0].children[0].innerHTML
    // alert(id)
    function_url = document.querySelector('#getforview').value

    var res = null
    $.ajax({
        type: 'GET',
        url: function_url,
        data: {
            'query': id,
        },
        success: function (response) {
            res = response['result'][0]
            // alert(JSON.stringify(res))
            inputs = view_popup.querySelectorAll('input')
            inputs[0].value = res['id']
            inputs[1].value = res['fname']
            inputs[2].value = res['lname']
            inputs[3].value = res['mobile']
            inputs[4].value = res['age']
            inputs[5].value = res['gender']
            inputs[6].value = res['address']

            return false
        },
        error: function () {
            alert("Error During Deletion.");
            res = null
        }
    });

}

function edit_patient(elem) {
    document.querySelector('.popup_1').style.display = 'block'
    edit_popup = document.querySelector('.popup_1')
    id = elem.parentElement.parentElement.children[0].children[0].innerHTML
    function_url = document.querySelector('#getforview').value

    inputs = edit_popup.querySelectorAll('input')

    $.ajax({
        type: 'GET',
        url: function_url,
        data: {
            'query': id,
        },
        success: function (response) {
            res = response['result'][0]

            inputs[1].value = res['id']
            inputs[2].value = res['fname']
            inputs[3].value = res['lname']
            inputs[4].value = res['mobile']
            inputs[5].value = res['age']
            inputs[6].value = res['gender']
            inputs[7].value = res['address']

        },
        error: function () {
            alert("Error During Deletion.");
            res = null
        }
    });
}

document.querySelector('#edit-form').onsubmit = function (e) {
    edit_form = document.querySelector('#edit-form')

    //When the update button in the form is clicked, the input data is gathered
    let patient_ID = edit_form.querySelector('input[name="id"]').value;
    let newFName = edit_form.querySelector('input[name="fname"]').value;
    let newLName = edit_form.querySelector('input[name="lname"]').value;
    let newMobile = edit_form.querySelector('input[name="mobile"]').value;
    let newAge = edit_form.querySelector('input[name="age"]').value;
    let newGender = edit_form.querySelector('input[name="gender"]').value;
    let newAddress = edit_form.querySelector('input[name="Address"]').value;


    // Creating a JSON object with student data
    let new_patient = {
        'fname': newFName,
        'lname': newLName,
        'id': patient_ID,
        'age': newAge,
        'gender': newGender,
        'mobile': newMobile,
        'address': newAddress
    }

    let edit_url = document.querySelector('#editpatient').value;

    // Sending an AJAX GET request to the edit_Student view, with the updated student info
    $.ajax({
        type: 'GET',
        url: edit_url,
        data: {
            'patient': JSON.stringify(new_patient),
        },
        success: function () {
            // If the student is edited successfully
            alert('Edited Successfully.');

            window.location.reload()
        },
        error: function () {
            alert('Editing Error.');
        }
    });

}
