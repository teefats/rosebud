const days = document.querySelector("#days")
const minutes = document.querySelector("#minutes")
const hours = document.querySelector("#hours")
const seconds = document.querySelector("#seconds")
const year = document.querySelector("#year")
const loading = document.getElementById('loading');
const countdown = document.getElementById('countdown');

// Step 1 Get the current year
const currentYear = new Date().getFullYear();
console.log(currentYear)
// step 2 Get new year time
const newYearTime = new Date(`January 01 ${currentYear + 1} 00:00:00`)
console.log(newYearTime)

// step 3 set background year
year.innerText = currentYear + 1

function newYearCount(){
   
    // Get current time
    const currentTime= new Date();
  
    // time difference
    const diff = newYearTime - currentTime;
    console.log(diff)
    const d = Math.floor(diff/1000/60/60/24)
    console.log(d)
    const h = Math.floor(diff/1000/60/60) % 24
    const m = Math.floor(diff/1000/60) % 60
    const s = Math.floor(diff/1000) % 60

    // Add values to DOM
   days.innerHTML = d;
   minutes.innerHTML = m < 10 ? '0' + m : m;
   hours.innerHTML = h < 10 ? '0' + h : h;
   seconds.innerHTML = s < 10 ? '0' + s : s;


}
// Show spinner before countdown

setTimeout(() => {
    loading.remove();
    countdown.style.display = 'flex';
  }, 1000);
  // Run every second

  setInterval(newYearCount, 1000);


newYearCount()