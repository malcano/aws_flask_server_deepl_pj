const carouselText = [
    { text: "국화", color: "coral" },
    { text: "아카시아", color: "seagreen" },
    { text: "델피니움", color: "lavender" },
    { text: "스타티스", color: "hotpink" },
    { text: "아네모네", color: "mediumpurple" },
    { text: "프리지아", color: "white" },
    { text: "장미", color: "red" },
    { text: "유채", color: "yellow" },
    
  ];
  
  window.onload = function () {
    carousel(carouselText, "#feature-text");
  };
  
  async function typeSentence(sentence, eleRef, delay = 100) {
    const letters = sentence.split("");
    let i = 0;
    while (i < letters.length) {
      await waitForMs(delay);
      document.querySelector(eleRef).textContent += letters[i];
      i++;
    }
    return;
  }
  
  async function deleteSentence(eleRef) {
    const sentence = document.querySelector(eleRef).innerHTML;
    const letters = sentence.split("");
    let i = 0;
    while (letters.length > 0) {
      await waitForMs(100);
      letters.pop();
      document.querySelector(eleRef).innerHTML = letters.join("");
    }
  }
  
  async function carousel(carouselList, eleRef) {
    var i = 0;
    while (true) {
      updateFontColor(eleRef, carouselList[i].color);
      await typeSentence(carouselList[i].text, eleRef);
      await waitForMs(1500);
      await deleteSentence(eleRef);
      await waitForMs(500);
      i++;
      if (i >= carouselList.length) {
        i = 0;
      }
    }
  }
  
  function updateFontColor(eleRef, color) {
    document.querySelector(eleRef).style.color = color;
  }
  
  function waitForMs(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
  
  function checkLength(input) {
    if (input.value.length > 49) {
      alert("49자 이하로 입력해주세요.");
      input.value = input.value.substring(0, 49);
    }
  }