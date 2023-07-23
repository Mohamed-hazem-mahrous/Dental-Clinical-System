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

















  google.load("visualization", "1", {packages:["corechart"]});
  google.setOnLoadCallback(drawChart1);

  function drawChart1() {
    var data = google.visualization.arrayToDataTable([
      ['Month', 'Done', 'Undone'],
      ['Jun',  24,      17],
      ['Feb',  28,      15],
      ['Mar',  27,       10],
      ['Apr',  23,      20],
      ['May',  30,       11],
      ['Jun',  33,       9],
      ['Jul',  0,       0],
      ['Aug',  0,       0],
      ['Sep',  0,       0],
      ['Oct',  0,       0],
      ['Nov',  0,       0],
      ['Dec',  0,       0]
    ]);

    var year = 2023
    var options = {
      title: 'Statistical Treatment Performance for the clinical at Year ' + year,
      hAxis: {title: 'Month', titleTextStyle: {color: 'red'}}
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div1'));
    chart.draw(data, options);
  }

 
  $(window).resize(function(){
    drawChart1();
  });