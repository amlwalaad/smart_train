function showDateTime() {
    var myDiv = document.getElementById("myDiv");
  
    var date = new Date();
    var dayList = ["الاحد", "الاثنين", "الثلاثاء", "الاربعاء", "الخميس", "الجمعة", "السبت"];
    var monthNames = [
      "يناير",
      "فبراير",
      "مارس",
      "ابريل",
      "مايو",
      "يونيو",
      "يولو",
      "اغسطس",
      "سيتمبر",
      "اكتوبر",
      "نوفمبر",
      "دبسمبر"
    ];
    var dayName = dayList[date.getDay()];
    var monthName = monthNames[date.getMonth()];
    var today = `${dayName}, ${monthName} ${date.getDate()}, ${date.getFullYear()}`;
  
    var hour = date.getHours();
    var min = date.getMinutes();
    var sec = date.getSeconds();
  
    var time = hour + ":" + min + ":" + sec;
    myDiv.innerText = `  ${today} ${time}`;
  }
  setInterval(showDateTime, 1000);
  