function showDateTime() {
    var myDiv = document.getElementById("myDiv");

    var date = new Date();
    var dayList = ["الاحد", "الاثنين", "الثلاثاء", "الاربعاء", "الخميس", "الجمعه", "السبت"];
    var monthNames = [
      "يناير",
      "فبراير",
      "مارس",
      "ابريل",
      "مايو",
      "يونيو",
      "يوليو",
      "اغسطس",
      "سبتمبر",
      "اكتوبر",
      "نوفمبر",
      "ديسمبر"
    ];
    var dayName = dayList[date.getDay()];
    var monthName = monthNames[date.getMonth()];
    var today = `${dayName}, ${date.getDate()}, ${monthName} , ${date.getFullYear()}`;

    var hour = date.getHours();
    var min = date.getMinutes();
    var sec = date.getSeconds();

    var time = hour + ":" + min + ":" + sec;
    myDiv.innerText = ` ${time} . ${today}  `;
  }
  setInterval(showDateTime, 1000);
  