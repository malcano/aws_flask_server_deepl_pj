const carouselText = [
    { text: "북런던", color: "red" },
    { text: "울버햄튼", color: "orange" },
    { text: "비야레알", color: "yellow" },
    { text: "첼시", color: "blue" },
    { text: "맨체스터", color: "skyblue" },
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
  