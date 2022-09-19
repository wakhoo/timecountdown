# Time Count Down Clone Project

### source: [vanillawebprojects New Year Countdown](https://vanillawebprojects.com/projects/new-year-countdown/)

---

Hard part

- I didn't know how to connect JS with HTML(DOM)
- I didn't know about detail CSS
- I didn't know how to get current time to JS


How I figgured out
- I didn't know how to connect JS with HTML(DOM)<br>
  I keep watch the DOC but it keep failed, and I found out I was using worng value names. When I fixed this it works!<br>
  <br>
  if I used id in html like this
  ```html
    <div>
        <h1 class="countDown" id="days">00</h1>
        <h2 class="countDown">Days</h2>
    </div>
  ```
  I have to use JS like below
  ```jsx
  
  const days = document.getElementById('days');
  function countDown(){
    ...
    const d = Math.floor(diff / 1000 / 60 / 60 / 24);
    ...
    days.innerHTML=d;
    ...
    }
   ```
   
- I didn't know about detail CSS<br>
  For this I'm just try to add things one by one.
  
  **Ver1**
  
  https://user-images.githubusercontent.com/40779092/190941372-089be7f4-71c5-490a-9f8a-4a91e576290b.mov


    
  **Ver2**

  https://user-images.githubusercontent.com/40779092/190941487-d1ef1d0d-af2d-4a05-bd38-c9c6c548679f.mov

  Removed Scroll and add display: flex, og tags
  
  And get some feedback from friend. He told me add some twitter og tags also, and I fixed display but he still see cropped display.
  
  ![ver2_problem](https://user-images.githubusercontent.com/40779092/190941802-38508aae-ff82-49da-902a-4ff5df595cd1.png)

  **Ver3**
  
  -- preparing --
