
const days = document.getElementById('days');
const hours = document.getElementById('hours');
const mins = document.getElementById('mins');
const secs = document.getElementById('secs');
const year = document.getElementById('year');


const currentYear = new Date().getFullYear();
const untilWhen = new Date(`January 01 ${currentYear + 1} 00:00:00`);

function countDown(){

    const today = new Date()
    const diff = untilWhen - today;

    const d = Math.floor(diff / 1000 / 60 / 60 / 24);
    const h = Math.floor(diff / 1000 / 60 / 60)%24;
    const m = Math.floor(diff / 1000 / 60)%60;
    const s = Math.floor(diff / 1000)%60;

    // console.log(d+"day"+h+"hour"+m+"min"+s+"sec")
    days.innerHTML=d;
    hours.innerHTML=h < 10 ? '0' + h : h;
    mins.innerHTML=m < 10 ? '0' + m : m;
    secs.innerHTML=s < 10 ? '0' + s : s;
    year.innerHTML=currentYear+1;


}
// countDown()



setInterval(countDown, 1000);