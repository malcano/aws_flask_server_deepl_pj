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

  // form 요소를 선택합니다.
const form = document.querySelector('form');

// submit 이벤트가 발생하면 처리할 함수를 등록합니다.
form.addEventListener('submit', (event) => {
  // 기본 동작을 막습니다.
  event.preventDefault();

  // submit 버튼을 선택합니다.
  const submitButton = form.querySelector('input[type="submit"]');

  // 버튼을 비활성화합니다.
  submitButton.disabled = true;

  // 버튼의 값을 "분석중입니다"로 변경합니다.
  submitButton.value = '분석중입니다...';

  // form 요소를 서버로 전송합니다.
  form.submit();
});